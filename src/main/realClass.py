from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import json

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.kakamuka.com")
sleep(1)
main = WebDriverWait(driver, 10)

for i in range(1, 30):
    with open(f"../../dist/href{i}.json", "r", encoding="utf-8") as f:
        content = json.load(f)

    result_d = []
    for ctt in content:
        driver.get(ctt)
        main.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]')))
        sleep(1)

        cotBox = driver.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[3]')
        title = cotBox.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[3]/div[2]/h2')
        category_code = driver.find_element(By.XPATH, '//*[@id="contents"]/div[1]/ol')
        price = cotBox.find_element(By.XPATH, '//*[@id="span_product_price_text"]')
        amount_per_box = cotBox.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/table/tbody/tr[4]/td/span')
        expire_date = cotBox.find_element(By.XPATH, '//*[@id="contents"]/div[2]/div[2]/div[3]/div[2]/div[3]/div[1]/table/tbody/tr[5]/td/span')
        formatted_text = " > ".join(category_code.text.split("\n"))
        result_d.append({
            "link": ctt,
            "title": title.text,
            "location": formatted_text,
            "price": price.text,
            "amount_per_box": amount_per_box.text,
            "expire_date": expire_date.text
        })

        with open(f"../../finished/data{i}.json", "w", encoding="utf-8") as f:
            json.dump(result_d, f, ensure_ascii=False, indent=4)

driver.quit()