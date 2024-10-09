import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

search_query = "cats"
output_folder = "downloaded_images"

# Set up Selenium (make sure you have the correct driver for your browser)
driver = webdriver.Chrome()
driver.get('https://imgur.com/')

try:
    # Wait for the search box to be present
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search images, tags, and users"]'))
    )
    
    # Search for the category of images
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.ENTER)

    time.sleep(3)  # Allow time for images to load

    # Find all image elements
    images = driver.find_elements(By.TAG_NAME, 'img')

    # Download images
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for index, image in enumerate(images):
        src = image.get_attribute('src')
        if src and 'http' in src:  # Ensure src is a valid URL
            img_data = requests.get(src).content
            with open(f'{output_folder}/image_{index}.jpg', 'wb') as f:
                f.write(img_data)

    print("Download complete.")

finally:
    driver.quit()
