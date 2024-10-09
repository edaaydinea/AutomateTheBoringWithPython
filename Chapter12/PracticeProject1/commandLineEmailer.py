import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Parse arguments
email_address = sys.argv[1]
message = sys.argv[2]

# Set up Selenium
driver = webdriver.Chrome()
driver.get('https://mail.google.com/')

# Log in to Gmail (you may need to handle the login process or use an API like OAuth for a better approach)
email_input = driver.find_element_by_id('identifierId')
email_input.send_keys('your_email@gmail.com')
email_input.send_keys(Keys.ENTER)

# Add delays as necessary for loading time
time.sleep(3)

# Enter password
password_input = driver.find_element_by_name('password')
password_input.send_keys('your_password')  # use environment variables for security
password_input.send_keys(Keys.ENTER)

# Wait for login and load
time.sleep(10)

# Click Compose button
compose_button = driver.find_element_by_xpath('//div[contains(text(),"Compose")]')
compose_button.click()

time.sleep(2)

# Fill in the recipient's email address
to_input = driver.find_element_by_name('to')
to_input.send_keys(email_address)

# Fill in the subject (optional)
subject_input = driver.find_element_by_name('subjectbox')
subject_input.send_keys('Automated Email')

# Fill in the message
body_input = driver.find_element_by_xpath('//div[@aria-label="Message Body"]')
body_input.send_keys(message)

# Send the email
send_button = driver.find_element_by_xpath('//div[contains(text(),"Send")]')
send_button.click()

print("Email sent successfully.")
driver.quit()
