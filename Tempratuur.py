import wmi
import time
import requests

def avg(value_list):
	num = 0
	length = len(value_list)
	for val in value_list:
		num += val
	return num/length
    
    
w = wmi.WMI(namespace="root\\OpenHardwareMonitor")

while True: #Loop
	time.sleep(1)
	sensors = w.Sensor()
	cpu_temp = []
	gpu_temp = []
	for sensor in sensors:
		if sensor.SensorType==u'Temperature' and 'CPU' in sensor.Name: #Haalt tempratuur van de CPU op
			cpu_temp = sensor.Value
		elif sensor.SensorType==u'Temperature' and 'GPU' in sensor.Name: #Haalt tempratuur van de GPU op
			gpu_temp = sensor.Value
	#urllib2.urlopen(urllib2.Request('http://10.80.17.1/smartthings.py', urllib.urlencode({'cpu_temp':cpu_temp,'gpu_temp':gpu_temp})))
	#connection = httplib.HTTPConnection('http://10.80.17.1')
	#headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	#connection.request('POST', 'smartthings.py', urllib.urlencode({'cpu_temp':cpu_temp,'gpu_temp':gpu_temp}), headers)
	#connection.getresponse()
	requests.post('http://10.80.17.1/smartthings.py', data={'cpu_temp':cpu_temp,'gpu_temp':gpu_temp})
	print(cpu_temp)
