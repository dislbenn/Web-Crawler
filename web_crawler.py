#!usr/bin/python
"""Web Crawler designed to find products and ratings for products developed and targeting seniors.
"""
import os
from urllib.request import urlopen
#from urllib import urlopen (python2)
from bs4 import BeautifulSoup

__author__ = "Disaiah Bennett"
__version__ = "0.1"

class WebCrawler:
    """Web Crawler
    """
    def __init__(self, url=None, page=None, data=None, clean=False):
        """This is the inside of my web crawler
            url: string - the url
            page: object - the url page.
            data: object - the page data.
            categories: list - navigation categories
            catlinks: list - navigation categories links
            clean: bool - places csv files into csv directory
            count: int - category list item count
        """
        self.url = url
        self.page = page
        self.data = data
        self.categories = []
        self.catlinks = []
        self.clean = clean
        self.count = 0

    def data_extract(self):
        """Extract the url page data and parses the information with BeautifulSoup
        """
        self.page = urlopen(self.url)
        self.data = self.page.read()

        self.page.close()
        soup = BeautifulSoup(self.data, "html.parser")

        return soup

    def get_url(self):
        """Gets the url that the webcrawler will be accessing.
            Returns:
                url: string - the url.
            Example:
                >>> example_url = crawler.get_url()
        """
        return self.url

    def get_page(self):
        """Gets the page that the webcrawler is parsing data from.
            Returns:
                self.page: string - the page of the url.
            Example:
                >>> example_page = crawler.get_page()
        """
        return self.page

    def get_data(self):
        """Get the data that the webcrawler is parsing
            Returns:
                self.data: string - page data.
            Example:
                >>> example_data = crawler.get_data()
        """
        return self.data

    def get_nav_categories(self):
        """Get the categories parsed within the webcrawler.
            Returns:
                self.categories: list - list of categories within the navigation bar.
            Example:
                >>> example_categories = crawler.get_nav_categories()
        """
        return self.categories

    def get_nav_catlinks(self):
        """Get the category links within the webcrawler.
            Returns:
                self.catlinks: list - list of category links within the navigation bar.
            Example:
                >>> example_catlinks = crawler.get_nav_catlinks()
        """
        return self.catlinks

    def cleanup(self):
        """Clean up csv files in the current directory, and saves them to csv folder.
            Returns:
                self.clean: bool - file cleaned.
        """
        self.clean = True
        try:
            os.system(". ./move_csv.sh")
        except OSError:
            print("CLEANING FAILED")
        return self.clean
