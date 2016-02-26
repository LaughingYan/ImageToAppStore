# ImageToAppStore
# By Laughing.Yan, 02/26/2016, 1st python program
# user guide: 
# 1. input : some image in folder 'source_Image'
# 2. output: all size image to upload 'https://itunesconnect.apple.com'
# 3. need  : PIL


import os,sys
#import Image
#import PIL
from PIL import Image
_imaging = Image.core

isScreenPortrait = 1
outputFormat = [ '.png', 'PNG' ]

def generate_all_size(pic):
        global outputFileInfo
	try:
		im = Image.open('source_Image'+ os.sep +pic)
		#im.show()
                for fileInfo in outputFileInfo:
                        if isScreenPortrait :
                                width  = fileInfo[1][0];
                                height = fileInfo[1][1];                                
                        else :                                        
                                width  = fileInfo[1][1];
                                height = fileInfo[1][0];
                                        
                        out = im.resize( (width, height) )
                        _index = pic.rfind('.')
                	out.save( fileInfo[0]+ os.sep  + pic[0:_index] + outputFormat[0], outputFormat[1] )
	finally:
		print 'generate_all_size :'+pic
		

outputFileInfo = [[ 'iphone4_4s', [ 640, 960  ] ], \
                  [ 'iphone5_5s', [ 640, 1136 ] ],\
                  [ 'iphone6_6s', [ 750, 1334 ] ],\
                  [ 'ipad',       [ 768, 1024 ] ],\
                  [ 'ipadPro',    [ 2048,2732 ] ] ]  

all = os.listdir( 'source_Image'+ os.sep  )
pics = []
for fileInfo in outputFileInfo:
        if not os.path.exists(fileInfo[0]):
                os.mkdir(fileInfo[0]);
for file in os.listdir('source_Image'+ os.sep ):
	if os.path.isfile('source_Image'+ os.sep +file):
                pics.append(file)
print pics
for pic in pics:
        generate_all_size(pic)
