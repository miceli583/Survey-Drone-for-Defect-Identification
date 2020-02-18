from dronekit import connect

import sys
import csv

time = sys.argv[1]
print time

print('Connecting...')
vehicle = connect('tcp:127.0.0.1:5762')

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
#print alt
#print gim
#print ran
#print comp

with open('%s.csv' % time, mode='w') as telem_file:
    telem_writer = csv.writer(telem_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    telem_writer.writerow(['Lat','Lon','Alt','Gimbal','Rangefinder','Compass'])
    telem_writer.writerow([lat,lon,alt,gim,ran,comp])


vehicle.close()
print("Completed")