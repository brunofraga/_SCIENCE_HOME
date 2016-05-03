import csv
import urllib2
from time import gmtime, strftime
import time
import thread
from itertools import islice

CHUNK = 2048 * 4096  #6 Mb per read iteration

#Same thing, but with threads now
def getMyFilesBitch (initial_line, length):
	with open('temp.csv', 'rb') as csvfile:
		ith_line = 0
		for line in islice(csv.reader(csvfile), initial_line-1, length):
			ith_line = ith_line+1
			#dont know why but it go the reverse if i dont pick the last first
			array = line[-1].split(';')
			first_item = array[0]
			file_name = first_item.split('\r\n')[0]
			base_url = "http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/"
			url = base_url + file_name
			req = urllib2.urlopen(url)
		
			fp = open(file_name, 'wb')
			with open(file_name, 'wb') as f:
				while True:
					chunk = req.read(CHUNK)
					if not chunk: break
					f.write(chunk)
			fp.close()
			time.sleep(0.1)
			print "Arquivo #" + str(initial_line-1 + ith_line) + " carregado!"


print("-------------------------------------------------------------------------------")

# Creating some threads
START_ROW = 1
FINAL_ROW = 281
LENGTH = 25

try:
	for i in range(START_ROW, FINAL_ROW, LENGTH):
		thread.start_new_thread( getMyFilesBitch, (i, LENGTH) )
		print "Criando a " + str(i) + "th thread..."
	
except:
	print "Error: unable to start thread"
while 1:
	pass	
print("-------------------------------------------------------------------------------")