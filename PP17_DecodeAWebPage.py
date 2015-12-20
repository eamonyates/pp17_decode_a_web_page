import requests
from bs4 import BeautifulSoup


def title_grab(web_page):
	
	r = requests.get(web_page)
	soup = BeautifulSoup(r.text, 'html.parser')
	
	for title in soup(class_='story-heading'):
		if title.a:
			print(title.a.text.replace("\n", " ").strip())
		else:
			print(title.contents[0].strip())


if __name__ == '__main__':
	title_grab('http://www.nytimes.com')
