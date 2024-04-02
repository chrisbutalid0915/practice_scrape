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
    wb = Workbook() # Create a new Workbook object
    ws = wb.active # Select the active worksheet

    page_to_scrape = requests.get(url, headers=headers)
    if page_to_scrape.status_code == 200:
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")
        quotes = soup.findAll("span", attrs={"class": "text"})
        authors = soup.findAll("small", attrs={"class": "author"})

        ws.append(["Quote", "Author"])
        for quote, author in zip(quotes, authors):
            ws.append([quote.text, author.text])

        file_name = f'data_scrape_{formatted_date_time}'
        path = "./export/scrapes/"
        file_format = ".xlsx"
        file_path = f"{path}{file_name}{file_format}"
        wb.save(file_path)
    else:
        print("Failed to retrieve page:", page_to_scrape.status_code)

#     if site.domain == "https://kidscompany.com.ph/baby.html?p=1":
#         page_to_scrape = requests.get(site.domain)
#         if page_to_scrape.status_code == 200:
#             soup = BeautifulSoup(page_to_scrape.text, "html.parser")
#             products = soup.findAll("li", attrs={"class": "product-item"})
#             ws.append(["Product", "Price", "Special Price"])
#             for product in products:
#                 product_name = product.find("a", class_="product-item-link").text.strip()
#                 old_price = 0
#                 special_price = 0
#                 special_price_span = product.find("span", class_="special-price")
#                 if special_price_span:
#                     old_price_span = product.find("span", class_="old-price")
#                     old_price = old_price_span.find('span', class_='price').text.strip()
#                     special_price = special_price_span.find('span', class_='price').text.strip()
#                 else:
#                     old_price = product.find('span', class_='price').text.strip()
                
#                 ws.append([product_name, old_price, special_price])

#             file_name = site.name + formatted_date_time
#             path = "./export/scrapes/"
#             file_format = ".xlsx"
#             file_path = f"{path}{file_name}{file_format}"
#             wb.save(file_path)
#         else:
#             print("Failed to retrieve page:", page_to_scrape.status_code)
#     if site.domain == "https://www.amazon.com/s?i=electronics-intl-ship&rh=n%3A16225009011&fs=true":
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
#             "Accept-Language": "en-US,en;q=0.5",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Connection": "keep-alive",
#         }
            
#         page_to_scrape = requests.get(site.domain, headers=headers)
#         if page_to_scrape.status_code == 200:
#             soup = BeautifulSoup(page_to_scrape.text, "html.parser")
#             products = soup.findAll("div", attrs={"class": "sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"})
#             ws.append(["Product", "Price", "Special Price"])
#             for product in products:
#                 old_price = 0
#                 special_price = 0
#                 product_price_amount = 0
#                 product_section = product.find("div", class_="a-section a-spacing-small puis-padding-left-small puis-padding-right-small")
#                 product_name_a = product_section.find("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
#                 product_name = product_name_a.find("span", class_='a-size-base-plus a-color-base a-text-normal').text.strip()
#                 # print(product_name)
#                 # product_section = product.find("div", class_="a-section a-spacing-none a-spacing-top-small s-title-instructions-style")
#                 # product_name_a = product_section.find("a", class_="a-link-normal")
#                 # product_name = product_name_a.find("span", class_='a-size-base-plus a-color-base a-text-normal').text.strip()

#                 # product_section_price = product.find("div", class_="a-section a-spacing-none a-spacing-top-small s-price-instructions-style")
#                 # print(product_section_price)
#                 product_price_a = product_section.find("a", class_="a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal")
#                 # product_price_amount = product_price_a.find("span", class_='a-price-whole').text.strip()
#                 # product_price_amount = product_section.find('span', class_='a-price-whole').text.strip()
#                 if product_price_a:
#                     product_price_amount = product_price_a.find("span", class_='a-offscreen').text.strip()
#                     # product_price_span = product_price_a.find("div", class_="a-price a-text-price")
#                     # old_price = product_price_span.find("span", class_='a-offscreen').text.strip()

