import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
import os
from selenium.common.exceptions import NoSuchElementException

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

sleep(2)

def getOpLink(end_num, fp):
    for v in range(1, end_num):
        with open(f"{fp}/href/href{v}.json", "r", encoding="utf-8") as f:
            content = json.load(f)

        head_result = []
        for ctt in content:
            driver.get(ctt)
            main.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]')))
            sleep(0.5)

            img_link = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[1]/div[1]/div[1]/a/img').get_attribute("src")
            title = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[3]/div[2]/h2').text
            price = driver.find_element(By.XPATH, '//*[@id="span_product_price_text"]').text.replace("원", "")
            category_code = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/ol').text
            ctg_result = " > ".join(category_code.split("\n"))

            try:
                img_link_2 = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[1]/div[2]/ul/li[2]/img').get_attribute("src")
            except NoSuchElementException:
                img_link_2 = ""

            try:
                img_link_3 = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[1]/div[2]/ul/li[3]/img').get_attribute("src")
            except NoSuchElementException:
                img_link_3 = ""

            head_result.append({
                "modelName": ctt,
                "name": title,
                "categoryCode": ctg_result,
                "price": price,
                "img1Url": img_link,
                "img2Url": img_link_2,
                "img3Url": img_link_3
            })

        with open(f"{fp}/data/data{v}.json", "w", encoding="utf-8") as f2:
            json.dump(head_result, f2, ensure_ascii=False, indent=4)

getOpLink(6, "../dist/noadmin/48/bottom")
driver.quit()