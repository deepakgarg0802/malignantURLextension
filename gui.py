from Tkinter import *
import tkMessageBox
import trainer as tr
import pandas
import utilities


def detect(url):
	if url.startswith("http://"):
		url= url[len("http://"):]

	if url.startswith("https://"):
		url= url[len("https://"):]

	url= "http://"+url
	print url
	flag=utilities.check_cache(url,'mycache.csv')

	if flag==0:
		return "The URL "+" is Safe"

	elif flag==1:
		return "The URL "+" is Malicious"
	
	elif flag==2:
		return "The URL "+" is Malware"

	else :

		utilities.features_to_csv(url,'test_features.csv')
		return_ans = tr.train_and_test('url_features.csv','test_features.csv')
		a=str(return_ans).split()

		if int(a[1])==0:
			flag=0
			utilities.append_result([url,flag],'mycache.csv')
			return "The URL "+" is Safe"

		elif int(a[1])==1:
			flag=1
			utilities.append_result([url,flag],'mycache.csv')
			return "The URL "+" is Malicious"
		else:
			flag=2
			utilities.append_result([url,flag],'mycache.csv')
			return "The URL "+" is Malware"

	   		   
if __name__ == '__main__':
	print detect("https://github.com")