# DNS Lookup CLI Tool

> A command-line tool that queries a domain's core DNS records and WHOIS registration data.

![Language](https://img.shields.io/badge/language-python-blue)
![Status](https://img.shields.io/badge/status-v2%20complete-green)

---

## Why This Was Built

The actual motivation is investigative, not procedural: if you come across a suspicious domain (a phishing lookalike, an IOC cited in someone else's report, something a coworker flags as "this looks off"), this is the first tool you reach for to build a picture of it. When was it registered, is that recent enough to be a red flag on its own? What does it resolve to? Who else's infrastructure does it share (registrar, name servers)? Is it locked against unauthorized transfer, or exposed to takeover? None of that requires trusting someone else's write-up, it is independently checkable, from public data, in seconds. That is also what re-verifying an IOC actually means in practice, not just copying an indicator from a report, but confirming what it currently looks like.

---

## What It Does

Given a domain name as a command-line argument, it queries and prints:

- The domain's `A`, `MX`, `NS`, and `TXT` DNS records
- WHOIS registration data: registrar, creation date, expiration date, name servers, EPP status codes, and contact emails (when not privacy-masked)

---

## How It Works

DNS queries go through `dnspython`'s `Resolver` object, deliberately pointed at Google's public resolver (`8.8.8.8`) rather than the system's configured DNS servers. This was originally a fix for a real problem (the system's own DNS servers were timing out), but it turned out to be the right default for a reason beyond that specific bug: an investigative tool should read a domain's public DNS state from a neutral, reliable vantage point, not through a local network's resolver, which may filter, redirect, or otherwise alter what comes back without that being visible to the tool. See What Was Learned below for the trade-offs of that choice, it is not free.

Each of the four record types is queried independently inside a loop, with three tiers of error handling: `dns.resolver.NoAnswer` (the domain exists but has no record of that type, common and not an error condition), `dns.resolver.NXDOMAIN` (the domain does not exist at all), and a general `Exception` fallback for anything else (including the timeout that originally motivated the resolver change).

WHOIS uses a separate, unrelated protocol and library (`python-whois`), queried independently of the DNS lookups above.

---

## Usage

```bash
pip install dnspython python-whois
python dns_lookup.py <domain>
```

Example:

```bash
python dns_lookup.py cloudflare.com
```

---

## What Was Learned

- WHOIS operates at the level of the registered (apex) domain, not a subdomain. Querying `g1.globo.com` correctly returned registration data for `globo.com`, a subdomain has no registration or expiration date of its own, it exists entirely under the authority of whoever controls the root domain.
- A subdomain commonly has no `MX`, `NS`, or `TXT` records of its own (mail, name service, and TXT-based configuration are usually set at the domain root), so "no records" for a subdomain query is expected behavior, not a failure.
- An MX record's leading number is a preference order among multiple mail servers *for the same domain* (lower is tried first), not a ranking against anything external. `0 .` (priority zero, target the root) is the "null MX" record defined in RFC 7505, a domain's explicit declaration that it does not accept email at all, usually paired with an SPF record ending in `-all`.
- TXT records accumulate over a domain's life mostly as domain-ownership proofs for third-party services (Google, Facebook, DocuSign, Zoom, and so on each ask for a unique token placed in DNS to confirm administrative control). The list of these, even without decoding any value, is a passive fingerprint of which external services an organization actually uses.
- An SPF record's `include:` list names every third party authorized to send mail as that domain, another passive fingerprint of an organization's vendor relationships, built entirely from public DNS.
- WHOIS contact emails are commonly `None` today, not a query failure, most registrars have masked this by default since GDPR-era privacy rules took effect (~2018).
- EPP status codes in WHOIS output (`clientDeleteProhibited`, `clientTransferProhibited`, `clientUpdateProhibited`) are anti-hijacking locks a registrar can set on a domain. Their absence is itself a signal, a domain without these locks is more exposed to unauthorized transfer or takeover.

**Why this matters beyond the script itself:** the point of building this was never the domain lookup in isolation. In a real investigation, DNS and WHOIS data are how an analyst pivots from one known-malicious domain to related infrastructure run by the same actor (shared registrar, shared name servers, shared hosting), how a domain's age gets used as a phishing risk signal, and how an IOC cited in someone else's report gets independently re-verified rather than taken on faith. This tool produces the per-domain detail that kind of investigation depends on, it does not (yet) do the pivoting itself, see Limitations.

**The resolver choice, with its trade-off named honestly:** pointing every query at `8.8.8.8` makes results more reliable and reproducible across different networks, but it is not free. Every domain queried through this tool is visible to Google as the resolver. The query itself also travels unencrypted (plain UDP port 53, no DNS-over-HTTPS/TLS), which means it is interceptable by the same class of on-path attacker built and studied firsthand in [lab exercise 05](../../analysis/labs/metasploitable2/05-arp-poisoning-mitm.md). None of this was a reason to avoid the choice, the alternative (the system's own resolver, un-auditable and in this case non-functional) was worse for this tool's specific purpose, but it is a real limitation, not a solved problem.

---

## Limitations

- Single-domain only. It does not find other domains related to the one queried (shared registrant, shared infrastructure), that kind of pivoting typically depends on passive DNS or reverse WHOIS data this tool does not have access to.
- DNS resolver is hardcoded to `8.8.8.8`, not configurable via a flag. Comparing results across different resolvers (which can itself reveal DNS hijacking or regional filtering) is not possible yet.
- Only four record types are covered (`A`, `MX`, `NS`, `TXT`). No `AAAA` (IPv6), `CNAME`, `SOA`, or `CAA`.
- The query itself is unencrypted and not anonymized, see What Was Learned above.
- No caching or rate limiting; repeated runs against the same domain always issue fresh queries.
