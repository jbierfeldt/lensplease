# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PhotographerRequest.satisfied'
        db.add_column(u'requests_photographerrequest', 'satisfied',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PhotographerRequest.satisfied'
        db.delete_column(u'requests_photographerrequest', 'satisfied')


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
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'satisfied': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['requests']