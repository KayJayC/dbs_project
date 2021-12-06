import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv

url = 'https://www.goodreads.com/list/show/155178.New_York_Times_100_Notable_Books_of_2020'

response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")


# i = 0
# j = 1
# index = 0

# csv_file = open("bookInfoC.csv", "w")
# csv_file.write("id, title, author, rating, cover \n")

# for link in soup.find_all('img', attrs={'class':'bookCover'}):
# 	# prints out author's name and book title within html elements with these attributes
# 	title = soup.find_all('span', attrs={'role':'heading'})[i].text
# 	author = soup.find_all('span', attrs={'itemprop':'name'})[j].text
# 	j += 2
# 	avgRating = soup.find_all('span', attrs={'class':'minirating'})[i].text
# 	i += 1

# 	cover = link.get('src')
# 	csv_file.write(str(index))
# 	csv_file.write(',')
# 	csv_file.write(title)
# 	csv_file.write(',')
# 	csv_file.write(author)
# 	csv_file.write(',')
# 	csv_file.write(avgRating)
# 	csv_file.write(',')
# 	csv_file.write(cover)
# 	csv_file.write('\n')
# 	index += 1
# 	time.sleep(1)


# csv_file.close()



base = 'https://www.goodreads.com'


# find book links

bookLink = soup.find_all(class_='bookTitle', href=True)
k = -2
l = 0
m = 31

csv_file = open("bookInfo2.csv", "w")

csv_file.write("published, pages, summary \n")

for link in soup.find_all('a', class_='bookTitle'):
   	# print(link.get('href'))
	# link.get('href')
	book = link['href']
	burl = base + book
	# print(burl)
	bookInfo = requests.get(burl)
	book_specific_info = BeautifulSoup(bookInfo.text, 'html.parser')
	
	book_pub = book_specific_info.find_all('div', class_="row")[k].text
	book_pages = book_specific_info.find_all(class_="row")[l].text
	book_summ = book_specific_info.find_all('span')[m].text

	k += -1

	csv_file.write(book_pub)
	csv_file.write(',')
	csv_file.write(book_pages)
	csv_file.write(',')
	csv_file.write(book_summ)
	csv_file.write("\n")
	
	time.sleep(1)

csv_file.close()


