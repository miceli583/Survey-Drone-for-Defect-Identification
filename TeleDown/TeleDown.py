# -------TeleDown-------

from dronekit import connect

import sys
import csv

import os.path
from os import path

time = sys.argv[1]
path = "C:/Users/micel/Documents/Spring 2020/Capstone/survey_drone/TeleDown/TD_Results"


print('Connecting...')
#vehicle = connect('tcp:127.0.0.1:5762')
vehicle = connect('com8', baud=57600)

vehicle.wait_ready('autopilot_version')
print('Autopilot version: %s'%vehicle.version)

lat = vehicle.location.global_frame.lat #from GPS
lon = vehicle.location.global_frame.lon #from GPS
alt = vehicle.location.global_frame.alt #from Barometer (relative to sea level)
gim = vehicle.gimbal.pitch
ran = vehicle.rangefinder.distance
comp = vehicle.heading

#print lat
#print lon
#print s
#print gim
#print ran
#print comp
if os.path.exists(path + ".csv") ==  False:
    with open('%s.csv' % path, mode='wb') as telem_file:
        telem_writer = csv.writer(telem_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
        telem_writer.writerow(['Time','Lat','Lon','Alt','Gimbal','Rangefinder','Compass'])
        telem_writer.writerow([time,lat,lon,alt,gim,ran,comp])
else:
    with open('%s.csv' % path, mode='ab') as telem_file:
        telem_writer = csv.writer(telem_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
        telem_writer.writerow([time,lat,lon,alt,gim,ran,comp])

vehicle.close()
print("Completed")