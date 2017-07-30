import getopt
import sys
import re

class Util:
	@staticmethod
    	def read_arguments(valid_arguments,argv):
		url = None
		try:
      			opts, args = getopt.getopt(argv[1:],valid_arguments)
   		except getopt.GetoptError:
      			print argv[0]+'[-h] -u URL<inputfile>'
      			sys.exit(2)
   		for opt, arg in opts:
      			if opt == '-h':
         			print argv[0]+'[-h] -u URL<inputfile>' 
         			sys.exit()
      			elif opt in ("-u"):
         			url = arg
				return url
			else:
            			assert False, "unhandled option"
		if url is None:
			print "Argument: -u URL is mandatory"
			sys.exit(2)

	def treat_url(self,url):
	#Example URL: (http(s)://)hi.service-now.com/hisp?id=form&table=incident&sys_id=b3d8ea30dbd436800e58fb651f9619f9
 	#Example URL: (http(s)://)hi.service-now.com/nav_to.do?uri=incident.do?sys_id=9d607398dbd6f2000e58fb651f96191a%26sysparm_view=partner_support

		buscaSysId = "(?:(?:(?:https?:\/\/))?(\S+\.service\-now\.com)\/(?:\S+[^&\?])?[\&|\?]sys_id=)?([\da-f]{32})(?:%\S+)?";
  		match = re.match(buscaSysId,url);
		if match is None:
			print "URL format not correct"
			exit(1)
  		return self.get_instance(match.group(1)), match.group(2)
		#return match[1], match[2]; # Base url,Sys_id
		
	def get_instance(self, url_base):
		return url_base.split('.')[0]	
