# DNS Lookup CLI Tool

> A command-line tool that queries a domain's DNS records and registration data, encrypted by default, with local caching.

![Language](https://img.shields.io/badge/language-python-blue)
![Status](https://img.shields.io/badge/status-v3%20complete-green)

---

## Why This Was Built

The actual motivation is investigative, not procedural: if you come across a suspicious domain (a phishing lookalike, an IOC cited in someone else's report, something a coworker flags as "this looks off"), this is the first tool you reach for to build a picture of it. When was it registered, is that recent enough to be a red flag on its own? What does it resolve to? Who else's infrastructure does it share (registrar, name servers)? Is it locked against unauthorized transfer, or exposed to takeover? None of that requires trusting someone else's write-up, it is independently checkable, from public data, in seconds. That is also what re-verifying an IOC actually means in practice, not just copying an indicator from a report, but confirming what it currently looks like.

A second motivation grew out of the first version: once the tool existed, it became a deliberate exercise in not trusting the query path either. An investigative tool that leaks every domain it looks up to whoever is watching the network, or to whichever server it happens to ask, is a liability, not just an inconvenience. Everything added after the first version (encrypted DNS, encrypted registration data, caching) was about closing that gap, not about a feature checklist.

---

## What It Does

Given a domain name as a command-line argument, it queries and prints:

- The domain's `A`, `AAAA`, `MX`, `NS`, `CNAME`, `SOA`, `TXT`, and `CAA` DNS records, encrypted by default (DNS-over-HTTPS)
- Registration data via RDAP (registrar, creation date, expiration date, name servers, status codes), also encrypted by default (HTTPS)
- Both are cached locally (`dns_cache.json`), respecting each DNS record's own TTL, and a fixed 24-hour window for RDAP data (which has no TTL of its own)

```bash
python dns_lookup.py cloudflare.com
```

optionally followed by a resolver argument to override the default:

```bash
python dns_lookup.py cloudflare.com https://dns.google/dns-query 8.8.8.8   # a different DoH provider (URL + matching bootstrap IP)
python dns_lookup.py cloudflare.com 1.1.1.1                                 # explicit opt-out: plain, unencrypted DNS
```

---

## How It Works

### DNS resolution

Queries go through `dnspython`'s `Resolver` object. Three cases, decided from the command-line arguments:

1. **Nothing specified (the default):** DNS-over-HTTPS via Google (`https://dns.google/dns-query`), with the matching bootstrap IP (`8.8.8.8`) hardcoded.
2. **A second argument starting with `https://`:** a different DoH provider. This requires a *third* argument, the bootstrap IP for that specific URL, and refuses to continue without one, see Bootstrapping below for why a guessed default is actively wrong here.
3. **A second argument that is a plain IP:** explicit opt-out of encryption, plain DNS to that server.

Each of the eight record types is queried independently, with three tiers of error handling: `dns.resolver.NoAnswer` (the domain exists but has no record of that type, common and not an error), `dns.resolver.NXDOMAIN` (the domain does not exist), and a general `Exception` fallback.

### Registration data (RDAP, not WHOIS)

The original version used `python-whois`, which speaks the legacy WHOIS protocol (plain TCP port 43, no encryption, no equivalent of DoH exists for it at scale). It was fully replaced with **RDAP**, the modern, HTTPS/JSON-based successor, once it was clear the tool could not honestly be called "secure" while still leaking every registration lookup in plaintext.

`https://rdap.org/domain/<domain>` is a bootstrap redirect service, it automatically routes to whichever registry actually holds authoritative data for that domain's TLD, so no per-TLD server list has to be maintained here. The response is a nested JSON object, not a flat one:

- `ldhName`, `status`: direct fields
- `nameservers`: a list of objects, `ldhName` extracted from each
- `events`: a flat list of `{eventAction, eventDate}` pairs, searched for the entries where `eventAction` is `"registration"` or `"expiration"`
- Registrar name: the most deeply nested field, requires finding the entity in `entities` whose `roles` includes `"registrar"`, then searching that entity's `vcardArray` for the property named `"fn"`

### Caching

Both DNS and RDAP results are cached in a single local file (`dns_cache.json`), so an unchanged repeat lookup doesn't re-query at all. DNS records use dnspython's own `answers.expiration` (an absolute Unix timestamp derived from that specific answer's TTL, different per record type). RDAP has no equivalent field in the protocol, so it uses a fixed, chosen 24-hour window instead, registration data changes rarely enough that this is a reasonable default, not a measured one.

---

## Usage

```bash
pip install dnspython[doh] requests
python dns_lookup.py <domain> [resolver] [bootstrap_ip]
```

Examples:

```bash
python dns_lookup.py cloudflare.com                                          # default: encrypted, Google DoH
python dns_lookup.py cloudflare.com https://cloudflare-dns.com/dns-query 1.1.1.1   # a different DoH provider
python dns_lookup.py cloudflare.com 1.1.1.1                                  # opt out of encryption
```

`python-whois` is no longer a dependency, RDAP replaced it entirely.

---

## What Was Learned

**Bootstrapping is a real, named protocol problem, not an edge case.** Connecting to a DoH server identified by hostname (`https://dns.google/dns-query`) requires resolving that hostname first, and the only way to do that is... a DNS query, the exact thing being encrypted in the first place. dnspython's `DoHNameserver` exposes a `bootstrap_address` parameter specifically to break this cycle (connect to the literal IP directly, skip hostname resolution). There is no safe universal default for it: an early version defaulted the bootstrap IP to Cloudflare's (`1.1.1.1`) regardless of which provider's URL was being used, and testing it against Google's URL without an explicit override produced `CERTIFICATE_VERIFY_FAILED: Hostname mismatch, certificate is not valid for 'dns.google'`, a real, correct TLS rejection, because the tool was connecting to Cloudflare's server while presenting Google's hostname. The fix was to require the bootstrap IP explicitly whenever a DoH URL is given, and refuse to guess.

**Two exceptions can look interchangeable and are not.** Chaining `print(...) and sys.exit(1)` inside a one-liner silently failed to exit, because `print()` always returns `None`, which is falsy, so `and` short-circuits before reaching `sys.exit()`. Swapping to `or` fixed it, for the exact opposite reason (`or` only evaluates its right side when the left one is falsy). Both versions run without a syntax error, only one is correct, and the failure was silent, the script just kept going with a broken value instead of stopping.

**Not every DNS record type fits the same query shape.** `PTR` (reverse lookup, keyed by IP address in a completely different zone) and `SRV` (keyed by a service-prefixed name, e.g. `_sip._tcp.domain`) were added to the record-type list, then removed, because querying them by plain domain name the same way as `A` or `MX` doesn't match how they are actually meant to be looked up, they would always return empty, not because the domain lacks them, but because the question being asked was the wrong shape.

**A cache needs to handle its "value has expired" branch as carefully as its "value exists" branch.** An early version's expired-cache path printed "...expired, querying DNS server..." and then did nothing, because the actual query logic was nested only under the sibling branch for "never cached at all". The message lied, no query happened, the loop just moved on. The fix was structural: only the confirmed-valid-cache path gets a `continue`, every other path (missing or expired) falls through to the same query code, once, rather than duplicating it per case.

**RDAP is a large improvement over WHOIS in structure, not just encryption.** WHOIS returns loosely formatted text designed for a human to read, `python-whois` parses it into best-effort flat attributes. RDAP returns actual structured JSON, but nests three of the most useful fields (dates, nameservers, registrar) inside arrays that have to be searched by key, not indexed by position, a version that read `vcardArray[1][0][3]` (assuming the registrar's name is always the first vCard property) broke silently, because `"version"` came first in the real data, not `"fn"`. Searching by name instead of trusting position was the actual fix.

**WHOIS/RDAP lookups and DNS lookups are genuinely different problems**, even though this tool bundles both under one command. DNS record data comes with a self-describing validity window (TTL) built into the protocol response, RDAP does not, so caching it required picking an arbitrary duration rather than reading one from the data. Two different caching strategies coexisting in the same cache file, for a principled reason, not an oversight.

**Catching the right *family* of exceptions matters, not just catching something.** `get_rdap_info`'s exception handling originally only covered `requests.exceptions.RequestException`, network and HTTP-level failures. But the nested field extraction that follows a successful request (searching `entities` for the one with a `"registrar"` role, then its `vcardArray` for the `"fn"` property) can fail for reasons that have nothing to do with the network, a TLD or regional RDAP server returning a thinner response than expected, missing a `vcardArray` entirely, or no entity carrying the `"registrar"` role at all. Those raise `KeyError`, `TypeError`, or `IndexError`, none of which are `RequestException`, so the original `except` clause let them through uncaught. Fixed by catching the specific tuple of exception types that can actually occur at each stage, not just the one from the network call.

**`NXDOMAIN` is a statement about the domain, not about one record type.** The DNS loop originally caught `NXDOMAIN` per record type and kept going, meaning a genuinely nonexistent domain produced the same "not found" message eight times, once per type, before still going on to query RDAP, which would predictably fail too. `NXDOMAIN` means the domain itself doesn't exist, that fact doesn't change across record types, so it only needs establishing once. Fixed with a flag set on the first `NXDOMAIN`, breaking out of the record-type loop immediately, and skipping the RDAP call entirely when it's set.

---

## Limitations

- Single-domain only. It does not find other domains related to the one queried (shared registrant, shared infrastructure), that kind of pivoting typically depends on passive DNS or reverse WHOIS/RDAP data this tool does not have access to. Deliberate scope boundary, not a gap.
- Encrypted is not the same as anonymous. By default, every query (DNS and RDAP) is visible to whichever provider answers it (Google for DoH, the authoritative RDAP registry for registration data). True anonymity is a different, unaddressed problem.
- The RDAP 24-hour cache window is a reasonable default, not a measured one, the protocol gives no signal for how long a value should actually be considered fresh.
- No rate limiting beyond what caching incidentally provides. A script that queried many different domains in a loop could still be throttled by `rdap.org` or an upstream registry.
- Only `A`, `AAAA`, `MX`, `NS`, `CNAME`, `SOA`, `TXT`, and `CAA` are covered. `PTR` and `SRV` were deliberately excluded, see What Was Learned above.
