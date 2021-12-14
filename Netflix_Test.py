from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

load_dotenv()

Username = os.getenv('NF_USER')
Password = os.getenv('NF_PASSWORD')

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.netflix.com/")
print(driver.title)

# items = driver.find_element(By.CSS_SELECTOR, "#body-main > div > div")
# print(items.text)



time.sleep(5)

driver.quit()
