# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Photo.date_taken'
        db.alter_column('photos_photo', 'date_taken', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Photo.date_uploaded'
        db.alter_column('photos_photo', 'date_uploaded', self.gf('django.db.models.fields.DateField')())


    def backwards(self, orm):
        
        # Changing field 'Photo.date_taken'
        db.alter_column('photos_photo', 'date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Photo.date_uploaded'
        db.alter_column('photos_photo', 'date_uploaded', self.gf('django.db.models.fields.DateTimeField')())


    models = {
        'photos.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'date_taken': ('django.db.models.fields.DateField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'date_uploaded': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Location']", 'null': 'True', 'blank': 'True'}),
            'permissions': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
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
