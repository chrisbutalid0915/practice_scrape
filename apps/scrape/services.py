from django.contrib.sites.models import Site
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime
from fake_useragent import UserAgent
import requests
import random


def scrape(url):
    # scrape url "https://quotes.toscrape.com/"
    user_agents = UserAgent()
    headers = {
        "User-Agent": user_agents.random,
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    now = datetime.now()
    formatted_date_time = now.strftime("%Y%m%d%H%M")
    wb = Workbook()  # Create a new Workbook object
    ws = wb.active  # Select the active worksheet

    page_to_scrape = requests.get(url, headers=headers)
    if page_to_scrape.status_code == 200:
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        quotes = soup.findAll("span", attrs={"class": "text"})
        authors = soup.findAll("small", attrs={"class": "author"})

        ws.append(["Quote", "Author"])
        for quote, author in zip(quotes, authors):
            ws.append([quote.text, author.text])

        file_name = f"data_scrape_{formatted_date_time}"
        path = "./export/scrapes/"
        file_format = ".xlsx"
        file_path = f"{path}{file_name}{file_format}"
        wb.save(file_path)
    else:
        print("Failed to retrieve page:", page_to_scrape.status_code)
