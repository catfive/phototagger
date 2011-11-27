# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Photo.date_added'
        db.add_column('photos_photo', 'date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 10, 25), blank=True), keep_default=False)

        # Adding field 'Photo.date_taken'
        db.add_column('photos_photo', 'date_taken', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 10, 25), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Photo.date_added'
        db.delete_column('photos_photo', 'date_added')

        # Deleting field 'Photo.date_taken'
        db.delete_column('photos_photo', 'date_taken')


    models = {
        'photos.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Location']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'photos.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['photos']
