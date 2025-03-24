from bs4 import BeautifulSoup

for i in range(1, 14):
    with open(f"../dist/html/en{i}.html", "r", encoding="utf-8") as f:
        content = f.read()
        soup = BeautifulSoup(content, "html5lib")

        