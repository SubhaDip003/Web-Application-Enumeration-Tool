import argparse
import os
import textwrap
import dns.resolver

def get_dns_info(domain):
    dns_info = {}
    for record_type in ['A', 'AAAA', 'MX', 'CNAME', 'SOA']:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            dns_info[record_type] = [str(a.to_text()) for a in answers]
        except dns.resolver.NoAnswer:
            dns_info[record_type] = []
    return dns_info

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            Query DNS information of a specific domain.
            The DNS information will be stored in txt format inside "results" directory.

            '''),
    )
    parser.add_argument('-d', '--domain', required=True, help='The domain to query.')
    args = parser.parse_args()
    os.makedirs('results', exist_ok=True)
    dns_info = get_dns_info(args.domain)
    with open(os.path.join('results', f'{args.domain}.txt'), 'w') as f:
        for record_type, records in dns_info.items():
            f.write(f'{record_type} Records:\n')
            for record in records:
                f.write(f'  {record}\n')
            f.write('\n')

if __name__ == '__main__':
    main()
