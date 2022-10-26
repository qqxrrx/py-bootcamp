# https://quotes.toscrape.com
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter


BASE_URL = "https://quotes.toscrape.com"


def scrape_quotes():
    all_quotes = []
    url = "/page/1/"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        print(f"Now Scraping: {BASE_URL}{url}")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
            })

        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None

        # --- wait 2 seconds before next, to prevent overloading server or attracting attention ---
        # sleep(2)
    return all_quotes


def write_quotes(quotes):
    with open("quotes.csv", "w", encoding="utf-8") as f:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(f, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)


write_quotes(scrape_quotes())
