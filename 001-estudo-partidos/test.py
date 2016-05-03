import csv
import urllib2
from time import gmtime, strftime
import time
print("-------------------------------------------------------------------------------")

CHUNK = 2048 * 4096  #6 Mb por vez

"""
base_url = "http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/"
file_name = "filiados_pmdb_ap.zip"	
url = base_url + file_name
fp = open(file_name, 'wb')
req = urllib2.urlopen(url)
for line in req:
		fp.write(line)
fp.close()
"""
i=1
#"""
with open('temp.csv', 'rb') as csvfile:
	# get number of columns
    for line in csvfile.readlines():
        array = line.split(';')
        first_item = array[0]
	file_name = first_item.split('\r\n')[0]
	print "[" + strftime("%H:%M:%S", gmtime()) + "] " + "Fazendo o download do #" + str(i)+" arquivo: " + first_item
	base_url = "http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/"
	url = base_url + file_name
	#urllib.urlretrieve (url, file_name)
	req = urllib2.urlopen(url)
	
	fp = open(file_name, 'wb')
	with open(file_name, 'wb') as f:
		while True:
			chunk = req.read(CHUNK)
			if not chunk: break
			f.write(chunk)
	#for line in req:
	#	fp.write(line)
	fp.close()
	i=i+1
	time.sleep(0.1)
	

	
	
	
print("-------------------------------------------------------------------------------")
"""
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		print ', '.join(row(1))

base_url = "http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/"
file_name = "filiados_pmdb_ap.zip"
url = base_url + file_name
urllib.urlretrieve (url, "zips/" + file_name)

"""