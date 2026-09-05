
from collections import defaultdict, deque
from dataclasses import dataclass, field

from severity import classify_severity

@dataclass
class IPStats:
    failures: int = 0
    invalid_failures: int = 0
    accepted: int = 0
    users: set = field(default_factory=set)
    accepted_users: set = field(default_factory=set)
    recent_connections: deque = field(default_factory=deque)
    max_connections_count: int = 0

def extract_ip(message):
    try:
        return message.split("from ")[1].split(" port")[0]
    except IndexError:
        return None

def extract_user(message):
    try:
        if "invalid user" in message:
            return message.split("invalid user ")[1].split(" from")[0]
        else:
            return message.split(" for ")[1].split(" from")[0]
    except IndexError:
        return None

def extract_port(message):
    try:
        return message.split(" port ")[1].split(" ")[0]
    except IndexError:
        return None
    
def analyze_ssh_auth(entries, known_assets, threshold=20, window_seconds=60, connection_threshold=3):
    stats = defaultdict(IPStats)

    for entry in entries:
        if "Accepted password" in entry.message:
            user = extract_user(entry.message)
            ip_address = extract_ip(entry.message)
            if ip_address is None or user is None:
                print(f"Warning: Could not extract IP or user from message: {entry.message}")
                continue
            stats[ip_address].accepted += 1
            stats[ip_address].accepted_users.add(user)
            continue

        if "Failed password" not in entry.message:
            continue

        ip_address = extract_ip(entry.message)
        user = extract_user(entry.message)
        if ip_address is None or user is None:
            print(f"Warning: Could not extract IP or user from message: {entry.message}")
            continue

        port = extract_port(entry.message)
        if port is not None:
            conn_window = stats[ip_address].recent_connections
            conn_window.append((entry.timestamp, port))
            while conn_window and (entry.timestamp - conn_window[0][0]).total_seconds() > window_seconds:
                conn_window.popleft()
            distinct_connections = len(set(port for _, port in conn_window))
            stats[ip_address].max_connections_count = max(stats[ip_address].max_connections_count, distinct_connections)

        if "invalid user" in entry.message:
            stats[ip_address].invalid_failures += 1
        stats[ip_address].failures += 1
        stats[ip_address].users.add(user)

    findings = []
    for ip_address, s in stats.items():
        reasons = []

        if s.failures > threshold:
            reasons.append(f"{s.failures} failed attempts (threshold {threshold})")
        if s.invalid_failures > 0:
            reasons.append(f"{s.invalid_failures} attempts against nonexistent usernames")
        if s.accepted > 0 and s.failures > 0:
            reasons.append(f"succeeded after failing ({s.accepted} accepted login(s) for {', '.join(s.accepted_users)})")
        if reasons and ip_address not in known_assets:
            reasons.append("source is not in the known asset list")
        if s.max_connections_count > connection_threshold and s.failures > threshold:
            reasons.append(f"more than {connection_threshold} distinct connections in a short time window (max {s.max_connections_count})")
        if reasons:
            severity = classify_severity(len(reasons))
            findings.append((ip_address, s, reasons, severity))
    return findings