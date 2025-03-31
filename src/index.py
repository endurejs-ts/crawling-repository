import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib.parse

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
main = WebDriverWait(driver, 10)

# //*[@id="anchorBoxId_1665"]/a //*[@id="anchorBoxId_2032"]/a
# itemList = driver.find_element(By.XPATH, '//*[@id="contents"]/div[3]/div/ul/li/div')
# allUL = itemList.find_elements(By.TAG_NAME, 'ul')
# # //*[@id="anchorBoxId_1665"]/a #anchorBoxId_1665 > a
# # #anchorBoxId_2032 > a
# all_A = allUL[1].find_elements(By.XPATH, '//*[starts-with(@id, "anchorBoxId")]/a')
# result_a1 = []
# for aa in all_A:
#     result_a1.append(urllib.parse.unquote(aa.get_attribute("href")))

# with open("../dist/admin/head/href.json", "w", encoding="utf-8") as f:
#     json.dump(result_a1, f, ensure_ascii=False)

# driver.get("https://www.kakamuka.com/product/list.html?cate_no=122")
# content_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[5]')

def getLink(end_num: int, cate_num: int, fp: str):
    for i in range(1, end_num):
        result_a2 = []
        driver.get(f"https://www.kakamuka.com/product/list.html?cate_no={cate_num}&page={i}")
        main.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]/div[5]')))
        content_box = driver.find_element(By.XPATH, '//*[@id="contents"]/div[5]')
        ul = content_box.find_element(By.XPATH, '//*[@id="contents"]/div[5]/div[2]/ul')

        all_a = ul.find_elements(By.XPATH, '//*[starts-with(@id, "anchorBoxId")]/div[1]/a')
        for aa in all_a:
            result_a2.append(urllib.parse.unquote(aa.get_attribute("href")))

        result_a2 = result_a2[7:]

        with open(f"{fp}/bottom/href/href{i}.json", "w", encoding="utf-8") as f:
            json.dump(result_a2, f, ensure_ascii=False)

getLink(6, 48, "../dist/noadmin/48")
driver.quit()