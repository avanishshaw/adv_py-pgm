from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

url = "https://books.toscrape.com/"

response = requests.get(url)
