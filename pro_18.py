import requests
from bs4 import BeautifulSoup
import json

url = "https://books.toscrape.com/catalogue/page-1.html"

all_books = []

while len(all_books) < 70:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text

        all_books.append({"title": title, "price": price})

    # next page
    next_btn = soup.find("li", class_="next")
    if next_btn:
        next_page = next_btn.a["href"]
        url = "https://books.toscrape.com/catalogue/" + next_page
    else:
        break

# sirf 70 books
all_books = all_books[:70]

# JSON file me save
with open("books.json", "w") as file:
    json.dump(all_books, file, indent=4)

print("Data JSON file me save ho gaya ✅")