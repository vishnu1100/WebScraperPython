# Domain and Web Page Analyzer

This script gathers detailed technical information about a domain or URL. It performs the following tasks:
- DNS resolution to find the IP address.
- WHOIS lookup to retrieve registration and ownership details.
- HTTP headers retrieval to analyze server details.
- Web scraping to extract metadata, links, and content from the webpage.

## Features

1. **DNS Resolution**:
   - Retrieves the IP address of the domain.

2. **WHOIS Lookup**:
   - Provides information like registrar, domain creation, and expiration dates.

3. **HTTP Headers Retrieval**:
   - Analyzes HTTP response headers to extract server and content details.

4. **Web Scraping**:
   - Extracts page title, meta description, and hyperlinks from the webpage.

## Requirements

Install the following Python libraries before running the script:

```bash

pip install requests beautifulsoup4 python-whois



Analyzing Domain: xxxxx.xxx
==================================================

### DNS Resolution ###
IP Address: xxx.xxx.xxx

### WHOIS Data ###
Domain Name: EXAMPLE.COM
Registrar: INTERNET ASSIGNED NUMBERS AUTHORITY
Creation Date: 1995-08-14 00:00:00
Expiration Date: 2024-08-14 00:00:00

### HTTP Headers ###
Content-Type: text/html; charset=UTF-8
Content-Length: 1256
Server: ECS (nyb/1D08)

### Web Scraping ###
Title: Example Domain
Meta Description: No Description

Links found on the page:
http://www.iana.org/domains/example






Feel free to copy this directly into a `README.md` file for your GitHub repository. Let me know if you need further adjustments!
