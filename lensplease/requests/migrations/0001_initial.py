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
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=256)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('max_price', self.gf('django.db.models.fields.IntegerField')()),
            ('date_needed', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('follow_up', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fulfilled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('payment_received', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('payment_made', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'requests', ['PhotographerRequest'])


    def backwards(self, orm):
        # Deleting model 'PhotographerRequest'
        db.delete_table(u'requests_photographerrequest')


    models = {
        u'requests.photographerrequest': {
            'Meta': {'object_name': 'PhotographerRequest'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_needed': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '256'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'follow_up': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fulfilled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'max_price': ('django.db.models.fields.IntegerField', [], {}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'payment_made': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'payment_received': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['requests']