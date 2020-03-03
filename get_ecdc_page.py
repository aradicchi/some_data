'''
A script for downloading the ecdc page with status on coronavirus.
'''
import requests
from bs4 import BeautifulSoup
import datetime as dt
import wget

ecdc_uri = "https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases"
out_folder = "ecdc_pages"

r = requests.get(ecdc_uri)
soup = BeautifulSoup(r.text,'html.parser')
print("-> report title:", soup.title.text)

out_file = "%s/ecdc_worldwide_%s.html" % (out_folder,dt.datetime.today().strftime("%Y%m%d"))
print("-> saving to:", out_file)
wget.download(ecdc_uri,out_file)
