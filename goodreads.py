import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv

url = 'https://www.goodreads.com/list/show/155178.New_York_Times_100_Notable_Books_of_2020'

response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")


i = 0
j = 0

csv_file = open("bookInfo.csv", "w")

for i in range(100):
	# prints out author's name and book title within html elements with these attributes
	authorTitle = soup.find_all('span', attrs={'itemprop':'name'})[i].text
	avgRating = soup.find_all('span', attrs={'class':'minirating'})[i].text
	csv_file.write(authorTitle)
	csv_file.write("\n")
	csv_file.write(avgRating)
	csv_file.write("\n")
	print(authorTitle)
	time.sleep(1)




csv_file.close()

base = 'https://www.goodreads.com'


# find book links

# bookLink = soup.find_all(class_='bookTitle', href=True)
k = 1
l = 0
m = 31

for link in soup.find_all('a', class_='bookTitle'):
   	# print(link.get('href'))
	# link.get('href')
	book = link['href']
	burl = base + book
	# print(burl)
	bookInfo = requests.get(burl)
	book_specific_info = BeautifulSoup(bookInfo.text, 'html.parser')

	book_pub = book_specific_info.find_all(class_="row")[k].text
	book_pages = book_specific_info.find_all(class_="row")[l].text
	book_summ = book_specific_info.find_all('span')[m].text
	print(book_pub)
	print(book_summ)
	time.sleep(1)