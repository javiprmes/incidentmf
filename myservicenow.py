#!/usr/bin/python
""" ************************** data_servicenow.py  ****************************** 
    * Description: libraries and methods to operate with SN instances
    *****************************************************************************
"""
#from servicenow import ServiceNow
#from servicenow import Connection
import base64
from SOAPpy import SOAPProxy
import sys
import requests
import json
""" ************* function: NAME ******************
    * Description:
"""
""" ************* function: connect ******************
    * Description: *
"""

""" ************* Class: ServiceNowMng ******************
    * Description: Class to manage the ServiceNow instance connection *
"""
class MyServiceNow:

	def __init__(self,instance,user,passwd):
		self.instance = instance
		self.user = user
		self.passwd = base64.b64decode(passwd)
		self.url = 'https://'+instance+'.service-now.com/' 
		#self.loginjson()

	def __login(self):
		#self.conn = Connection.Auth(username='javier.messeri@fruitionpartners.eu', password='cGljaHVycmluYQ==', instance='hi', api='JSONv2')
		#self.conn = Connection.Auth(username='javier.messeri@fruitionpartners.eu', password=base64.b64decode('cGljaHVycmluYQ=='), instance='hi', api='JSONv2')
		proxy = 'https://%s:%s@%s.service-now.com/incident.do?SOAP' % (self.user, self.passwd, self.instance)
        	namespace = 'http://www.service-now.com/'
        	server = SOAPProxy(proxy, namespace)
		response = server.get(sys_id='9c573169c611228700193229fff72400')
		for each in response:
			print each
	
	def getRecord(self,table,sysid,query=''):
		# Set the request parameters
 		#request_url = self.url+'/api/now/table/'+table+'/'+sysid
 		request_url = self.__buildrequest(table,sysid,query)
 		# request = self.url+'/'+table+'.do?JSONv2&sysparm_action=get&sysparm_sys_id='+sysid

		# Set proper headers
		headers = {"Content-Type":"application/json","Accept":"application/json"}
 
 		# Do the HTTP request
 		response = requests.get(request_url, auth=(self.user, self.passwd), headers=headers)
 
 		# Check for HTTP codes other than 200
 		if response.status_code != 200: 
			print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
     			exit()
 		# Decode the JSON response into a dictionary and use the data
 		#print('Status:',response.status_code,'Headers:',response.headers,'Response:',response.json())
 		#print('Cookies', response.cookies)
		data = json.loads(response.text)
		# ServiceNow returns a JSON file :
		#{
  		# "result": [
    		# {
		# } 
		#]
		#}
		return data['result']

	def __buildrequest(self,table,sysid,query=''):
			
 		request_url = '%s/api/now/table/%s/%s' % (self.url, table, sysid)
		if query != '':
			request_url = '%s?sysparm_query=%s' % (request_url, query)

		return request_url

#def query:
