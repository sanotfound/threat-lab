def classify_severity(signal_count):
    if signal_count >= 3:
        return "CRITICAL"
    if signal_count == 2:
        return "ALERT"
    return "INFO"