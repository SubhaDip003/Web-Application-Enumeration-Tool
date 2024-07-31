# WebRecon - Web Enumeration Tool

## Description:

WebRecon is a comprehensive web enumeration tool to analyze websites and web applications, facilitating the discovery of crucial information. This tool will focus on sub-domain identification, directory listing, file enumeration, DNS enumeration. By providing insights into the website's structure, vulnerabilities, and potential attack vectors. Basically, this tool is used for Web Reconnaissance for security assessment.

## Objective:

It is a Python-based web enumeration tool named WebRecon. The main objective is to develop a comprehensive web enumeration tool to analyze websites and web applications, facilitating the discovery of crucial information such as sub-domain identification, directory listing, file enumeration, and DNS enumeration. This tool aims to provide insights into the website's structure, vulnerabilities, and potential attack vectors, making it essential for web reconnaissance in security assessments.

## Features:

- **Directory Enumeration**: Scans for directories on the target web application.
- **DNS Enumeration**: Discovers DNS records for the target domain.
- **File Enumeration**: Identifies files available on the target web server.
- **Subdomain Discovery**: Detects subdomains associated with the target domain.
- **Command-Line Interface**: User-friendly CLI for specifying the domain and selecting tasks.

# How to Use:

## Installation

Clone the repository and navigate to the project directory and create a directory called `results` for store the results:
```
 git clone https://github.com/SubhaDip003/WebRecon.git

 cd WebRecon

 mkdir results
```

Install the required Python packages:
```
pip install -r requirements.txt
```

### NOTE: If you have any error to install the requirement packages in kali Linux or parrotOS (Debian-based Linux) then at first you create a Virtual Environment. Follow the commands to create Virtual Environment and install all dependencies:
```
# Create a virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install packages using pip
pip install -r requirements.txt

# Exit from the virtual environment
deactivate
```

## To get help

Run the command:
```
python3 WebAppRecon.py -h
```

## Running the Tool

Execute the `WebRecon.py` script via the command-line interface. You need to provide the domain name of the target website using the `-d` or `--domain` switch. Here are the available options:
```
python3 WebRecon.py -d <domain> [options]
```

### Options:

* `-d`, `--domain`: Specify the domain name (required).
* `-a`, `--all`: Run all scripts.
* `-dir`: Run directory enumeration script.
* `-dns`: Run DNS enumeration script.
* `-file`: Run file enumeration script.
* `-sub`: Run subdomain discovery script.

# Examples:

## To Run All Scripts:
```
python3 WebRecon.py -a -d example.com
```

## To Run Directory Enumeration:
```
python3 WebRecon.py -dir -d example.com
```

## To Run DNS Enumeration:
```
python3 WebRecon.py -dns -d example.com
```

## To Run File Enumeration:
```
python3 WebRecon.py -file -d example.com
```

## To Run Subdomain Discovery:
```
python3 WebRecon.py -sub -d example.com
```
