# -*- coding: utf-8 -*-
import requests, sys, webbrowser, bs4, os
import csv
import requests
import datetime

def scraping_hatena():
	url = 'http://b.hatena.ne.jp/'

	#ぺーじDL
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.content,'html.parser')

	title = soup.select('div > h3 > a.js-keyboard-openable')
	if title == []:
		print("見つからなかった")
		return
	arr = []
	for i in range(len(title)):
		tmp = [title[i].getText(),title[i].get('href')]
		arr.append(tmp)
	output(arr)


def output(arr):
	csv_name = 'hatena_log_'+datetime.datetime.now().strftime('%Y%m%d')+'.csv'

	with open(os.path.join('csv',csv_name),'a',encoding="utf-8") as csv_file:
		csv_writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
		csv_writer.writerows(arr)
		csv_file.close()


if __name__ == '__main__':
	os.makedirs("csv",exist_ok=True)

	scraping_hatena()
