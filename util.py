class Util:
	@staticmethod
    	def read_arguments(argv):
		try:
      			opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   		except getopt.GetoptError:
      			print 'test.py -i <inputfile> -o <outputfile>'
      			sys.exit(2)
   		for opt, arg in opts:
      		if opt == '-h':
         		print 'test.py -i <inputfile> -o <outputfile>'
         		sys.exit()
      		elif opt in ("-i", "--ifile"):
         		inputfile = arg
      		elif opt in ("-o", "--ofile"):
         		outputfile = arg