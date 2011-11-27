from django.db import models
from datetime import datetime
from time import strptime, mktime
from photos.imageFunctions import get_exif, thumb

LOCATION_CHOICES = (
	('E', 'Elementary School'),
	('J', 'Junior High School'),
	('D', 'District Building'),
)

PERMISSION_CHOICES = (
	(1, 'Yes'),
	(2, 'Internal Use Only'),
	(3, 'No'),
)

class Location( models.Model ):
	name = models.CharField( max_length = 50 )
	type = models.CharField( max_length = 1, choices = LOCATION_CHOICES )

	def __unicode__(self):
		return self.name

class Photo( models.Model ):
	title = models.CharField( max_length=100, blank=True )
	image = models.ImageField( upload_to='photos' )
	location = models.ForeignKey( Location, blank=True, null=True )
	permissions = models.IntegerField( max_length = 1, choices = PERMISSION_CHOICES )
	description = models.TextField( blank=True )
	date_taken = models.DateField( blank=True, default='', null=True)
	date_uploaded = models.DateField( blank=True, default=datetime.now )
	
	def _thumb(self):
		p = self.image.url.split('/')
	 	f = 'thumb_' + p.pop()
	 	p.append(f)
	 	p = '/'.join(p)

		return p
	
	thumb = property(_thumb)
	
	def __unicode__(self):
		if self.title is None:
			return "Untitled"
		else:
			return self.title
	
 	def save( self, *args, **kwargs ):
 		if not self.title:
 			self.title = self.image.name.split('/')[-1] 
 		xf = get_exif( self.image )
 		if xf['DateTime']:
 			dt = datetime.fromtimestamp(
 				mktime(
 					strptime( xf['DateTime'], "%Y:%m:%d %H:%M:%S")
 				)
 			)
 			self.date_taken = dt
 		super( Photo, self ).save( *args, **kwargs )	
 		thumb(self.image)	
 		
 		
class Tag( models.Model ):
	image = models.ForeignKey( Photo )
	name = models.CharField( max_length=25 )
	
	def __unicode__(self):
		return self.name
