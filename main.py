#!/usr/bin/python
import config
import myservicenow
import util
import sys
import json
import cgi
import base64
import getpass
#import cgitb
#from pprint import pprint
def web(form):
	# form = cgi.FieldStorage()
        #varleida = form.getvalue('test')
        url = form.getvalue('url')
        user = form.getvalue('user')
        passwd = form.getvalue('pass')
	
	return url,user,passwd

def main():
	# arguments: --url "URL"
	print "Content-type: text/html\n\n"
	# Read arguments from URL
	form = cgi.FieldStorage()
	if len(sys.argv) == 1:
	#varleida = form.getvalue('test')
		url,user,passwd = web(form)
	else:
	#user = form.getvalue('user')
	#passwd = form.getvalue('pass')
		valid_arguments='hu:' # Help; u + argument(URL)
		user = raw_input('user:')
		passwd = base64.b64encode(getpass.getpass('password:'));
	#print url,user,passwd
		url=util.Util.read_arguments(valid_arguments,sys.argv)
	my_util = util.Util()
	# Treat URL format
	instance_name,sys_id = my_util.treat_url(url)
	#my_util.treat_url(url)
	# print instance_name,sys_id
	#exit(0)
	# read config
	globalconfig=config.Config()
	#print globalconfig.debug
	#globalconfig.debugMsg(user+"--"+passwd)
	#myServiceN=myservicenow.MyServiceNow("dev12876","admin","UGljaHVycmluMzEk")
	myServiceN=myservicenow.MyServiceNow(instance_name,user,passwd)
	#myServiceN=myservicenow.MyServiceNow(instance_name,"admin","cGljaHVycmluYQ==")
	#myServiceN=myservicenow.MyServiceNow("dev23002","admin","ZFU1S253eyE9P3ot")
	data=myServiceN.getRecord('incident',sys_id)
	#pprint(data)
	print "Output..."
	print json.dumps(data,indent=2,sort_keys=True)
	exit(0)

if (__name__== '__main__'):
	main()

