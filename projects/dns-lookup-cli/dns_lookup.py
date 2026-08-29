import sys
import dns.resolver
import whois


def get_whois_info(domain: str) -> None:
    """Query and print WHOIS registration data for a domain."""
    try:
        w = whois.whois(domain)

        # Display key WHOIS fields (some may be None depending on the TLD)
        print(f"Domain Name: {w.domain_name}")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Name Servers: {w.name_servers}")
        print(f"Status: {w.status}")
        print(f"Emails: {w.emails}")
    except whois.parser.PywhoisError as e:
        print(f"WHOIS lookup failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Read the domain from the command line argument
    domain = sys.argv[1] if len(sys.argv) > 1 else None

    # Use Google's public DNS server instead of the system default.
    # See README.md "What Was Learned" for why this is a deliberate
    # choice, not just a default, and what it trades off.
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8']

    # Query the main DNS record types for the domain
    record_types = ['A', 'MX', 'NS', 'TXT']
    for record_type in record_types:
        try:
            answers = resolver.resolve(domain, record_type)
            print(f"{record_type} records:")
            for rdata in answers:
                print(rdata.to_text())
        except dns.resolver.NoAnswer:
            print(f"No {record_type} records for {domain}")
        except dns.resolver.NXDOMAIN:
            print(f"Domain {domain} not found")
        except Exception as e:
            print(f"Error querying {record_type} records: {e}")

    # Query domain registration data
    get_whois_info(domain)
