# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PhotographerRequest.modified_on'
        db.add_column(u'requests_photographerrequest', 'modified_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 8, 5, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PhotographerRequest.modified_on'
        db.delete_column(u'requests_photographerrequest', 'modified_on')


    models = {
        u'requests.photographerrequest': {
            'Meta': {'object_name': 'PhotographerRequest'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_needed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '256'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'follow_up': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fulfilled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'max_price': ('django.db.models.fields.IntegerField', [], {'default': '50'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'payment_made': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'payment_received': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['requests']