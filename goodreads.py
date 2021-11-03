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


# for j in range(100):
# 	# prints out average rating within html elements with these attributes
# 	csv_file.write(avgRating)
# 	csv_file.write("\n")
# 	print(avgRating)
# 	time.sleep(1)

csv_file.close()


# for k in range(100):
# 	summary = soup.find_all('a', attrs={'class':'bookTitle'})


# do we need book summaries?
# url2 = 'https://www.goodreads.com'

# genURL = requests.get(url2)