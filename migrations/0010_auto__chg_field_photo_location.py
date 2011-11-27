# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Photo.location'
        db.alter_column('photos_photo', 'location_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.Location'], null=True))


    def backwards(self, orm):
        
        # Changing field 'Photo.location'
        db.alter_column('photos_photo', 'location_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['photos.Location']))


    models = {
        'photos.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 10, 26, 10, 7, 20, 794828)', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'default': "''", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Location']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'})
        },
        'photos.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['photos']
