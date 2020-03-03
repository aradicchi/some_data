import datetime as dt
import wget

ecdc_uri = "https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases"
out_folder = "ecdc_pages"

wget.download(ecdc_uri,"%s/ecdc_worldwide_%s.html" % (out_folder,dt.datetime.today().strftime("%Y%m%d")))
