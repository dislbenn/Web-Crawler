#!usr/bin/python
"""Web Crawler designed to find products and ratings for products developed and targeting seniors.
"""
import os
from urllib.request import urlopen
import unicodecsv as csv
from bs4 import BeautifulSoup

__author__ = "Disaiah Bennett"
__version__ = "0.1"

class WebCrawler:
    """Web Crawler
    """
    def __init__(self, url=None, page=None, data=None, clean=None):
        """This is the inside of my web crawler
        """
        self.url = url
        self.page = page
        self.data = data
        self.categories = []
        self.catlinks = []
        self.clean = clean

    def data_extract(self):
        """Extract the url page data and parses the information with BeautifulSoup
        """
        self.page = urlopen(self.url)
        self.data = self.page.read()

        self.page.close()
        soup = BeautifulSoup(self.data, "html.parser")

        return soup

    def get_categories(self):
        """Returns all categories
        """
        return self.categories

    def cleanup(self):
        """Cleans up directory
        """
        print("CLEANING FILES\n")
        self.clean = True
        try:
            os.system(". ./move_csv.sh")
        except OSError:
            print("CLEANING FAILED")
        return self.clean

def main():
    """Extract data from the walmart website and return the information into a csv file.
    """
    url = "https://www.walmart.com/cp/home-health-care/1005860"
    crawler = WebCrawler()

    # Set the url of the crawler
    crawler.url = url
    soup = crawler.data_extract()

    cat_product_price = []
    cat_product_link = []
    cat_product_rating = []

    cat_sidebar_li = soup.find_all("li", {"class": "SideBarMenuModuleItem"})

    for category in cat_sidebar_li:
        links = category.findAll("a", {"class": "SideBarMenu-toggle"})
        item = category.findAll("span", {"class": "SideBarMenu-title"})

        for link in links:
            crawler.catlinks.append(link.get('href'))

        for item in category:
            head, _, _ = item.text.partition("-")
            if len(head) > 30:
                pass
            else:
                crawler.categories.append(head)

    count = 0
    for i, _ in enumerate(crawler.categories):
        # Set the url of the crawler
        crawler.url = crawler.catlinks[i]

        # Open individual CSV File
        csv_file = csv.writer(open(crawler.categories[i] + ".csv", "wb"))
        csv_file.writerow(["#", crawler.categories[i], "Price", "Rating", "Link", "Top Review"])

        # Parse html data
        soup = crawler.data_extract()

        print("Current Category", crawler.categories[i], "URL: ", crawler.catlinks[i])

        # Products to a list
        prods = soup.find_all("a", {"class": "product-title-link line-clamp line-clamp-2"})

        # Ratings [Done]
        ratings = soup.find_all("span", {"class": "seo-avg-rating"})

        # Price
        price_current = soup.find_all("div", {"class": "price-main-block"})

        # Links [Done]
        links = soup.find_all("div", {"class": ["search-result-productimage gridview", "search-result-productimage listview"]})

        for link in links:
            sub_links = link.find_all("a", {"class": "display-block"})
            for j, _ in enumerate(sub_links):
                cat_product_link.append(sub_links[j].get("href"))

        # For k in the range of products total
        for k, _ in enumerate(prods):
            try:
                rate = float(ratings[k].text)

                cat_product_rating.append(round(rate, 1))
                cat_product_price.append(price_current[k].text)

                csv_file.writerow([k+1, prods[k].text, cat_product_price[k], str(cat_product_rating[k]) + "/5.0", "https://www.walmart.com" + cat_product_link[k], "blank"])

            except IndexError:
                pass

        print(crawler.categories[count] + ".csv file created.\n")
        count += 1
        cat_product_price.clear()
        cat_product_link.clear()
        cat_product_rating.clear()
    crawler.cleanup()

if __name__ == "__main__":
    main()
