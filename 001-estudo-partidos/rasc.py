import csv
import urllib2
from time import gmtime, strftime
import time
import thread
from itertools import islice
import threading

import os


ERROR_SIZE = 88 * 1000



err = [f for f in os.listdir("downloads/") if f.endswith(".zip")]
err = [f for f in err if os.path.getsize("downloads/"+f)< ERROR_SIZE]

with open("aux.csv", "wb") as f:
    writer = csv.writer(f,lineterminator='\n')
    for val in err:
        writer.writerow([val])