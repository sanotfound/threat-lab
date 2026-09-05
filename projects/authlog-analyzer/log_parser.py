from collections import defaultdict, namedtuple
from datetime import datetime

LogEntry = namedtuple("LogEntry", ["timestamp", "host", "process", "message"])


def parse_line(line):
    parts = line.split(maxsplit=5)
    if len(parts) < 6:
        bad_formated_line = line.strip()
        print(f"Warning: Line is not in expected format: {bad_formated_line}")
        return None
    timestamp = datetime.strptime(" ".join(parts[:3]), "%b %d %H:%M:%S")
    host = parts[3]
    process = parts[4].split("[")[0].rstrip(":")
    message = parts[5].rstrip("\n")

    return LogEntry(timestamp, host, process, message)

def load_buckets(log_path):
    buckets = defaultdict(list)
    with open(log_path, "r") as log_file:
        for line in log_file:
            log_entry = parse_line(line)
            if log_entry is None:
                continue
            buckets[log_entry.process].append(log_entry)
    return buckets