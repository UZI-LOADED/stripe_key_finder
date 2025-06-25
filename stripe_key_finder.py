#!/usr/bin/env python3
import os, re, requests, sys

def find_keys(path):
    rx = re.compile(r"sk_live_[0-9a-zA-Z]{24,}")
    keys = set()
    for root,_,files in os.walk(path):
        for f in files:
            if f.endswith(('.js','.env','.py','.php','.txt','.md')):
                for i,ln in enumerate(open(os.path.join(root,f), errors='ignore'),1):
                    for match in rx.findall(ln):
                        keys.add((match, f"{root}/{f}:{i}"))
    return keys

def validate_key(key):
    r = requests.get("https://api.stripe.com/v1/account", auth=(key, ""))
    return r.status_code == 200

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Usage: stripe_key_finder.py /path/to/code")
        sys.exit(1)
    found = find_keys(sys.argv[1])
    for key, loc in found:
        valid = validate_key(key)
        print(f"{'[VALID]' if valid else '[INVALID]'} {key} – found at {loc}")
