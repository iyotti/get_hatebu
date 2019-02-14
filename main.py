# -*- coding: utf-8 -*-
import requests, sys, webbrowser, bs4, os
import csv
import requests

def scraping_hatena():
	url = 'http://b.hatena.ne.jp/'

	#ぺーじDL
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.content,'html.parser')

	title = soup.select('div > h3 > a.js-keyboard-openable')
	if title == []: print("見つからなかった")

	for i in range(len(title)):
		arr = [title[i].getText(),title[i].get('href')]
		output(arr)


def output(arr):
	os.makedirs("csv",exist_ok=True)

	with open(os.path.join('csv','hatena_log.csv'),'a',encoding="utf-8") as csv_file:
		csv_writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
		csv_writer.writerow(arr)
		csv_file.close()


if __name__ == '__main__':
	scraping_hatena()
