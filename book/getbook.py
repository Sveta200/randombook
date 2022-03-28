import requests
from bs4 import BeautifulSoup
import random

def randomBook(link, header):
    textlink = open(link)
    url = textlink.read()
    urlBook = url.split("\n")
    urlBook = urlBook[random.randrange(1, 200)]

    resp = requests.get(urlBook, header)
    resp = resp.text

    soup = BeautifulSoup(resp, "lxml")
    titlebook = soup.find("h1", class_="title").text
    caption = soup.find("article", class_="post").find("p").text
    img = soup.find("img", class_="wp-image-12689")
    book = {
        "text": titlebook+"\n"+caption,
        "img": img["src"],
        "url": "\n\n <b>Читать</b>\n"+urlBook,
    }
    return book


