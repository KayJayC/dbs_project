import requests
from bs4 import BeautifulSoup

URL= "https://www.nytimes.com/interactive/2020/books/notable-books.html"
page = requests.get(URL)

soup = BeautifulSoup( page.content, "html.parser")

results = soup.find(id = "app")

job_elements = results.find_all("div", class_= "g-book-data")

for job_element in job_elements:
	title_element = job_element.find("div" , class_= "g-book-title balance-text")
	
	#split up the book info
	book_info_element= job_element.find("div", class_= "g-book-author balance-text")
	#author, extra =  book_info_element.text

	tags= job_element.find("span", class_="g-book-tag")
	description= job_element.find("div", class_= "g-book-description")
	print( title_element.text.strip())
	print()
	print( book_info_element.text.strip())
	print ( tags.text.strip())
	print (description.text.strip())
	print()