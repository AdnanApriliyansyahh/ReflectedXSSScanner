#!/usr/bin/env python3
import argparse
import requests
import urllib3

# Matikan warning SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scan(url, wordlist, param, output):
    with open(wordlist, "r") as f:
        payloads = [line.strip() for line in f if line.strip()]

    with open(output, "w") as log:
        for payload in payloads:
            try:
                params = {param: payload}
                r = requests.get(url, params=params, timeout=10, verify=False)

                if payload in r.text:
                    print(f"[!] Reflected: {payload}")
                    log.write(f"[!] Reflected payload: {payload}\n")
                    log.write(f"    URL: {r.url}\n\n")

            except Exception as e:
                print(f"[!] Error testing payload {payload}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Reflected XSS scanner PoC")
    parser.add_argument("-u", "--url", required=True, help="Target URL, e.g. http://site.com/page")
    parser.add_argument("-w", "--wordlist", required=True, help="Wordlist file with payloads")
    parser.add_argument("-p", "--param", default="q", help="Target parameter name (default: q)")
    parser.add_argument("-o", "--output", default="reflected.log", help="Output log file")
    args = parser.parse_args()

    print(f"[*] Scanning {args.url} with payloads from {args.wordlist} using parameter '{args.param}'\n")
    scan(args.url, args.wordlist, args.param, args.output)
    print(f"\n[✓] Finished. Results saved in {args.output}")

if __name__ == "__main__":
    main()
