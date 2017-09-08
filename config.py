import ConfigParser
import io
""" ********************** config.py *********************** 
    * Description: Read app configuration from file
    ********************************************************
"""

""" ************* function: NAME ******************
    * Description:
"""
""" SAMPLE
... [mysqld]
... user = mysql
... pid-file = /var/run/mysqld/mysqld.pid
... skip-external-locking
... old_passwords = 1
... skip-bdb
... skip-innodb
... """

class Config:
	#debug = False
	#conf = ''
	def __init__(self):
		self.conf = ConfigParser.RawConfigParser(allow_no_value=True)
		self.conf.read('config.txt')
		self.debug = (self.conf.get('Global','debug')=="1")
		#print self.debug
	def debugMsg(self,msg):
		if (self.debug):
			print "[[DEBUG]] "+msg
		
	
