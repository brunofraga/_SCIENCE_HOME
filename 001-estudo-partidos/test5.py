import csv
import urllib2
from time import gmtime, strftime
import time
import thread
from itertools import islice
import threading

import os



global CHUNK
global n_arquivos

CHUNK = 2048 * 4096  #6 Mb per read iteration

def getMyFilesBitch (initial_line, length, download_list):
	global CHUNK
	with open(download_list, 'rb') as csvfile:
		ith_line = 0
		for line in islice(csv.reader(csvfile), initial_line-1, initial_line-1 + length):
			ith_line = ith_line+1
			#dont know why but it go the reverse if i dont pick the last first
			array = line[-1].split(';')
			first_item = array[0]
			file_name = first_item.split('\r\n')[0]
			base_url = "http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/"
			url = base_url + file_name
			req = urllib2.urlopen(url)
			with open("downloads/"+file_name, 'wb') as f:
				while True:
					chunk = req.read(CHUNK)
					if not chunk: break
					f.write(chunk)
			f.close()



# A Pool Class is implemented to manage the threads
class Pool:
	def __init__(self, max_threads_alive):
		self.threads_to_run = []
		self.threads_running = []
		self.threads_executed = 0
		self.max_threads_alive = max_threads_alive
		
	
	def addThread(self,t):
		self.threads_to_run.append(t)
		
	def run(self):
		#try:
		self.t_run = threading.Thread(target=self.run_foo)
		self.t_run.start()
		time.sleep(0.25)
		self.t_check = threading.Thread(target=self.check_foo)
		self.t_check.start()
		time.sleep(0.25)
		#except:
		#	print "Error: unable to start thread"

	def run_foo(self):
		while len(self.threads_to_run) > 0:
			if len(self.threads_running) < self.max_threads_alive:
				t = self.threads_to_run[0]
				t.start()
				del self.threads_to_run[0]
				self.threads_running.append(t)
				time.sleep(0.25)
	
	def check_foo(self):
		while len(self.threads_running) > 0:
			executed = [t for t in self.threads_running if not t.isAlive()]
			self.threads_executed = self.threads_executed + len(executed)
			# Using list comprehension to remove the no longer running threads 
			# from the running array
			self.threads_running = [t for t in self.threads_running if t.isAlive()]
			
			
	def clear(self):
		"""
		for t in self.threads_running:
			if t.process is not None:
				t.process.terminate()
				t.process = None
		"""
		
		del self.threads_running[:]
		del self.threads_to_run[:]
		
		self.t_run = None
		self.t_check = None


LENGTH = 1
START_ROW = 1
FINAL_ROW = 884
LIMIT_TIME = 5 * 60# in seconds
ERROR_SIZE = 87 * 1000 # 87kb

i=1


# Creating the thread pool
p = Pool(100)

#starting clock 
#loaded_files_from_last_loop = 0
task_incomplete = True
t0 = time.clock()
deltaT = 0

file_list = 'temp.csv'
while task_incomplete:
	 # Adding threads to the pool
	for i in range(START_ROW, FINAL_ROW, LENGTH):
		p.addThread(threading.Thread(target=getMyFilesBitch, args=(i, LENGTH, file_list)))
	
	# Start threads
	p.run()
	print("-------------------------------------------------------------------------------")
	
	while len(p.threads_running) > 0 and deltaT < LIMIT_TIME :
		carregados = p.threads_executed
		print "[" + strftime("%H:%M:%S", gmtime()) + "] " + "Carregando " + str(len(p.threads_running)) + " arquivo(s)... " + str(carregados) +" de " + str(FINAL_ROW) + " carregados."
		deltaT = time.clock() - t0
		time.sleep(3);
	
	p.clear()
	err = [f for f in os.listdir("downloads/") if f.endswith(".zip")]
	err = [f for f in err if os.path.getsize("downloads/"+f)< ERROR_SIZE]
	
	# Are threre corrupted files?
	if len(err) > 0:
		with open("aux.csv", "wb") as f:
			writer = csv.writer(f,lineterminator='\n')
			for val in err:
				writer.writerow([val])
		file_list = "aux.csv"
		
		print "Existem " + str(len(err)) + " arquivos a serem carregados ainda. Reiniciando tarefa..."
		deltaT = 0;
		t0 = time.clock()
		
	else:
		task_incomplete = False
	
print("-------------------------------------------------------------------------------")
