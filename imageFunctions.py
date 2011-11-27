import Image
import os
from PIL.ExifTags import TAGS

def get_exif( path ):
	i = Image.open( path )
	if hasattr( i, '_getexif' ):
		exif = i._getexif() or None
		tags = {}
		for tag, value in exif.items():
			d = TAGS.get( tag, tag )
			tags[d] = value
		return tags
 	
def thumb( image ):
 	i = Image.open( image.path )
 	if image.width > image.height:	
 		ratio = float(image.width) / float(image.height)
 		size = (400, 400/ratio)
 	else:
 		ratio = float(image.height) / float(image.width)
 		size = (400/ratio, 400)
 	t = i.resize( size, Image.ANTIALIAS )
 	p = image.path.split('/')
 	f = 'thumb_' + p.pop()
 	p.append(f)
 	p = '/'.join(p)
	t.save(p) 