## Basic for web scrap

## Author: Abdul Basit

from bs4 import BeautifulSoup as soup
from urlib.request import urlopen as urq

my_url = 'site url'

client = urq(my_url)
page_html = client.read()
client.close()
page_soup = soup(page_html, 'html.parser')

containers = page_soup.findAll('div',('class' : 'col_2-gk'))

print(len(containers))

print(soup.prettify(containers[0]))

container = containers[0]
print(container.div.img['alt'])


