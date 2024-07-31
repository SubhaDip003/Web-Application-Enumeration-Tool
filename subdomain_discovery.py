import requests
import concurrent.futures
import time
import threading

class TokenBucket:
    def __init__(self, rate, capacity):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.lock = threading.Lock()
        self.last_fill = time.monotonic()

    def get_token(self):
        with self.lock:
            current_time = time.monotonic()
            elapsed = current_time - self.last_fill
            self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
            self.last_fill = current_time

            if self.tokens >= 1:
                self.tokens -= 1
                return True
            else:
                return False

def check_subdomain(subdomain, verbose):
    if verbose:
        print(f"Checking {subdomain}...")
    try:
        response = requests.get(f"http://{subdomain}", timeout=3)
        if response.status_code in [200, 301, 302]:
            if verbose:
                print(f"Found: {subdomain} (Status code: {response.status_code})")
            return subdomain
    except requests.RequestException:
        pass
    return None

def fuzz_subdomains(domain, wordlist_file, results_file, rate, capacity, verbose=True, max_workers=10):
    token_bucket = TokenBucket(rate, capacity)
    subdomains = []

    with open(wordlist_file, 'r') as file:
        words = file.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for word in words:
            while not token_bucket.get_token():
                time.sleep(0.1)  # Wait for a token to become available
            futures.append(executor.submit(check_subdomain, f"{word}.{domain}", verbose))

        with open(results_file, 'a') as f:
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    f.write(result + "\n")
                    f.flush()

if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) < 2 or '-d' not in sys.argv:
        print("Usage: python subdomain_enumeration.py -d <domain>")
        sys.exit(1)

    domain = sys.argv[sys.argv.index("-d") + 1]
    wordlist_file = "wordlist2.txt"
    results_file = "results/subdomains.txt"

    # Token bucket parameters
    rate = 1  # Tokens added per second
    capacity = 5  # Maximum number of tokens

    if not os.path.exists(wordlist_file):
        print(f"Wordlist file '{wordlist_file}' not found.")
        sys.exit(1)

    os.makedirs("results", exist_ok=True)
    fuzz_subdomains(domain, wordlist_file, results_file, rate, capacity)

    print(f"Subdomains of {domain} have been saved to {results_file}")
