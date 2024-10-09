import requests
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com/in/'

# Fetch the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links
links = soup.find_all('a', href=True)

# Check the status of each link
for link in links:
    link_url = link['href']
    try:
        link_response = requests.get(link_url)
        if link_response.status_code == 404:
            print(f'Broken link: {link_url}')
        else:
            print(f'Working link: {link_url}')
    except requests.exceptions.RequestException as e:
        print(f'Error accessing {link_url}: {e}')
        
print('Link verification complete.')
