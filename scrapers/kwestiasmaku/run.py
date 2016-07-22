import requests, bs4
from itertools import chain
from bs4 import BeautifulSoup

def fetch_html(template, text):
	url = template.format(text)
	print("Scraping from: {}".format(url))
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	return soup


def get_links_from_page(page: int):
	soup = fetch_html('http://www.kwestiasmaku.com/przepisy?sort_by=created&sort_order=&page={}', page)

	for span in soup.find_all('span', {"class":"field-content"}):
		for link in span.find_all('a'):
			href = link.get('href')
			if 'przepis' in href:
				yield href

def get_all_links():
	for i in range(68):
		for link in get_links_from_page(i):
			yield link	

def scrap(link):
	soup = fetch_html('http://www.kwestiasmaku.pl/{}', link)
	output = []

	output.append('<!START>')
	output.append('<!SKLADNIKI>:')
	for x in soup.find_all('div', {'class': "field-name-field-skladniki"}):
		for y in x.find_all('li'):
			output.append(y.text.strip())

	output.append('<!PRZEPIS>')
	for x in soup.find_all('div', {'class': "field-name-field-przygotowanie"}):
		for y in x.find_all('li'):
			output.append(y.text.strip())

	output.append('<!STOP>')
	return output

def dump_array(array, file):
	with open(file, "a") as text_file:
		for line in array:
			print(line, file=text_file)


if __name__ == '__main__':
	for index, href in enumerate(get_all_links()):
		print ('{} {}'.format(index, href))
		dump_array(scrap(href), 'input.txt')


