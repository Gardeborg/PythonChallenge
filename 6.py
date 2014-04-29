# import sys

# def myOpener(filename):
#     with open(filename, 'r') as f:
#         for line in f:
#             print(line)
#             number = line.split()[-1]
#             f.close()
            
#             #wait = input()
#             myOpener(createFileName(number))

# def createFileName(number):
#     if number == 'comments.':
#         wait = input()
#     return path + number + '.txt'

# path = "/Users/kristofer/Downloads/channel/"

# print(myOpener(createFileName(sys.argv[1])))
import zipfile

zip = zipfile.ZipFile(open('channel.zip'))

nothing = '90052'
comments = [] #The answer is *in* the zip..
while True:
    raw_data = zip.read(file % nothing)
    print(raw_data)
    nothing = int(raw_data.split()[-1])
    comments.append(zip.getinfo(file % nothing).comment)

print(''.join(comments))
