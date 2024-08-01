import os
import argparse
import requests
from tqdm import tqdm
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []

    for link in soup.find_all('a', href=True):
        href = link['href']
        links.append(urljoin(url, href))

    return links

def download_file(url, directory):
    response = requests.get(url, stream=True)
    filename = os.path.join(directory, os.path.basename(urlparse(url).path))

    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    return filename

def find_backup_files(url):
    result_dir = "results"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    links = extract_links(url)
    backup_files = []

    # Add more extensions here
    backup_extensions = ['.zip', '.tar', '.bak', '.dump', '.sql', '.tgz', '.tar.gz', '.txt', '.xml', '.php']

    for link in tqdm(links, desc="Searching for backup files", unit="file"):
        filename = os.path.basename(urlparse(link).path)
        if any(filename.endswith(ext) for ext in backup_extensions):
            backup_files.append(link)

    return backup_files

def main():
    parser = argparse.ArgumentParser(description="Find backup files on a website")
    parser.add_argument("-d", "--url", type=str, help="Website URL", required=True)
    args = parser.parse_args()

    url = args.url
    if not url.startswith("http"):
        url = "http://" + url

    backup_files = find_backup_files(url)
    print("Backup files found:", backup_files)

    # Save the output to a text file
    result_dir = "results"
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    with open(os.path.join(result_dir, "backup_files.txt"), 'w') as f:
        for item in backup_files:
            f.write("%s\n" % item)

    print("Results saved to results/backup_files.txt")

if __name__ == "__main__":
    main()
