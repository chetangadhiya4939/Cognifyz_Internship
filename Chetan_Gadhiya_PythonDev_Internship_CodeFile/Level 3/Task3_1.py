import requests
from bs4 import BeautifulSoup
# I have not used proxies here.
# one must use proxies for the more data scraping and to prevent from blocking of IP.
def scrape_links(url):
    try:
        
        response = requests.get(url)
        response.raise_for_status()  # HTTPError for bad responses
        
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all anchor tags
        links = soup.find_all('a')
        
        
        print(f"Links found on {url}:")
        for link in links:
            href = link.get('href')
            if href:
                print(href)
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


url = input("Enter the URL of the website to scrape (e.g., https://example.com): ")
scrape_links(url)
