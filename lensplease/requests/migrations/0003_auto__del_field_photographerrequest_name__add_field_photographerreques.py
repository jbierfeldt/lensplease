# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PhotographerRequest.name'
        db.delete_column(u'requests_photographerrequest', 'name')

        # Adding field 'PhotographerRequest.first_name'
        db.add_column(u'requests_photographerrequest', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='sdf', max_length=256),
                      keep_default=False)

        # Adding field 'PhotographerRequest.last_name'
        db.add_column(u'requests_photographerrequest', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='sdlkfj', max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PhotographerRequest.name'
        db.add_column(u'requests_photographerrequest', 'name',
                      self.gf('django.db.models.fields.CharField')(default="<type 'str'>", max_length=256),
                      keep_default=False)

        # Deleting field 'PhotographerRequest.first_name'
        db.delete_column(u'requests_photographerrequest', 'first_name')

        # Deleting field 'PhotographerRequest.last_name'
        db.delete_column(u'requests_photographerrequest', 'last_name')


    models = {
        u'requests.photographerrequest': {
            'Meta': {'object_name': 'PhotographerRequest'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_needed': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '256'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'max_price': ('django.db.models.fields.IntegerField', [], {}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'satisfied': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['requests']