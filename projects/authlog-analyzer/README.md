# Auth Log Analyzer

> A command-line tool that reads a Linux authentication log and produces a triage report: what happened on the host, which of it looks like an attack, and which is routine.

![Language](https://img.shields.io/badge/language-python-blue)
![Status](https://img.shields.io/badge/status-v2-yellow)

---

## Why This Was Built

A Linux authentication log (`/var/log/auth.log` on Debian and Ubuntu, `/var/log/secure` on RHEL family, same syslog `auth`/`authpriv` stream underneath) records most of what matters for a first-pass security look at a host: who logged in and how, who failed, who escalated to root and to run what, whether accounts were added or changed, whether the SSH service itself misbehaved. Reading it by eye works until the log is more than a screen long, and then it stops working.

This tool exists to do that first pass automatically. Point it at an auth log and it returns the picture: the SSH authentication activity including any brute-force pattern, and (planned) privilege escalation, account and group changes, session activity, service events, and signs the log itself may be incomplete. The goal is not to declare a verdict on its own. It lays out the full scope, with a severity per finding, so the analyst can tell an intentional attack from an unintentional mistake from a plain system fault, a judgement that needs context, not one alarming line.

It is deliberately not tied to the lab. It came out of needing to read Metasploitable2's auth log during [lab exercise 06](../../analysis/labs/metasploitable2/06-ssh-bruteforce.md), and the sample data at [`sample-data/auth.txt`](sample-data/auth.txt) is the real log from that exercise, but the tool parses the standard syslog auth format and works on any Linux host's log. The lab is where it gets used, not what it is for.

---

## Scope

The finished tool covers six categories of auth log event. The list is closed on purpose, so "done" is definable rather than an open-ended "summarize everything":

1. **SSH authentication** — failed and accepted passwords, public key auth, invalid users, and the brute-force pattern derived from them
2. **Privilege escalation** — `sudo` commands run (who, what, as whom), `sudo` failures (wrong password, user not in sudoers), `su` attempts
3. **Account and group changes** — `useradd`, `userdel`, `usermod`, `passwd`, `groupadd`, `gpasswd`
4. **Sessions** — PAM session opened and closed events, grouped by user, with cron sessions separated from interactive ones
5. **Service events** — `sshd` start, stop, and listening; configuration errors; protocol errors; `Did not receive identification string`
6. **Log continuity** — large time gaps between consecutive entries, syslog or systemd restart markers, rotation markers, anything suggesting the log is not a continuous record

Categories 2 through 6 are not built yet, see Limitations. The current sample log is pure SSH traffic (confirmed: 635 of 635 lines are `sshd`), so there is nothing to build or test those sections against until a richer capture exists, from a future lab exercise that generates real `sudo`/account-change activity.

Separately from these six, the tool takes an optional **known-asset list**, [`sample-data/known_assets.txt`](sample-data/known_assets.txt), the IP addresses expected to legitimately talk to the host (in this lab, Kali and alpine-endpoint). This is not a seventh category, it is context supplied from outside the log that adjusts how findings from the other categories are scored: the same behavior from a recognized host and from a never-seen address should not weigh the same.

---

## What It Does

### v1

Failed-password count per source IP against a fixed threshold. Superseded by v2's fuller analysis.

### v2 (current)

Covers category 1 (SSH authentication) in full, plus the known-asset check. Given an auth log, it:

- Parses every line into timestamp, host, process, and message, and routes each into a per-process bucket (a single pass over the file)
- For the `sshd` bucket, per source IP: counts failed attempts, tracks every distinct username tried, counts attempts against usernames that do not exist, counts accepted logins, and tracks the highest number of distinct TCP connections (by source port) seen in any 60-second window
- Scores each source on four independent signals: failure count over threshold, any invalid-username attempts, a successful login after failing, and a high number of distinct connections in a short window (evaluated only once the failure count already crossed the threshold); an unrecognized source address is a fifth, conditional signal, it only counts if another signal already fired
- Classifies severity by how many signals fired (`INFO` for one, `ALERT` for two, `CRITICAL` for three or more) and reports each finding with the specific reasons behind it

```bash
python main.py sample-data/auth.txt
```

Output against the exercise 06 dataset:

```
SSH Authentication Findings
===========================
INFO: 192.168.10.40
  Failed attempts: 8, distinct users: 1 (msfadmin)
  Accepted attempts: 6, distinct users: 1 (msfadmin)
  Max connections count: 2
  Reason: succeeded after failing (6 accepted login(s) for msfadmin)
CRITICAL: 192.168.10.10
  Failed attempts: 269, distinct users: 6 (user, msfadmin, oracle, admin, test, root)
  Accepted attempts: 1, distinct users: 1 (msfadmin)
  Max connections count: 28
  Reason: 269 failed attempts (threshold 20)
  Reason: 135 attempts against nonexistent usernames
  Reason: succeeded after failing (1 accepted login(s) for msfadmin)
  Reason: more than 3 distinct connections in a short time window (max 28)
```

`192.168.10.40` is a real user who mistyped a password a few times before succeeding, six separate times, over four minutes, always the same account. `192.168.10.10` is the Hydra brute force from the same exercise. The report tells them apart without either being invisible: the legitimate user still shows up, at a severity that says "worth a glance", not "this is an attack". The 28-versus-2 gap in distinct connections is what actually settles the question a raw failure count cannot: `192.168.10.40`'s activity was not concentrated in time (2 connections in any 60-second window is unremarkable for someone reconnecting a few times), where `192.168.10.10`'s was (28). Not every anomaly is malicious, but every anomaly deserves to be seen, and the analyst, not the script, makes the call.

With no argument, it defaults to `sample-data/auth.txt`. `sample-data/known_assets.txt` is used automatically; if a source address in a finding is not in it, and the finding already has another reason, that fact becomes an additional reason and can push the severity up a tier.

---

## How It Works

### File layout

The tool is split across single-purpose modules instead of one growing script, so each responsibility stays visually separate and category 2 onward each get their own file the same way `ssh_auth.py` does:

```
main.py           # entry point: reads argv, wires the pieces together, prints
log_parser.py     # LogEntry, parse_line, load_buckets (generic, not category-specific)
known_assets.py   # load_known_assets
severity.py       # classify_severity (shared by every category's analysis)
ssh_auth.py       # IPStats, extract_ip/user/port, analyze_ssh_auth (category 1)
report.py         # report
```

### Parsing (`log_parser.py`)

Every line has the shape `<mon> <day> <HH:MM:SS> <host> <process>[<pid>]: <message>`. `parse_line` splits it with `line.split(maxsplit=5)`, which stops after the fifth space so the message is captured whole, not broken up. The timestamp is parsed with `datetime.strptime(..., "%b %d %H:%M:%S")` into a real `datetime` object, not kept as a string, so later code can subtract two of them to get a duration. The log has no year; Python defaults to a filler year, which is fine here because only relative differences are ever used, never an absolute date. The process field (`sshd[4848]:`) has its PID and trailing colon stripped down to `sshd`. Each parsed line becomes a `LogEntry` namedtuple (same memory and speed as a plain tuple, but `entry.message` instead of `entry[3]`).

A line that does not split into at least six parts is reported as malformed and skipped, rather than raising and stopping the whole run. `load_buckets` reads the file exactly once and routes each `LogEntry` into a `dict` of lists keyed by process name (`collections.defaultdict(list)`, so a first-seen process gets an empty list automatically). Each bucket is a plain `list`, within a category the events are only ever iterated in order, never looked up by position, a `list` is the minimal structure that fits.

### SSH authentication analysis (`ssh_auth.py`)

`analyze_ssh_auth` walks the `sshd` bucket once and keeps one record per source IP, an `IPStats` `@dataclass` (not a `dict` with string keys): mutable named fields (`failures`, `users`, `invalid_failures`, `accepted`, `accepted_users`, `recent_connections`, `max_connections_count`), each new IP getting its own independent instance via `defaultdict(IPStats)`. `users` and `accepted_users` are `set`s specifically because the question asked of them is always "how many *distinct* names", and a `set` answers "have I seen this one" in O(1) without letting duplicates in. Mutable fields like `set` and `deque` are declared with `field(default_factory=...)`, not a bare `= set()`, because a bare mutable default would be one single object shared across every `IPStats` instance, the same trap as a mutable default argument on a function.

`extract_ip`, `extract_user`, and `extract_port` pull the three pieces out of a message like `Failed password for root from 192.168.10.10 port 51962 ssh2` (or the `invalid user` variant), each wrapped in a `try`/`except IndexError` that returns `None` on an unexpected shape instead of crashing the whole run.

The connection-frequency check is a sliding window over `recent_failures`' ports: each failure's `(timestamp, port)` is appended to `recent_connections`, then anything older than `window_seconds` is dropped from the front, then the count of *distinct* ports currently in the window is compared against the best seen so far. A `deque` is the right structure for the drop-from-the-front step specifically: `deque.popleft()` is O(1) because a deque is a doubly-linked sequence of blocks, where a plain `list`'s `pop(0)` is O(n), shifting every remaining element down by one. Counting distinct ports rather than raw failure lines matters because SSH allows several password attempts per TCP connection, so "how many failures" and "how many separate connections" are different questions with different answers, one automated tool opening 28 connections in a minute is a much stronger tell than a raw failure count alone.

Once every line is counted, a second pass over the per-IP records decides which sources get reported and why. Each of four conditions is its own independent `if`, appending its own reason when it fires: they are deliberately not `elif`, because more than one can be true for the same source and all of them should count. The connection-frequency check is additionally gated on the failure count already being over threshold (`s.failures > threshold and s.max_connections_count > connection_threshold`), so a source with a handful of ordinary reconnects, but no real failure volume, does not get flagged for that alone. The known-asset check is gated differently, on `reasons` already being non-empty, so a clean, never-before-seen address is not noise by itself. `classify_severity` maps how many reasons fired to a tier (`INFO`, `ALERT`, `CRITICAL`), an additive score instead of a hand-set flag, so a fifth or sixth signal later is one more `if` block, not a rewrite of the severity logic.

Counting and deciding are two separate passes on purpose. An earlier version decided inside the counting loop and appended a finding on every single line once a source crossed the threshold, producing over 200 duplicate entries for one IP. The function that detects should return data, not print, and should decide once per subject, not once per event.

A raw failure-rate check (a sliding window counting *all* recent failures, not distinct connections) was built, tested, and then retired once the connection-count check existed: on real SSH traffic the two are highly correlated, since a connection can only carry so many attempts before OpenSSH cuts it off, and distinct-connection count is the more precise of the two for telling "one client retrying" from "many separate connection attempts". Keeping both would have been redundant.

### Known-asset check (`known_assets.py`)

`load_known_assets` reads a plain text file, one IP per line, into a `set`. It is loaded from `sample-data/known_assets.txt` for this lab's data, but the function itself takes any path, and the tool works with an empty or missing list, it just cannot use that particular signal without one.

---

## Usage

```bash
python main.py [path-to-auth-log]
```

No dependencies beyond the Python standard library.

---

## Planned

- **v3:** categories 2 through 6 (privilege escalation, account and group changes, sessions, service events, log continuity), once a richer capture with that activity exists, each in its own module following `ssh_auth.py`'s pattern, plus a synthesized summary at the top of the report across all sections.

---

## What Was Learned

**A variable set inside one `if` branch is not defined in the others, it just looks like it is.** This came up twice. First, `ip_address` computed only inside the `"Accepted password"` branch, silently reused stale in the `"Failed password"` branch below it, misattributing every failure to whichever address last succeeded. Later, during the refactor into `extract_ip`/`extract_user` helpers, the same class of bug reappeared: `user` got extracted at the top of the `"Failed password"` branch, then a later cleanup pass removed it while deleting genuinely redundant re-extractions further down, leaving `stats[ip].users.add(user)` reading a `user` left over from the last `"Accepted password"` line instead of the current one. No crash either time, just a wrong answer. Refactoring a fix does not make the underlying lesson stick automatically, the same failure mode can slip back in through a different edit.

**Code indented one level too shallow runs once, not once per iteration, and still runs without error.** Two lines meant to execute inside a `for` loop ended up dedented to the loop's own level, ran exactly once after the loop finished, using whatever values survived from the final iteration.

**Deciding inside the counting loop duplicates the decision.** An early version appended a finding every time a running total crossed the threshold, once per subsequent line, not once per source. Counting (one pass over every event) and deciding (one pass over the per-source totals, afterward) have to be separate loops.

**A weak signal is still worth showing, just not at the same weight as a strong one.** A first pass suppressed "succeeded after failing" entirely unless a stronger reason had already fired, reasoning that the pattern alone is normal human behavior. That went too far: it is also the exact pattern behind credential stuffing, a stolen device, or someone targeting a specific person's account, cases the tool should never silently hide. The fix was proportional severity, not visibility: every source with any reason is reported, and an additive score does the weighting.

**Two signals measuring different things should stay two signals, even if they usually move together.** Failure count and distinct-connection count were briefly merged into one combined `if` (`failures > threshold and connections > connection_threshold`), producing a single reason instead of two. That loses resolution: a source that trips only one of the two would get zero credit under the merged version, where it would have earned a point under either check alone. Keeping every independent condition as its own `if`, each appending its own reason, is the same pattern used everywhere else in the file, merging just these two was the inconsistent choice, not the correct one.

**`datetime` the module and `datetime` the class share a name on purpose, and it bites you exactly once.** `import datetime` binds the module; calling `datetime.strptime(...)` on it fails with `AttributeError: module 'datetime' has no attribute 'strptime'`, because `strptime` lives on the `datetime.datetime` class, not the module itself. `from datetime import datetime` binds the class directly under the same name, which is what the working code actually needs. This surfaced when the parsing logic was moved into its own module and the import got rewritten from memory instead of copied.

**A missing year does not block duration math.** The log's timestamps have no year. `datetime.strptime` fills one in on its own, and since every calculation here is a subtraction between two timestamps from the same file (`timedelta.total_seconds()`), the filler year cancels out.

---

## Limitations

- Only category 1 of the six-category scope (SSH authentication) is built. Categories 2 through 6 need a richer sample log (real `sudo`, account-change, and session activity) that does not exist yet.
- The known-asset check is binary presence in a flat list. It has no concept of a host being newly added, temporarily expected, or partially trusted.
- Thresholds (`threshold`, `window_seconds`, `connection_threshold`) are constants chosen to fit this dataset, not calibrated against a larger or more varied corpus.
- IP, user, and port extraction assume the exact `... from <IP> port <N> ssh2` line shape OpenSSH uses. A different SSH daemon or a customized log format needs a different parser.
- IPv6 source addresses are not handled. The sample data is IPv4 only.
- A log spanning a year boundary would break the timestamp math, since the parsed year is a fixed filler value, not read from the log.
