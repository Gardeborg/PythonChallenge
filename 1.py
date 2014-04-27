import string

def decipher(text):
	return text.translate(str.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:26]+string.ascii_lowercase[0:2]))

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "http://www.pythonchallenge.com/pc/def/map.html"

print(decipher(text))
print(decipher(url))

#gives http://www.pythonchallenge.com/pc/def/ocr.html