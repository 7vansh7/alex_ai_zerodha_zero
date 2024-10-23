import requests
from bs4 import BeautifulSoup

# List of URLs to visit
urls = [
    "https://support.zerodha.com/category/account-opening",
    "https://support.zerodha.com/category/account-opening/getting-started",
    "https://support.zerodha.com/category/account-opening/online-account-opening",
    "https://support.zerodha.com/category/account-opening/offline-account-opening",
    "https://support.zerodha.com/category/account-opening/charges-at-zerodha",
    "https://support.zerodha.com/category/account-opening/company-partnership-and-huf-account-opening",
    "https://support.zerodha.com/category/account-opening/nri-account-opening",
    "https://support.zerodha.com/category/your-zerodha-account",
    "https://support.zerodha.com/category/your-zerodha-account/login-credentials",
    "https://support.zerodha.com/category/your-zerodha-account/your-profile",
    "https://support.zerodha.com/category/your-zerodha-account/account-modification-and-segment-addition",
    "https://support.zerodha.com/category/your-zerodha-account/dp-id-and-bank-details",
    "https://support.zerodha.com/category/your-zerodha-account/nomination-process",
    "https://support.zerodha.com/category/your-zerodha-account/transfer-of-shares-and-conversion-of-shares",
    "https://support.zerodha.com/category/trading-and-markets",
    "https://support.zerodha.com/category/trading-and-markets/trading-faqs",
    "https://support.zerodha.com/category/trading-and-markets/kite-web-and-mobile",
    "https://support.zerodha.com/category/trading-and-markets/margins",
    "https://support.zerodha.com/category/trading-and-markets/product-and-order-types",
    "https://support.zerodha.com/category/trading-and-markets/corporate-actions",
    "https://support.zerodha.com/category/trading-and-markets/kite-features",
    "https://support.zerodha.com/category/funds",
    "https://support.zerodha.com/category/funds/fund-withdrawal",
    "https://support.zerodha.com/category/funds/adding-funds",
    "https://support.zerodha.com/category/funds/adding-bank-accounts",
    "https://support.zerodha.com/category/funds/mandate",
    "https://support.zerodha.com/category/console",
    "https://support.zerodha.com/category/console/ipo",
    "https://support.zerodha.com/category/console/portfolio",
    "https://support.zerodha.com/category/console/ledger",
    "https://support.zerodha.com/category/console/profile",
    "https://support.zerodha.com/category/console/reports",
    "https://support.zerodha.com/category/console/referral-program",
    "https://support.zerodha.com/category/mutual-funds",
    "https://support.zerodha.com/category/mutual-funds/understanding-mutual-funds",
    "https://support.zerodha.com/category/mutual-funds/coin-app",
    "https://support.zerodha.com/category/mutual-funds/coin-web",
    "https://support.zerodha.com/category/mutual-funds/transaction-and-reports",
    "https://support.zerodha.com/category/mutual-funds/nps"
]

# Function to extract all hrefs from a URL
def extract_hrefs(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad requests

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all href attributes from <a> tags
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        print(f"Failed to extract hrefs from {url}: {e}")
        return []

# File to save the results
output_file = "extracted_links.txt"

# Open file in write mode
with open(output_file, 'w') as file:
    # Iterate over all URLs
    for url in urls:
        file.write(f"Links from {url}:\n")
        links = extract_hrefs(url)
        
        # Write each link to the file
        for link in links:
            file.write(f"{link}\n")
        
        # Write a separator between different URL sections
        file.write("\n" + "="*50 + "\n\n")

print(f"All links have been saved to {output_file}")
