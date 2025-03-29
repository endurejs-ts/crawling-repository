from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv
import urllib.parse
import json
load_dotenv()

ID = os.getenv("ID")
PWD = os.getenv("PWD")

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.kakamuka.com")
sleep(1)

main = WebDriverWait(driver, 10)
main.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="JS_topMenu"]/li[1]/a[1]')))
login_button = driver.find_element(By.XPATH, '//*[@id="JS_topMenu"]/li[1]/a[1]')
login_button.click()
sleep(2)

main.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]')))

input1 = driver.find_element(By.XPATH, '//*[@id="member_id"]')
input1.send_keys(ID)
sleep(1.3)

input2 = driver.find_element(By.XPATH, '//*[@id="member_passwd"]')
input2.send_keys(PWD)
sleep(2)

login_button_form = driver.find_element(By.XPATH, '//form[starts-with(@id, "member_form_")]/div/div/fieldset/a')
login_button_form.click()

sleep(3)

driver.get("https://www.kakamuka.com/product/list.html?cate_no=122")
main.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[5]')))
sleep(1)

main_c = driver.find_element(By.XPATH, '//*[@id="contents"]/div[5]')
uls = main_c.find_element(By.XPATH, '//*[@id="contents"]/div[5]/div[2]/ul')
allOfLis = uls.find_elements(By.TAG_NAME, 'li')

hrefsa = []
for aol in allOfLis:
    a = aol.find_element(By.XPATH, '//*[starts-with(@id, "anchorBoxId")]/div[1]/a') # /html/body/div[4]/div/div[2]/div[5]/div[2]/ul/li[2]/div[1]/a
    hrefsa.append(a.get_attribute("href"))

href_result = [urllib.parse.unquote(h) for h in hrefsa]

with open("../../dist/href2.json", "w", encoding="utf-8") as f:
    json.dump(href_result, f, ensure_ascii=False)