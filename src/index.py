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
hrefs = []
for idx, i in enumerate(url, start=1):
    driver.get(i)
    main.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]')))
    sleep(1)
    esangho_crack = driver.find_element(By.XPATH, '//*[@id="contents"]')

    ani = esangho_crack.find_element(By.CSS_SELECTOR, 'div.xans-element-.xans-product.xans-product-listrecommend')
    zinzza = ani.find_element(By.CSS_SELECTOR, 'div > ul')
    zonna = zinzza.find_element(By.CSS_SELECTOR, 'li > div')
    ul_all = zonna.find_elements(By.TAG_NAME, "ul")
    one_li = ul_all[0].find_element(By.TAG_NAME, "li")
    best_pro = one_li.find_element(By.TAG_NAME, "a")

    href = best_pro.get_attribute("href")
    hrefs.append(href)

hrefs.pop(8)
result = []
for h in hrefs:
    driver.get(h)
    main.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]')))
    sleep(1)

    main_content = driver.find_element(By.XPATH, '//*[@id="contents"]')
    content_box = main_content.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[3]/div[2]')
        
    title = content_box.find_element(By.TAG_NAME, "h2")

    div_box = content_box.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[3]/div[2]/div[2]')
    table = div_box.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/table/tbody')

    price = table.find_element(By.XPATH, '//*[@id="span_product_price_text"]')
    origin_price = table.find_element(By.XPATH, '//*[@id="span_product_price_custom"]')
    amout_per_box = origin_price.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/table/tbody/tr[4]/td/span')
    expire_date = table.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/table/tbody/tr[5]/td/span')
    bacode = table.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/span')
    result.append({
        "title": title.text,
        "price": price.text,
        "origin": origin_price.text,
        "abpbox": amout_per_box.text,
        "expire": expire_date.text,
        "bdc": bacode.text,
    })

with open("../dist/resulta.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

driver.quit()