import csv
import scrapy
from bs4 import BeautifulSoup
from pathlib import Path
import re
import os
import traceback
import json
import urllib2

def make_sure_path_exists(directoryName):
	try:
		if not os.path.exists(directoryName):
			os.makedirs(directoryName)
	except OSError as exception:
		print "Unable to create directory" + directoryName

class ToiSpider(scrapy.Spider):
	name = "toiscrapper"

	count_total_scrapped = 0;
	count_successfully_scrapped = 0;
	count_no_data = 0;
	count_missed_totally = 0;

	def start_requests(self):
		base_url_1 = 'http://timesofindia.indiatimes.com/2009/1/1/archivelist/year-2009,month-1,starttime-'
		base_url_2 = '.cms'

	#	print "Scrapping Started for "+base_url_1+". Please wait..."
		make_sure_path_exists('output');
		make_sure_path_exists('status');
		for month in xrange(39814,40179):
			url = base_url_1 + str(month) + base_url_2;
		#	print "Url to be scrapped for "+str(self.count_total_scrapped)+" : "+url
			yield scrapy.Request(url = url, callback = self.parse_page)

	def parse_page(self, response):
		#print response
		self.count_total_scrapped = self.count_total_scrapped + 1
		#print self.count_total_scrapped

		page = response.css('table.cnt').extract()[1]
		soup = BeautifulSoup(page, 'html.parser')
		arr =  soup.find_all('a')

		for a in arr:
		
			a_text = a.string
			a_link = a.get('href')


			if a_text and (' hiv ' in a_text.encode('utf8').lower() or 'hiv ' in a_text.encode('utf8').lower() or ' hiv' in a_text.encode('utf8').lower()):
				self.count_successfully_scrapped = self.count_successfully_scrapped +1

				print "Entry: "+str(self.count_successfully_scrapped)
				#print a
				print a_text
				print "Link: "
				print a_link
				print
				
	        # 	with open("output/files.txt", "wb") as myFile:
	        # 		if a: myFile.write(a.encode('utf8'))
	        # 		if a_text: myFile.write(a_text.encode('utf8'))
	        # 		if a_link: myFile.write(a_link.encode('utf8'))
	        #     	myFile.closed

	        # with open("output/all_data.txt", "wb") as myFile:
	        # 	if a: myFile.write(a.encode('utf8'))
	        # 	if a_text: myFile.write(a_text.encode('utf8'))
	        # 	if a_link: myFile.write(a_link.encode('utf8'))
	        #    	myFile.closed
	        # 