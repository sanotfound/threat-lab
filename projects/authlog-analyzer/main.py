import sys

from log_parser import load_buckets
from known_assets import load_known_assets
from ssh_auth import analyze_ssh_auth
from report import report

def main():
    log_path = sys.argv[1] if len(sys.argv) > 1 else "sample-data/auth.txt"
    known_assets = load_known_assets("sample-data/known_assets.txt")
    buckets = load_buckets(log_path)
    ssh_findings = analyze_ssh_auth(buckets["sshd"], known_assets)
    report(ssh_findings, "SSH Authentication Findings")

if __name__ == "__main__":
    main()