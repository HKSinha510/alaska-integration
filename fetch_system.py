'''import psutil
from datetime import datetime


boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
cpufreq = psutil.cpu_freq()
svmem = psutil.virtual_memory()
swap = psutil.swap_memory()
disk_io = psutil.disk_io_counters()
net_io = psutil.net_io_counters()

#

import subprocess
 
# traverse the info
Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
new = []
 
# arrange the string into clear info
for item in Id:
    new.append(str(item.split("\r")[:-1]))
for i in new:
    print(i[2:-2])'''

import wmi

hwmon = wmi.WMI(namespace="D:\Download\LibreHardwareMonitor-net472")
sensors = hwmon.Sensor(SensorType="Control")

for s in sensors:
	print(s)