#!usr/bin/python
"""Web Crawler designed to find products and ratings for products developed and targeting seniors.
"""
import sys
import unicodecsv as csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep

__author__ = "Disaiah Bennett"
__version__ = "0.1"

class web_crawler:
    def __init__(self, url=None, page=None, data=None, **kwargs):
        self.url = url
        self.page = page
        self.data = data
    
    def get_url(self):
        return self.url

    def data_extract(self):
        self.page = urlopen(self.url)
        self.data = self.page.read()

        self.page.close()
        soup = BeautifulSoup(self.data, "html.parser")

        return soup
        
def main():
    url = "https://www.walmart.com/cp/home-health-care/1005860"
    crawler = web_crawler()

    crawler.url = url # Set the url of the crawler
    soup = crawler.data_extract()

    categories_names = []
    categories_links = []
    categories_product = []
    categories_product_review = []
    categories_product_price = []

    cat_sidebar_li = soup.find_all("li", {"class": "SideBarMenuModuleItem"})

    for category in cat_sidebar_li:
        links = category.findAll("a", {"class": "SideBarMenu-toggle"})
        item = category.findAll("span", {"class": "SideBarMenu-title"})

        for link in links:
            categories_links.append(link.get('href'))
        
        for item in category:
            head, _, _ = item.text.partition("-")
            if len(head) > 30:
                pass
            else:
                categories_names.append(head)
    
    for i in range(len(categories_names)):
        csv_file = csv.writer(open(categories_names[i] + ".csv", "wb")) # Open individual CSV File
        csv_file.writerow([categories_names[i], "Price", "Rating", "Top Review"])

        temp_page = urlopen(categories_links[i])
        temp_data = temp_page.read()
        temp_page.close()
        
        temp_soup = BeautifulSoup(temp_data, "html.parser")

        print("Current Category", categories_names[i], "URL: ", categories_links[i], "\n\n")
        products = temp_soup.find_all("a", {"class": "product-title-link line-clamp line-clamp-2"})
        reviews = temp_soup.find_all("span", {"class": "seo-avg-rating"})
        pricings = temp_soup.find_all("div", {"class": "product-variant-price"})
        
        for i in range(len(products)):
            categories_product.append(products[i].text) # Products to a list
            categories_product_review.append(reviews[i].txt)

            min_price = pricings.find_all("span", {"class": "price-min"})
            max_price = pricings.find_all("span", {"class": "price-max"})
            categories_product_price.append(min_price[i].text, max_price[i].text)

            csv_file.writerow([products[i].text, (min_price[i].text, max_price[i].text), reviews[i].text, "TBA"])

    #print("These are the categories names\n\n", categories_names, "\n\n")
    #print("These are the links\n\n", categories_links, "\n\n")
    #print("These are the sub links\n\n", categories_sub_links, "\n\n")

    extracted_file = csv.writer(open("walmart_senior_product.csv", "wb"))
    extracted_file.writerow(["#","Category Name", "Product Name", "Product Price", "Product Rating", "Product Review", "Category Links"])
    
    for i in range(len(categories_names)):
        extracted_file.writerow([i+1, categories_names[i], "Blank", "Blank", "Blank", "Blank", categories_links[i]])

if __name__ == "__main__":
    main()