#                     # product_price_whole = product_price_a.find("span", class_='a-price-whole').text.strip()
#                     # product_price_fraction = product_price_a.find("span", class_='a-price-fraction').text.strip()
#                     # product_price_amount = f'{product_price_whole}{product_price_fraction}'
#                     # print(product_price_amount)
#                 # product_price_symbol = product_price_a.find("span", class_='a-price-symbol').text.strip()
#                 # product_price_amount = product_price_a.find("span", class_='a-price-whole').text.strip()

#                 # product_price = f'{product_price_symbol} {product_price_amount}'

#                 ws.append([product_name, old_price, product_price_amount])

#             file_name = site.name + formatted_date_time
#             path = "./export/scrapes/"
#             file_format = ".xlsx"
#             file_path = f"{path}{file_name}{file_format}"
#             wb.save(file_path)
#         else:
#             print("Failed to retrieve page:", page_to_scrape.status_code)

# def start_scrape(url):
#     user_agents = UserAgent()
#     headers = {
#             "User-Agent": user_agents.random,
#             "Accept-Language": "en-US,en;q=0.5",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Connection": "keep-alive",
#         }
#     print(headers)
#     now = datetime.now()
#     formatted_date_time = now.strftime("%Y%m%d%H%M")
#     wb = Workbook() # Create a new Workbook object
#     ws = wb.active # Select the active worksheet

#     # site = Site.objects.get(domain=url)
#     page_to_scrape = requests.get(url, headers=headers)
#     if page_to_scrape.status_code == 200:
#         soup = BeautifulSoup(page_to_scrape.text, "html.parser")
#         products = soup.findAll("div", attrs={"class": "sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"})
#         ws.append(["Product", "Price", "Special Price"])
#         for product in products:
#             old_price = 0
#             special_price = 0
#             product_price_amount = 0
#             product_section = product.find("div", class_="a-section a-spacing-small puis-padding-left-small puis-padding-right-small")
#             product_name_a = product_section.find("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
#             product_name = product_name_a.find("span", class_='a-size-base-plus a-color-base a-text-normal').text.strip()
#             # print(product_name)
#             # product_section = product.find("div", class_="a-section a-spacing-none a-spacing-top-small s-title-instructions-style")
#             # product_name_a = product_section.find("a", class_="a-link-normal")
#             # product_name = product_name_a.find("span", class_='a-size-base-plus a-color-base a-text-normal').text.strip()

#             # product_section_price = product.find("div", class_="a-section a-spacing-none a-spacing-top-small s-price-instructions-style")
#             # print(product_section_price)
#             product_price_a = product_section.find("a", class_="a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal")
#             # product_price_amount = product_price_a.find("span", class_='a-price-whole').text.strip()
#             # product_price_amount = product_section.find('span', class_='a-price-whole').text.strip()
#             if product_price_a:
#                 product_price_amount = product_price_a.find("span", class_='a-offscreen').text.strip()
#                 # product_price_span = product_price_a.find("div", class_="a-price a-text-price")
#                 # old_price = product_price_span.find("span", class_='a-offscreen').text.strip()

#                 # product_price_whole = product_price_a.find("span", class_='a-price-whole').text.strip()
#                 # product_price_fraction = product_price_a.find("span", class_='a-price-fraction').text.strip()
#                 # product_price_amount = f'{product_price_whole}{product_price_fraction}'
#                 # print(product_price_amount)
#             # product_price_symbol = product_price_a.find("span", class_='a-price-symbol').text.strip()
#             # product_price_amount = product_price_a.find("span", class_='a-price-whole').text.strip()

#             # product_price = f'{product_price_symbol} {product_price_amount}'

#             ws.append([product_name, old_price, product_price_amount])

#         file_name = "test_scrapte_" + formatted_date_time
#         path = "./export/scrapes/"
#         file_format = ".xlsx"
#         file_path = f"{path}{file_name}{file_format}"
#         wb.save(file_path)
#     else:
#         print("Failed to retrieve page:", page_to_scrape.status_code)