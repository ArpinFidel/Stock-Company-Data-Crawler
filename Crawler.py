from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import os
import time

class Company:
	def __init__(self, data):
		self.code = data[1].get_attribute('innerHTML')
		self.name = data[2].get_attribute('innerHTML')
		self.recDate = data[3].get_attribute('innerHTML')
		self.stock = data[4].get_attribute('innerHTML')
		self.board = data[5].get_attribute('innerHTML')
		
		

runPath = os.path.dirname(os.path.abspath(__file__))

op = webdriver.ChromeOptions()
prefs = {	'profile.default_content_setting_values': {
				'cookies': 2, 'images': 2,
				'plugins': 2, 'popups': 2, 'geolocation': 2, 
				'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
				'mouselock': 2, 'mixed_script': 2, 'media_stream': 2, 
				'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
				'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
				'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
				'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
				'durable_storage': 2},
			'disk-cache-size': 4096}

op.add_experimental_option("prefs", prefs)

op.add_argument('headless')
op.add_argument("--disable-notifications");

url = 'https://www.idx.co.id/data-pasar/data-saham/daftar-saham/'

browser = webdriver.Chrome(runPath+'\\lib\\chromedriver.exe',options=op)

browser.implicitly_wait(20)

browser.get(url)

buttonNext = browser.find_element(By.ID, 'stockTable_next')

Select(browser.find_element(By.NAME, 'stockTable_length')).select_by_value('100')

companies = list()

time.sleep(5)

for i in range(7):
	while True:
		while  True:
			try:
				table = browser.find_element(By.ID, 'stockTable').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
				rowNum = int(table[0].find_elements(By.TAG_NAME, 'td')[0].get_attribute('innerHTML'))
				print('table html:', table[0].get_attribute('innerHTML'))
				print('rownum:', rowNum)
			except Exception as e:
				print(e)
				continue
			break
			
		if rowNum == i*100+1:
			break
		else:
			time.sleep(0.5)
	
	print('table length:', len(table))
	
	for row in table:
		while True:
			try:
				# print('row html:', row.get_attribute('innerHTML'))
				data = row.find_elements(By.TAG_NAME, 'td')
				print('data: ', data[1].get_attribute('innerHTML'))
			except Exception as e:
				print(e)
				print('failed. retrying')
				continue
			break
		companies.append(Company(data))
	
	while True:
		try:
			buttonNext.click()
		except Exception as e:
			print(e)
			buttonNext = browser.find_element(By.ID, 'stockTable_next')
			time.sleep(0.5)
			continue
		break
	
for c in companies:
	print(c.code)
