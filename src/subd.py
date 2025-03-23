from bs4 import BeautifulSoup
import json

with open("../dist/category.html", "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html5lib")
a_tags = soup.select("ul.nav.d1-wrap a")

href_list = [a["href"] for a in a_tags]
text_list = [a.get_text() for a in a_tags]

url = "https://www.kakamuka.com"
result = [{"name":name, "content": f'{url}{content}'} for name, content in zip(text_list, href_list)]

with open("../dist/infoofa.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)