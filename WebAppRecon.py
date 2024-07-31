import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Web Reconnaissance Tool")
    parser.add_argument("-d", "--domain", help="Specify the domain name", required=True)
    parser.add_argument("-a", "--all", help="Run all scripts", action="store_true")
    parser.add_argument("-dir", help="Run directory enumeration script", action="store_true")
    parser.add_argument("-dns", help="Run DNS enumeration script", action="store_true")
    parser.add_argument("-file", help="Run file enumeration script", action="store_true")
    parser.add_argument("-sub", help="Run subdomain discovery script", action="store_true")
    args = parser.parse_args()

    if args.all:
        run_all(args.domain)
    elif args.dir:
        run_script("dir_enum.py", args.domain)
    elif args.dns:
        run_script("dns_enum.py", args.domain)
    elif args.file:
        run_script("file_enum.py", args.domain)
    elif args.sub:
        run_script("subdomain_discovery.py", args.domain)
    else:
        print("Please select an option or use --help for more information.")

def run_script(script_name, domain):
    subprocess.run(["python", script_name, "-d", domain])

def run_all(domain):
    scripts = ["dir_enum.py", "dns_enum.py", "file_enum.py", "subdomain_discovery.py"]
    for script in scripts:
        run_script(script, domain)

if __name__ == "__main__":
    main()
