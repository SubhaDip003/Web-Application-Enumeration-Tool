import os
import requests
import argparse
import time
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def get_wordlist():
    """Read the wordlist from the local machine"""
    with open('wordlist.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]

def directory_enumeration(domain, word):
    """Perform directory enumeration"""
    url = f"http://{domain}/{word}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return url
    except requests.exceptions.RequestException:
        pass

def list_directories(domain, wordlist):
    """Perform directory listing or enumeration of a given domain name of a web application."""
    discovered_directories = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        for url in tqdm(executor.map(lambda word: directory_enumeration(domain, word), wordlist), desc=f"Enumerating directories for {domain}"):
            if url:
                discovered_directories.append(url)
    return discovered_directories

def save_results(discovered_directories, domain):
    """Save the results to a file in the results directory."""
    results_dir = "results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    filename = f"{results_dir}/{domain}_directories.txt"
    with open(filename, 'w') as f:
        for directory in discovered_directories:
            f.write(f"{directory}\n")
    print(f"Results saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Directory listing or enumeration tool")
    parser.add_argument("-d", "--domain", required=True, help="Domain name of the web application")
    args = parser.parse_args()
    domain = args.domain

    wordlist = get_wordlist()
    discovered_directories = list_directories(domain, wordlist)
    save_results(discovered_directories, domain)

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

