import sys
import httplib, urllib
import re
import random

#	client = httplib.HTTPConnection('www.random.org:80')

#	client.request('GET', '/integers/?num=10&min=1&max=100&col=1&base=10&format=plain&rnd=new')

#	res = client.getresponse()

#	rawns = map(int, res.read().split())
#	print rawns

#	client.request('GET', '/quota/?format=plain')
#	print "Bits remaining: ", client.getresponse().read()
#	client.close()

def roll(multi, face, mod):
	#just going with a rand implementation for now to conserve bandwidth
	return [random.randint(1, face)+mod for x in range(multi)]

def rollSum(results, args):
	return sum(results)

def rollCount(results, args):
	pass

def rollCountAbove(results, args):
	pass

def rollCountBelow(results, args):
	pass

def rollShow(results, args):
	pass

def rollSort(results, args):
	pass

def showHelp(results, args):
	pass

def unrecognizedInput(results, args):
	pass

def main():
	rolex = re.compile('(\d*)d(\d+)([+-]\d+)?', re.I)
	done = False
	lastrs = 'roll'
	lastroll = []
	while(not done):
		prompt = raw_input("[%s]>> " % lastrs)

		if(prompt == 'bye'): break

		matches = rolex.match(prompt)
		if(matches):		
			multi = int(matches.group(1) if matches.group(1) != '' else 1)
			face = int(matches.group(2))
			mod = int(matches.group(3) if matches.group(3) is not None else 0 )
			lastroll = roll(multi, face, mod)
			print lastroll
			lastrs = "{0}d{1}{2:+}".format(multi, face, mod)
		else:
			raw_command = prompt.split()
			command = raw_command[0]
			print {
				'sum' 			: rollSum,
				'count'			: rollCount,
				'countabove'	: rollCountAbove,
				'countbelow'	: rollCountBelow,
				'show'			: rollShow,
				'sort'			: rollSort,
				'help'			: showHelp,
			}.get(command, unrecognizedInput)(lastroll, raw_command[1:])

if __name__ == "__main__":
	main()