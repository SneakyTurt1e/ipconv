 #!/usr/bin/env python3

import argparse
import sys
def main():
	print('Origin IP:%s'%args.ip)
	BinIP = Decimal2Bin(args.ip)
	tmp = int(BinIP,2)
	start = Convert()
	if args.type == 'bin':
		print('Convert IP:%s'%tmp)
	elif args.type == 'oct':
		resqult = start.Bin2Octal(tmp)
		print('Convert IP:%s'%resqult)
	else:
		resqult = start.Bin2Hex(tmp)
		print('Convert IP:%s'%resqult)




def Decimal2Bin(ip):
	binip=''
	segment = ip.split(".")
	if len(segment) !=4:
		print('Incorrect IP format')
		sys.exit()
	else:
		for i in segment:
			binip += bin(int(i))[2:].zfill(8)
		return binip

class Convert:
	def Bin2Octal(self,BinIP):
		return str(oct(BinIP))[2:].zfill(12)
	def Bin2Hex(self,BinIP):
		return hex(BinIP)



description = '''
A script to convert Dot-decimal IP addresses to Hex Binary or Octal.
'''

epilog= "More Info: https://github.com/SneakyTurt1e/ipconv"

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description=description,epilog=epilog)

	parser.add_argument("-i", "--ip",dest='ip',help="IP Address[Do not support IPV6]",type=str,
					metavar='ip',required=True)

	parser.add_argument("-t","--type",dest='type',help="Convert type:bin oct hex ",type=str,choices=['bin', 'oct', 'hex'],
					metavar='type',required=True)

	args = parser.parse_args()

	main()
