import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv

# print("pls work")

# burl = 'https://www.barnesandnoble.com/b/discover-title/best-books-of-the-year-2020/new-york-times-best-books-of-2020/_/N-2l0fZ2v3u?Nrpp=40&page=1'

# rep = requests.get(burl)

# soup = BeautifulSoup(rep.text, "html.parser")

# work = soup.find('a', attrs={'title class':'current'})


# print(work)

burl = 'https://www.amazon.com/hz/wishlist/ls/1MBO8N1KWEIGC/ref=nav_wishlist_lists_4?_encoding=UTF8&type=wishlist'

rep = requests.get(burl)

soup = BeautifulSoup(rep.text, "html.parser")


file = open("amazon.csv", "w")
file.write("id, book info, price \n")
# work = soup.find('span', attrs={'class':'a-offscreen'})

i = 1
j = 0

for title in soup.find_all('div', attrs={'class':'a-row a-size-small'}):
    new_title = title.text.strip()
    title_info = new_title.split()
    fin = " ".join(title_info)

    
    file.write(str(i))
    file.write(",")
    file.write(fin)
    file.write(",")

    price = soup.find_all('span', attrs={'class':'a-offscreen'})[j].text
    file.write(price)
    file.write("\n")
    
    i += 1
    j += 1


# for price in soup.find_all('span', attrs={'class':'a-offscreen'}):
#     new_price = price.text.strip()
#     print(new_price)

# elements = soup.find_all('div', attrs={'class':'a-row'})

# for element in elements:
#     title = element.find('div', attrs={'class':'a-row a-size-small'})[0].text
#     # new_title = title.text.strip()
#     # title_info = new_title.split()
#     # fin = " ".join(title_info)

#     # price = element.find_all('span', attrs={'class':'a-offscreen'})
#     # new_price = price.text.strip()
#     # print(new_price)




