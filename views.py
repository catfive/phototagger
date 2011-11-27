from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from photos.models import Photo, Location, Tag
from django import forms

class PhotoForm(forms.ModelForm):
 	photo_id = forms.IntegerField(
 		widget = forms.HiddenInput(),
 		label = '',
 	)
	
	class Meta:
		model = Photo
		exclude = ('image')
		widgets = {
			'title' : forms.TextInput(attrs={'class':'title'}),
		}

	def __init__(self, *args, **kwargs):
		super(PhotoForm, self).__init__(*args, **kwargs)
		if kwargs.has_key('instance'):
			self.initial['photo_id'] = kwargs['instance'].pk

def home( request ):
	p = Photo.objects.all()
	if request.method == 'POST':
		form = PhotoForm( request.POST )
		if form.is_valid():
			q = Photo.objects.get(pk = form.cleaned_data['photo_id'])
			f = PhotoForm(request.POST, instance = q)
			f.save()
			return HttpResponseRedirect('/')
		else:
			return HttpResponse( 'fail' )
	else:
		for photo in p:
			photo.form = PhotoForm( instance = photo )
	return render_to_response(
		'home.html',
		{
			'photos' : p,
		},
		context_instance = RequestContext( request ),
	)
