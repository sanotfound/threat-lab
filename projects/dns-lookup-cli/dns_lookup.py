import sys
import dns.resolver
import dns.nameserver
import time
import json
import requests


def get_rdap_info(domain, cache):
    """Query and print RDAP registration data for a domain, using a 24h cache."""
    if domain in cache and "rdap" in cache[domain]:
        cached_data = cache[domain]["rdap"]
        expiration = cached_data.get("expiration", 0)
        if time.time() < expiration:
            print(f"Using cached RDAP data for {domain}:")
            print(json.dumps(cached_data["data"], indent=4))
            return
        else:
            print(f"Cached RDAP data for {domain} has expired. Querying RDAP server...")

    try:
        if domain not in cache:
            cache[domain] = {}

        # rdap.org bootstraps to the correct authoritative RDAP server for this domain's TLD
        rdap_url = f"https://rdap.org/domain/{domain}"
        response = requests.get(rdap_url)
        response.raise_for_status()
        data = response.json()

        print(f"Domain Name: {data['ldhName']}")
        print(f"Status: {data['status']}")

        nameservers = [ns["ldhName"] for ns in data["nameservers"]]
        print(f"Name Servers: {nameservers}")

        # events is a flat list of {eventAction, eventDate}, search it for the ones we want
        creation_date = None
        expiration_date = None
        for event in data["events"]:
            if event["eventAction"] == "registration":
                creation_date = event["eventDate"]
            elif event["eventAction"] == "expiration":
                expiration_date = event["eventDate"]
        print(f"Creation Date: {creation_date}")
        print(f"Expiration Date: {expiration_date}")

        # the registrar's name is nested: find the entity with role "registrar",
        # then find its "fn" (formatted name) property inside vcardArray
        registrar_entity = None
        for entity in data["entities"]:
            if "registrar" in entity["roles"]:
                registrar_entity = entity

        registrar_name = None
        for prop in registrar_entity["vcardArray"][1]:
            if prop[0] == "fn":
                registrar_name = prop[3]
        print(f"Registrar: {registrar_name}")

        rdap_summary = {
            "domain_name": data['ldhName'],
            "status": data['status'],
            "nameservers": nameservers,
            "creation_date": creation_date,
            "expiration_date": expiration_date,
            "registrar": registrar_name,
        }
        cache[domain]["rdap"] = {"data": rdap_summary, "expiration": time.time() + 86400}

    except requests.exceptions.RequestException as e:
        print(f"Error fetching RDAP data: {e}")


if __name__ == "__main__":
    # Read the domain from the command line argument
    domain = sys.argv[1] if len(sys.argv) > 1 else None
    resolver = dns.resolver.Resolver()

    try:
        with open("dns_cache.json", "r") as arquivo:
            cache = json.load(arquivo)
    except FileNotFoundError:
        cache = {}

    if len(sys.argv) > 2 and sys.argv[2].startswith('https://'):
        # Explicit DoH URL provided, requires an explicit bootstrap IP too
        print(f"Using DoH nameserver: {sys.argv[2]}")
        bootstrap_address = sys.argv[3] if len(sys.argv) > 3 else print("No bootstrap address provided for DoH nameserver. System is shutting down.") or sys.exit(1)
        ns = dns.nameserver.DoHNameserver(sys.argv[2], bootstrap_address=bootstrap_address)
        resolver.nameservers = [ns]

    elif len(sys.argv) > 2:
        # Plain IP(s) provided, explicit opt-out of encryption
        print(f"Using custom DNS resolver: {sys.argv[2]}")
        resolver.nameservers = sys.argv[2:]

    else:
        # Nothing specified, default to encrypted DoH (Google)
        print("Using default DoH nameserver: https://dns.google/dns-query")
        ns = dns.nameserver.DoHNameserver("https://dns.google/dns-query", bootstrap_address="8.8.8.8")
        resolver.nameservers = [ns]

    # Query the main DNS record types for the domain
    record_types = ['A', 'MX', 'NS', 'TXT', 'AAAA', 'CNAME', 'SOA', 'CAA']
    for record_type in record_types:
        if domain in cache and record_type in cache[domain]:
            cached_data = cache[domain][record_type]
            expiration = cached_data.get("expiration", 0)
            if time.time() < expiration:
                print(f"Using cached {record_type} records for {domain}:")
                for rdata in cached_data["data"]:
                    print(rdata)
                continue
            else:
                print(f"Cached {record_type} records for {domain} have expired. Querying DNS server...")
        else:
            print(f"No cached {record_type} records for {domain}. Querying DNS server...")

        try:
            answers = resolver.resolve(domain, record_type)

            if domain not in cache:
                cache[domain] = {}
            lista_de_textos = [rdata.to_text() for rdata in answers]
            cache[domain][record_type] = {"data": lista_de_textos, "expiration": answers.expiration}

            for rdata in answers:
                print(rdata.to_text())

        except dns.resolver.NoAnswer:
            print(f"No {record_type} records for {domain}")

        except dns.resolver.NXDOMAIN:
            print(f"Domain {domain} not found")

        except Exception as e:
            print(f"Error querying {record_type} records: {e}")

    # Query domain registration data (also updates cache)
    get_rdap_info(domain, cache)

    with open("dns_cache.json", "w") as arquivo:
        json.dump(cache, arquivo)
