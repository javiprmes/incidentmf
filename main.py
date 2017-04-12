#!/usr/bin/python
import config
import myservicenow

def main():
	# read config
	globalconfig=config.Config()
	print globalconfig.debug
	globalconfig.debugMsg("Prueba")
	myServiceN=myservicenow.MyServiceNow("dev18917","admin","cGljaHVycmluYQ==")
	#myServiceN=myservicenow.MyServiceNow("dev23002","admin","ZFU1S253eyE9P3ot")
	data=myServiceN.getRecord('incident','29507d19db79b200e5e6d360cf9619b1')
	print data
	exit(0)

if (__name__== '__main__'):
	main()

