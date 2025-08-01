import re
from datetime import datetime

def log_parser(log_content):
    timestamp_pattern=r'(?:[A-Z][a-z]{2} \d{2} \d{2}:\d{2}:\d{2}|\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
    suspicious_patterns = [
        "failed login", "login failed", "unauthorized access", "access denied", "malware", "malicious activity detected", "virus detected"
    ]
    
    combined_pattern=[]
    for pattern in suspicious_patterns:
        combined_pattern.append(re.compile(pattern,re.IGNORECASE))
    
    # print(combined_pattern)
    try:
        alerts=[]
        
        for line in log_content.splitlines():
            for pattern in combined_pattern:
                if pattern.search(line):
                    timestamp=re.search(timestamp_pattern, line)
                    # print(pattern,line)
                    # print(timestamp)
                    if timestamp:
                        timestamp=timestamp.group(0)
                    else:
                        timestamp="unknown time"
                    # print(f"ALERT: {pattern.pattern.upper()} DETECTED AT {timestamp}")
                    alerts.append(f"ALERT: {pattern.pattern.upper()} DETECTED AT {timestamp}")
                    break
        print("alerts inside parser:", alerts)
        return alerts
        
    except Exception as e:
        print(str(e))
    finally:
        print("End of function :-D")
# log_parser("system_log.txt")

