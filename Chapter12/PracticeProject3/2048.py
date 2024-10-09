from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up Selenium
driver = webdriver.Chrome()
driver.get('https://gabrielecirulli.github.io/2048/')

game = driver.find_element_by_tag_name('body')

# Simulate arrow keys to play
for i in range(1000):  # Change the number of iterations as needed
    game.send_keys(Keys.UP)
    game.send_keys(Keys.RIGHT)
    game.send_keys(Keys.DOWN)
    game.send_keys(Keys.LEFT)
    time.sleep(0.1)  # Slow down the loop for more natural play

print("Game played.")
driver.quit()
