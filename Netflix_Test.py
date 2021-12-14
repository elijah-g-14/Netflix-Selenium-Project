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
showArr = ["Criminal Minds", "Legends of Korra"]
play_next = False

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
time.sleep(3)

#Select Profile
driver.find_element(By.LINK_TEXT, NF_Profile).click()
time.sleep(3)

#Select and Play Titles
driver.find_element(By.LINK_TEXT, showArr[0]).click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "#appMountPoint > div > div > div:nth-child(1) > div.focus-trap-wrapper.previewModal--wrapper.detail-modal.has-smaller-buttons > div > div.previewModal--player_container.detail-modal.has-smaller-buttons > div:nth-child(4) > div > div.previewModal--player-titleTreatment-left.previewModal--player-titleTreatment.detail-modal.has-smaller-buttons.detail-modal.has-smaller-buttons > div.buttonControls--container > a > button").click()

time.sleep(900)

while play_next == False: 
    if driver.find_element(By.CSS_SELECTOR, "#appMountPoint > div > div > div.watch-video > div > div > div.nfa-pos-abs.nfa-top-0.nfa-left-0.nfa-right-0.nfa-bot-0.nfa-d-flex.nfa-ai-flex-end.nfa-jc-flex-end.SeamlessControls--container.SeamlessControls--container-visible > div.nfa-pos-abs.nfa-bot-6-em.nfa-right-5-em.nfa-d-flex > button.color-primary.hasLabel.hasIcon.ltr-v8pdkb").is_displayed():
        driver.find_element(By.CSS_SELECTOR, "#appMountPoint > div > div > div.watch-video > div > div > div.nfa-pos-abs.nfa-top-0.nfa-left-0.nfa-right-0.nfa-bot-0.nfa-d-flex.nfa-ai-flex-end.nfa-jc-flex-end.SeamlessControls--container.SeamlessControls--container-visible > div.nfa-pos-abs.nfa-bot-6-em.nfa-right-5-em.nfa-d-flex > button.color-primary.hasLabel.hasIcon.ltr-v8pdkb").click()
        play_next = True
    else:
        time.sleep(30)
        continue


print(play_next)



# driver.quit()
