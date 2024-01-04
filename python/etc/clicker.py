from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# List of websites you want to open
website = "https://www.nakarmpsa.olx.pl"

# Create a new instance of the Chrome driver with incognito mode
options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)

# Function to perform an action on the website
def perform_action(driver):
    
    pass

# Open each website, perform action, close tab and repeat
for x in range(0, 100):
    driver.get(website)
    perform_action(driver)
    time.sleep(2)  # Wait for 2 seconds
    driver.close()

# Quit the driver
driver.quit()
