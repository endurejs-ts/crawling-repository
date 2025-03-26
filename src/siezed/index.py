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

main.until(EC.presence_of_element_located((By.XPATH, '//*[@id="category-lnb"]')))

target_element = driver.find_element(By.XPATH, '//*[@id="category-lnb"]')
category_list = target_element.text.split("\n")

target_elementul = driver.find_element(By.XPATH, '//*[@id="category-lnb"]/div[1]/ul')
all_of_li = target_elementul.find_elements(By.TAG_NAME, "li")

url = []
for aol in all_of_li:
    link = aol.find_element(By.TAG_NAME, "a")
    url.append(link.get_attribute("href"))

url.pop(8)
url.pop(8+1)

datas = []
nokia = []
for idx, i in enumerate(url, start=1):
    driver.get(i)
    main.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]')))
    sleep(1)

    title = driver.find_element(By.XPATH, '//*[starts-with(@id, "anchorBoxId")]/a/div/p') # //*[@id="anchorBoxId_1712"]/a/div/p/text()
    origin = driver.find_element(By.XPATH, '//*[starts-with(@id, "anchorBoxId")]/a/div/ul/li[1]/span')
    price = driver.find_element(By.XPATH, '//*[starts-with(@id, "anchorBoxId")]/a/div/ul/li[2]/span[1]')
    bacode = driver.find_element(By.XPATH, '//*[starts-with(@id, "anchorBoxId")]/a/div/ul/li[3]/span') # //*[@id="anchorBoxId_10541"]/a/div/p/text() //*[@id="anchorBoxId_10541"]/a/div/p/span //*[@id="anchorBoxId_10541"]/a/div/p
    
    secondary_box_p = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div/ul/li/div/ul[2]/li[1]/a/div/p') # /html/body/div[4]/div/div[2]/div[3]/div/ul/li/div/ul[2]/li[1]/a/div/p
    secondary_box_origin = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div/ul/li/div/ul[2]/li[1]/a/div/ul/li[1]/span')
    secondary_box_price = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div/ul/li/div/ul[2]/li[1]/a/div/ul/li[2]/span[1]')
    secondary_box_bacode = driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div/ul/li/div/ul[2]/li[1]/a/div/ul/li[3]/span')

    datas.append({
        "title": title.text, "origin": origin.text, "price": price.text, "bacode": bacode.text
    })

    nokia.append({
        "title": secondary_box_p.text, "origin": secondary_box_origin.text, "price": secondary_box_price.text, "bacode": secondary_box_bacode.text
    })

print(len(datas))

with open("../../dist/nokia.json", "w", encoding="utf-8") as f:
    json.dump(nokia, f, ensure_ascii=False, indent=4)

driver.quit()