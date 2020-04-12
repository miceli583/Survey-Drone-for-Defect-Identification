# -------FileMerger-------


import sys
import csv

import os.path
from os import path

from numpy import array
import time

path1 = "GeoDim/TD_ResultsTestInput.csv"
# path1 = actual path
path2 = "GeoDim/YoloDetection_ResultsTestInput.csv"
# path2 = actual path

#print(os.path.exists(path1))
#print(os.path.exists(path2))

data = []

with open(path2, mode='r') as detection_file:
    detection_reader = csv.reader(detection_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    next(detection_file)
    for row in detection_reader:
        # row = [image,image_path,xmin,ymin,xmax,ymax,label,confidence,x_size,y_size]
        data.append(row)
        
i = 0
for line in data:
    with open(path1, mode='r') as telem_file:
        telem_reader = csv.reader(telem_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        next(telem_file)
    
        for row in telem_reader:
            # row = [time,lat,lon,alt,gim,ran,comp]            
           
            if line[0] == (row[0] + ".jpg"):
                data[i] = row + data[i]
                break
    i+=1            


with open('%s.csv' %('GeoDim/GeoDim/' + str(time.time())), mode='wb') as merged_file:
    merger = csv.writer(merged_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  
    merger.writerow(['Time','Lat','Lon','Alt','Gimbal','Rangefinder','Compass','image','image_path','xmin','ymin','xmax','ymax','label','confidence','x_size','y_size'])
    for line in data:
        merger.writerow(line)