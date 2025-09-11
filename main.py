#!/usr/bin/env python3
import argparse
import requests

def scan(url, wordlist, param):
    with open(wordlist, "r") as f:
        payloads = [line.strip() for line in f if line.strip()]

    for payload in payloads:
        try:
            params = {param: payload}
            r = requests.get(url, params=params, timeout=10, verify=False)

            if payload in r.text:
                print(f"[!] Reflection found with payload: {payload}")
            else:
                print(f"[-] No reflection: {payload}")

        except Exception as e:
            print(f"[!] Error testing payload {payload}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple reflection scanner PoC")
    parser.add_argument("-u", "--url", required=True, help="Target URL, e.g. http://site.com/page")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file with payloads")
    parser.add_argument("-p", "--param", default="script", help="Target parameter name (default: script)")
    args = parser.parse_args()

    print(f"[*] Scanning {args.url} with payloads from {args.wordlist} using parameter '{args.param}'\n")
    scan(args.url, args.wordlist, args.param)

if __name__ == "__main__":
    main()
