import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import webbrowser

# Ensure search term is passed
if len(sys.argv) < 2:
    print('Usage: python amazon.py <product name>')
    sys.exit()

search_term = ' '.join(sys.argv[1:])

# Set up the Selenium Chrome WebDriver
print('Opening browser...')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to Amazon and search for the product
amazon_search_url = f"https://www.amazon.com/s?k={search_term}"
driver.get(amazon_search_url)

time.sleep(3)  # Wait for the page to load

# Retrieve top search result links
print('Fetching product links...')
product_links = driver.find_elements(By.CSS_SELECTOR, ".a-link-normal.a-text-normal")

# Open a browser tab for each result (limit to 5)
num_open = min(5, len(product_links))
for i in range(num_open):
    product_url = product_links[i].get_attribute('href')
    print(f'Opening {product_url}')
    webbrowser.open_new_tab(product_url)

# Close the Selenium browser after fetching the links
driver.quit()
