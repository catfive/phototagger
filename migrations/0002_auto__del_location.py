# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Location'
        db.delete_table('photos_location')


    def backwards(self, orm):
        
        # Adding model 'Location'
        db.create_table('photos_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('photos', ['Location'])


    models = {
        
    }

    complete_apps = ['photos']
