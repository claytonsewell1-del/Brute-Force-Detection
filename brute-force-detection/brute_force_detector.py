from collections import defaultdict
import re

THRESHOLD = 5
failed_attempts = defaultdict(int)

with open("auth.log", "r") as log:
    for line in log:
        if "Failed password" in line:
            ip_match = re.search(r'(\d{1,3}(?:\.\d{1,3}){3})', line)
            if ip_match:
                ip = ip_match.group(1)
                failed_attempts[ip] += 1

print("\n?? Potential Brute Force Attacks Detected:\n")

for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        print(f"IP Address: {ip} | Failed Attempts: {count}")
