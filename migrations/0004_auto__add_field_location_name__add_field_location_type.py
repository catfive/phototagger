# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Location.name'
        db.add_column('photos_location', 'name', self.gf('django.db.models.fields.CharField')(default=1, max_length=50), keep_default=False)

        # Adding field 'Location.type'
        db.add_column('photos_location', 'type', self.gf('django.db.models.fields.CharField')(default=1, max_length=1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Location.name'
        db.delete_column('photos_location', 'name')

        # Deleting field 'Location.type'
        db.delete_column('photos_location', 'type')


    models = {
        'photos.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['photos']
