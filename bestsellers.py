#Hello this scrip will list out all the best sellers on Amazon.com
import requests
from bs4 import BeautifulSoup as bs

#Load the webpage
r = requests.get("https://www.amazon.com/Best-Sellers/zgbs/fashion/ref=zg_bs_nav_0")

#convert to bautiful soup object
soup = bs(r.content, "html.parser")

#print HTML
#print(soup.prettify())

#Get Title
title = soup.find("title")
print(title)

#Get all the items displayed
