def report(findings, title):
    print(f"\n{title}")
    print("=" * len(title))
    if not findings:
        print("No findings.")
    else:
        for ip, s, reasons, severity in findings:
            print(f"{severity}: {ip}")
            print(f"  Failed attempts: {s.failures}, distinct users: {len(s.users)} ({', '.join(s.users)})")
            print(f"  Accepted attempts: {s.accepted}, distinct users: {len(s.accepted_users)} ({', '.join(s.accepted_users)})")
            print(f"  Max connections count: {s.max_connections_count}")
            for reason in reasons:
                print(f"  Reason: {reason}")