from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

load_dotenv()

NF_Username = os.getenv('NF_USERNAME')
NF_Password = os.getenv('NF_PASSWORD')
NF_Profile= os.getenv('NF_Profile')

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.netflix.com/login")


#Login
driver.find_element(By.CSS_SELECTOR, "#id_userLoginId").send_keys(NF_Username)
driver.find_element(By.CSS_SELECTOR, "#id_password").send_keys(NF_Password)
driver.find_element(By.CSS_SELECTOR, "#appMountPoint > div > div.login-body > div > div > div.hybrid-login-form-main > form > button").send_keys(Keys.ENTER)
time.sleep(5)

#Select Profile
driver.find_element(By.LINK_TEXT, NF_Profile).click()
time.sleep(5)

# driver.quit()
