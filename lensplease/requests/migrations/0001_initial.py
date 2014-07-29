# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PhotographerRequest'
        db.create_table(u'requests_photographerrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=256)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('max_price', self.gf('django.db.models.fields.IntegerField')()),
            ('date_needed', self.gf('django.db.models.fields.DateField')()),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'requests', ['PhotographerRequest'])


    def backwards(self, orm):
        # Deleting model 'PhotographerRequest'
        db.delete_table(u'requests_photographerrequest')


    models = {
        u'requests.photographerrequest': {
            'Meta': {'object_name': 'PhotographerRequest'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_needed': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_price': ('django.db.models.fields.IntegerField', [], {}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['requests']