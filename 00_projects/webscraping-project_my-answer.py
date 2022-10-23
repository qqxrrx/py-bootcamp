# webscraping project (my answer)
# version: 1
import requests
from random import choice
from bs4 import BeautifulSoup
from csv import reader


# todo = scrape all quotes
# if next exists, go to that link and scrape again...


def retrieve_bs4data(url):
    return BeautifulSoup(requests.get(url).text, "html.parser")


main_url = "http://quotes.toscrape.com"

extracted_items = []

for item in retrieve_bs4data(main_url).find_all(class_="quote", attrs={"itemscope": ""}):
    author_field = item.find(class_="author", attrs={"itemprop": "author"})
    extracted_items.append({
        "quote": item.find(class_="text", attrs={"itemprop": "text"}).get_text(),
        "author": author_field.get_text(),
        "link": main_url + author_field.find_next_sibling()["href"]
    })


guess_attempt = 4

while guess_attempt >= 0:
    if guess_attempt == 4:
        quote_to_guess = choice(extracted_items)

        bs_ad = retrieve_bs4data(quote_to_guess['link'])
        date_author = bs_ad.find(class_="author-born-date").get_text()
        location_author = bs_ad.find(class_="author-born-location").get_text()

        author_initials = quote_to_guess['author'].split(" ")
        fn_author = author_initials[0][0].upper()
        ln_author = author_initials[-1][0].upper()

        print(f"Here's a quote:\n\n{quote_to_guess['quote']}")
        print(quote_to_guess["author"])

    if guess_attempt == 0:
        print("sorry you fail")
        break

    guessed_input = input(
        f"\nWho said this? Guesses remaining: {guess_attempt}. ")

    if quote_to_guess["author"].lower() == guessed_input.lower():
        print("You guessed correctly! Congratulations!")
        if "y" == input("Would you like to play again (y/n)? "):
            print("Great! Here we go again...\n")
            guess_attempt = 4
            continue
        else:
            break

    guess_attempt -= 1

    if guess_attempt == 3:

        print(f"Here's a hint: Born at {date_author} {location_author}")
    elif guess_attempt == 2:
        print(
            f"Here's a hint: The author's first name starts with '{fn_author}'")
    elif guess_attempt == 1:
        print(
            f"Here's a hint: The author's last name starts with '{ln_author}'")
