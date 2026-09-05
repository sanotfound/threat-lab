def load_known_assets(path):
    known_assets = set()
    with open(path, "r") as f:
        for line in f:
            if ip := line.strip():
                known_assets.add(ip)
    return known_assets