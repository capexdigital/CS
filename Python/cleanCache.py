import time
import os
import warnings
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from requests.exceptions import RequestsDependencyWarning


load_dotenv()
PASSWORD = os.getenv("PASSWORD")

warnings.simplefilter('ignore', RequestsDependencyWarning)

USERNAME = "admin"
PASSWORD = {PASSWORD}

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("https://portaldaeconomia.com/wp-login.php")
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="user_login"]').send_keys(USERNAME)
    driver.find_element(By.XPATH, '//*[@id="user_pass"]').send_keys(PASSWORD)
    driver.find_element(By.ID, "wp-submit").click()
    time.sleep(1)

    menu = driver.find_element(By.XPATH, '//*[@id="wp-admin-bar-autoptimize"]/a/span[2]')
    ActionChains(driver).move_to_element(menu).perform()
    time.sleep(1)

    item = driver.find_element(By.XPATH, '//*[@id="wp-admin-bar-autoptimize-delete-cache"]/div')
    item.click()
    time.sleep(1)

finally:
    driver.quit()
    