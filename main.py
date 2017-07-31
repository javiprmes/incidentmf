#!/usr/bin/python
import config
import myservicenow
import util
import sys
import json
import cgi
import base64
import getpass
#from pprint import pprint

def ask_user_and_password():
	# Ask user for user and password from command line
	user = raw_input('user:')
	passwd = base64.b64encode(getpass.getpass('password:'));
	return user,passwd

def treat_response(response):
	# Array with parameters
	items = [['number'],['company','link'],['short_description'],['caller_id','link'],['opened_by','link']]
	for item in items:
		#if isinstance(item,list): 
		#	continue
		print response['result'][item[0]]
	#for child in response:
	#	print child
	#TODO: get company name:
	# url = 'https://INSTANCE.service-now.com/api/now/table/core_company/SYS_ID?sysparm_fields=name'
	

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
	# If only one parameter, call was made using a URL ['/usr/local/cgi-bin/...','','']
	if len(sys.argv) == 1:
	#varleida = form.getvalue('test')
		url,user,passwd = web(form)
	else: # Check command line arguments
		valid_arguments='hu:' # Help; u + argument(URL)
		# Ask user for user and password from command line
		# user,passwd = ask_user_and_password()
		user = "javier.messeri@fruitionpartners.eu"
		passwd = base64.b64encode("6QjKrKznQu9X!")
		# Call util to check parameter
		url=util.Util.read_arguments(valid_arguments,sys.argv)
	my_util = util.Util()
	# Treat URL format
	instance_name,sys_id = my_util.treat_url(url)
	globalconfig=config.Config()
	#globalconfig.debugMsg(user+"--"+passwd)
	#myServiceN=myservicenow.MyServiceNow("dev12876","admin","UGljaHVycmluMzEk")
	myServiceN=myservicenow.MyServiceNow(instance_name,user,passwd)
	#myServiceN=myservicenow.MyServiceNow(instance_name,"admin","cGljaHVycmluYQ==")
	#myServiceN=myservicenow.MyServiceNow("dev23002","admin","ZFU1S253eyE9P3ot")
	data=myServiceN.getRecord('incident',sys_id)
	#pprint(data)
	#print "Output..."
	print json.dumps(data,indent=2,sort_keys=True)
	treat_response(data)
	exit(0)

if (__name__== '__main__'):
	main()

