from bs4 import BeautifulSoup
import json

itema = []
for i in range(1, 14):
    with open(f"../dist/html/en{i}.html", "r", encoding="utf-8") as f:
        content = f.read()
        soup = BeautifulSoup(content, "html5lib")

        main_content = soup.select_one("#contents")
        inner_div = main_content.select_one("div.xans-element-.xans-product.xans-product-listrecommend")
        ul_img = inner_div.select_one("div > ul")
        item_list = ul_img.select_one("li > div")
        ull_all = item_list.find_all("ul")
        one_li = ull_all[0].select_one("li")
        inner_a = one_li.select_one("a")
        itema.append(f'{"https://www.kakamuka.com"}{inner_a.get("href")}')

        with open("../dist/itema.json", "w", encoding="utf-8") as f:
            json.dump(itema, f, ensure_ascii=False)