import requests
from bs4 import BeautifulSoup
import socket
import whois

def analyze_domain(domain):
    try:
        # Ensure the URL has a scheme for web scraping and HTTP headers
        if not domain.startswith(("http://", "https://")):
            url = f"http://{domain}"
        else:
            url = domain

        print(f"Analyzing Domain: {domain}")
        print("=" * 50)

        # Step 1: Basic DNS Resolution
        print("\n### DNS Resolution ###")
        try:
            ip = socket.gethostbyname(domain)
            print(f"IP Address: {ip}")
        except socket.gaierror:
            print("Could not resolve domain")

        # Step 2: WHOIS Lookup
        print("\n### WHOIS Data ###")
        try:
            domain_info = whois.whois(domain)
            print(f"Domain Name: {domain_info.domain_name}")
            print(f"Registrar: {domain_info.registrar}")
            print(f"Creation Date: {domain_info.creation_date}")
            print(f"Expiration Date: {domain_info.expiration_date}")
        except Exception as e:
            print(f"Error fetching WHOIS data: {e}")

        # Step 3: HTTP Headers
        print("\n### HTTP Headers ###")
        try:
            response = requests.head(url, timeout=5)
            for key, value in response.headers.items():
                print(f"{key}: {value}")
        except requests.RequestException as e:
            print(f"Error fetching HTTP headers: {e}")

        # Step 4: Web Scraping
        print("\n### Web Scraping ###")
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract title
            title = soup.title.string if soup.title else "No Title"
            print(f"Title: {title}")

            # Extract meta description
            meta_description = soup.find("meta", {"name": "description"})
            meta_description = meta_description['content'] if meta_description else "No Description"
            print(f"Meta Description: {meta_description}")

            # Extract links
            print("\nLinks found on the page:")
            links = [a['href'] for a in soup.find_all('a', href=True)]
            for link in links:
                print(link)
        except requests.RequestException as e:
            print(f"Error scraping the web page: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    domain_to_analyze = input("Enter the domain or URL to analyze: ").strip()
    analyze_domain(domain_to_analyze)
