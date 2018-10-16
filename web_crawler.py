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
    categories_product_price = []
    categories_product_link = []
    categories_product_rating = []

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
    count = 0
    for i in range(len(categories_names)):
        csv_file = csv.writer(open(categories_names[i] + ".csv", "wb")) # Open individual CSV File
        csv_file.writerow(["#", categories_names[i], "Price", "Rating", "Link", "Top Review"]) # Writing header to csv file.

        temp_page = urlopen(categories_links[i]) #opening temp page
        temp_data = temp_page.read() # Read temp page data
        temp_page.close() # Close the current page.
        
        temp_soup = BeautifulSoup(temp_data, "html.parser") # Parse html data

        print("Current Category", categories_names[i], "URL: ", categories_links[i])
        products = temp_soup.find_all("a", {"class": "product-title-link line-clamp line-clamp-2"}) # Products [Done]
        ratings = temp_soup.find_all("span", {"class": "seo-avg-rating"}) # Ratings [Done]
        price_current = temp_soup.find_all("div", {"class": "price-main-block"}) # Price 
        links = temp_soup.find_all("div", {"class": ["search-result-productimage gridview", "search-result-productimage listview"]}) # Links [Done]

        #print("\n\n", links, "\n\n")
        for link in links:
            li = link.find_all("a", {"class": "display-block"})
            for i in range(len(li)):
                #print(li[i].get("href"))
                categories_product_link.append(li[i].get("href"))

        for i in range(len(products)): # For i in the range of products total
            try:
                categories_product.append(products[i].text) # Products to a list
                rate = float(ratings[i].text)
                categories_product_rating.append(round(rate, 1))

                categories_product_price.append(price_current[i].text)
                csv_file.writerow([i+1, products[i].text, categories_product_price[i], str(categories_product_rating[i]) + "/5.0", "https://www.walmart.com" + categories_product_link[i], "blank"])
            except IndexError:
                pass
        
        print(categories_names[count] + ".csv file created.\n")
        count += 1
        categories_product_price.clear()
        categories_product_link.clear()
    
    # print("These are the categories names\n\n", categories_names, "\n\n")
    # print("These are the links\n\n", categories_links, "\n\n")
    # print("These are the ratings\n\n", categories_product_rating, "\n\n")
    # print("These are the prices\n\n", categories_product_price, "\n\n")
    # print("These are the product links\n\n", categories_product_price, "\n\n")

    # extracted_file = csv.writer(open("walmart_senior_product.csv", "wb"))
    # extracted_file.writerow(["#","Category Name", "Product Name", "Product Price", "Product Rating", "Product Review", "Category Links"])

    # for i in range(len(categories_names)):
        # extracted_file.writerow([i+1, categories_names[i], "Blank", "Blank", "Blank", "Blank", categories_links[i]])

if __name__ == "__main__":
    main()