# def dec(number):
	# if number is 0:
		# return 0
	# return number + dec(number-1)
	
# print(dec(10))

import sys
from urllib.request import urlopen
	
def parseUrl(url):
	response = urlopen(url)
	html = response.read()
	something = html.decode(encoding='UTF-8')
	split_list = str(something).rsplit(' ')
	# Get the last item
	number = split_list[-1]
	#parseUrl(constructUrl(number))
	print(something)
	parseUrl(constructUrl(number))
	
def constructUrl(number):
	return url + number

print(sys.argv[1])

url	= 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
print(parseUrl(constructUrl(str(sys.argv[1]))))