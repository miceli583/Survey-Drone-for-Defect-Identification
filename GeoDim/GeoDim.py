import os
files = os.listdir('GeoDim/GeoDim/')

import sys
import csv

import math
import time

def GeoDim(row):
    
    lat = float(row[1])
    lon = float(row[2])
    alt = float(row[3])
    #gimbal angle given as negative
    gim = float(row[4])
    dis = float(row[5])
    com = float(row[6])

    xmin = float(row[9])
    xmax = float(row[11])
    px = xmax - xmin

    ymin = float(row[10])
    ymax = float(row[12])
    py = ymax-ymin

    #Earth Radius = 6378100

    #feature altitude
    Falt = alt - dis*math.sin(-1*gim)
    #feature latitude
    Flat = lat + 180*dis*math.cos(-1*gim)*math.cos(com)/(math.pi*6378100)
    #feature longitude
    Flon = lon + 180*dis*math.cos(-1*gim)*math.sin(com)/(math.pi*6378100)
    #feature horizontal dimension
    Xdim = 0.0058313294*dis*px
    #feature vertical dimension
    Ydim = 0.0058313294*dis*py
    #SCALING FACTOR SHOULD BE TUNED AFTER TESTING CAMERA FOV AND RANGEFINDER

    result = [row[7],row[8],row[13],row[14],Flat,Flon,Falt,xmin,ymin,xmax,ymax,Xdim,Ydim]
    return result

data = []


for entry in files:
    with open('GeoDim/GeoDim/' + entry, mode='r') as readable_file:
        next(readable_file)
        GD_reader = csv.reader(readable_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in GD_reader:
            data.append(GeoDim(row))



header = ['image','image_path','label','confidence','FeatureLat','FeatureLon','FeatureAlt','xmin','ymin','xmax','ymax','Xdim','Ydim']

with open('%s.csv' %('FullResults/Res_' + str(time.time())), mode='wb') as results:
    writer = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  
    writer.writerow(header)
    for line in data:
        writer.writerow(line)
