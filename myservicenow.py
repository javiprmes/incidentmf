#!/usr/bin/python
""" ************************** data_servicenow.py  ****************************** 
    * Description: libraries and methods to operate with SN instances
    * Method: REST messages
    *****************************************************************************
"""
#from servicenow import ServiceNow
#from servicenow import Connection
import base64
from SOAPpy import SOAPProxy
import sys
import requests
import json
from bs4 import BeautifulSoup
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
		self.passwd = passwd
		self.url = 'https://'+instance+'.service-now.com/'
		# self.__login()
		#self.loginjson()

	def queryInstance(self, request_url, headers):
		""" Description
		Args: 

		Returns: 
		"""
		response = requests.get(request_url, auth=(self.user, base64.b64decode(self.passwd)), headers=headers)
		if response.status_code == 401:
			print "User/password incorrect?"
			exit(1)
		
		if response.status_code == 404:
			print "Record not found"
			exit(1)
		if response.status_code == 200:
			# Detect HTML code. In that case, instance returned a message such "Instance sleeping"
			if bool(BeautifulSoup(response.text,"html.parser").find()):
				print 'No json response(HTML instead).Is instance aslept?'
				exit(2)
			else:
				 return response
		print 'Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json()
		exit(2)

	def getRecord(self,table,sysid,query=''):
		""" Read a record from an instance function with types documented in the docstring.

		Args:
        		table (str): table to query.
        		sysid (str): record sys_id to search.
			query (str): extra parameters to the query

    	    	Returns:
        		json: the query result in json format

    		"""
		# Set the request parameters
 		#request_url = self.url+'/api/now/table/'+table+'/'+sysid
 		request_url = self.__buildrequest(table,sysid,query)
 		# request = self.url+'/'+table+'.do?JSONv2&sysparm_action=get&sysparm_sys_id='+sysid

		# Set proper headers
		headers = {"Content-Type":"application/json","Accept":"application/json"}
 
 		# Do the HTTP request
		response = self.queryInstance(request_url,headers)
 		# response = requests.get(request_url, auth=(self.user, self.passwd), headers=headers)
 		# print response.status_code
 		# Check for HTTP codes other than 200
 		#if response.status_code != 200: 
			#print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
     			#exit()
 		# Decode the JSON response into a dictionary and use the data
 		
		# TODO: search for pattern "Hibernate" in response.text
		# print 'Status:',response.text
		# try:
 		#print 'Status:',response.status_code,'Headers:',response.headers,'Response:',response.json()
 		#print('Cookies', response.cookies)
		data = json.loads(response.text)
		return data
		# Returns json response
		#return response.text
		#except ValueError:
		#	print "Is instance aslept?"
			
		# ServiceNow returns a JSON file :
		#{
  		# "result": [
    		# {
		# } 
		#]
		#}
		#return data['result']
		#return data

	def __buildrequest(self,table,sysid,query=''):
			
 		request_url = '%s/api/now/table/%s/%s' % (self.url, table, sysid)
		# Add extra query requests if specified
		if query != '':
			request_url = '%s?sysparm_query=%s' % (request_url, query)
		return request_url

#def query:
