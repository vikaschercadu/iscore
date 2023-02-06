#! /usr/bin/python3

import notify2
import requests,bs4,pprint
import time


while True:
	try:
		respond=requests.get('https://cricbuzz.com')
		soup=bs4.BeautifulSoup(respond.text,'html.parser')
		element = soup.find_all('div', {'class': 'cb-col cb-col-25 cb-mtch-blk'})
	except Exception as err:
		print('error:',err)


	for match in element:
		if 'IND' in match.getText():
			#pprint.pprint(match.getText())
			break
	notify2.init('app name')
	n = notify2.Notification("Match Score",
	                         match.getText(),
	                         "notification-message-im" 
	                        )
	n.show()
	time.sleep(int(60))
