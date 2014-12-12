from ctypes import windll,byref,c_ulong
import sys
import optparse
import os.path

"""
Requires _ISource50.dll downloadbale from:
http://www.smalleranimals.com/isource.htm
http://www.smalleranimals.com/zips/ImgSource5/isource50.zip
"""

def pax_pwtry(isdll,password,paxfile):
	isdll._is5_Seek(paxfile, 0,0)
	return isdll._is5_ReadPAX(paxfile, byref(c_ulong(0)), byref(c_ulong(0)), 24, 0, password, 0) != 0 #=0 if password is incorrect

def main():
	usage = "Usage: %prog [options]"
	parser = optparse.OptionParser(usage=usage)
	parser.add_option('-p', '--password', action='store', dest='password', default='', help='Password to try')
	parser.add_option('-d', '--dictionary', action='store', dest='dictionary', default='', help='Specify dictionary (wordlist)')
	parser.add_option('-f', '--file', action='store', dest="file", default='', help='Chose PAX file to crack')
	options, args = parser.parse_args()
	
	if(options.file == ''):
		parser.error("No PAX file given. Please run 'python pickaxpwfinder.py --help' for usage instructions.")

	if(options.password == "" and options.dictionary == ""):
		parser.error("No password options specified. Please run 'pickaxpwfinder.py --help' for usage instructions.")
		
	if(not os.path.exists(options.file)):
		print "Specified PAX file can't be opened"
		sys.exit(0)

	#import ISource50.dll
	isdll = windll.LoadLibrary("_ISource50.dll")
	
	#open PAX file
	paxfile = isdll._is5_OpenFileSource(options.file)
	
	if (isdll._is5_GuessFileType(paxfile) == 9): #PAX filetype = 9
		if(options.password != ""):
			if(pax_pwtry(isdll,options.password,paxfile)): print "Password found: " + options.password
			else: print "Password not found"
		elif(options.dictionary != ""):
			try:
				f = open(options.dictionary,"r")
				linecount = 0
				for line in f:
					if(pax_pwtry(isdll,line.strip(),paxfile)):
						print "\nPassword found: " + line.strip()
						break
					linecount += 1
					progress = r"Number of passwords tried (to stop press CTRL+C): %10d" % (linecount)
					print progress + chr(8)*(len(progress)+1),
				f.close()
			except IOError:
				print "Couldn't open file: " + options.dictionary
				print "Password not found"
			except KeyboardInterrupt:
				f.close()
				print "\nExecution terminated"
				print "Password not found"
	else:
		print 'The given file is not a PAX file'
	
	isdll._is5_CloseSource(paxfile)

if __name__ == '__main__':
	main()
