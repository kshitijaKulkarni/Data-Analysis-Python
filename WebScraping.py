import sys
reload(sys)
sys.setdefaultencoding('utf8')

import csv
import requests
from bs4 import BeautifulSoup
url = 'http://espn.go.com/college-football/bcs/_/year/2013'
response = requests.get(url)
html = response.content

soup = BeautifulSoup((html), "lxml")
table = soup.find('table',attrs={'class': 'tablehead'})

list_of_rows = []
for rows in table.findAll('tr')[0:]:
	list_of_cells = []
	for cell in rows.findAll('td'):
		text = cell.text.replace('&nbsp;', '')
		list_of_cells.append(text)
	list_of_rows.append(list_of_cells)
	
outfile = open("./Rankings.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
