# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Renaming field 'Website.eml_reg_plaintext'
        db.rename_column(u'front_website', 'eml_reg_plaintext', 'eml_registration_plaintext')

        # Deleting field 'Website.pw_salted'
        db.delete_column(u'front_website', 'pw_salted')

        # Deleting field 'Website.pw_plaintext'
        db.delete_column(u'front_website', 'pw_plaintext')

        # Deleting field 'Website.pw_alphabet_size'
        db.delete_column(u'front_website', 'pw_alphabet_size')

        # Deleting field 'Website.pw_hashfunction'
        db.delete_column(u'front_website', 'pw_hashfunction')

        # Deleting field 'Website.pw_min_length'
        db.delete_column(u'front_website', 'pw_min_length')

        # Adding field 'Website.alphabet_limited'
        db.add_column(u'front_website', 'alphabet_limited',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Website.eml_recover_plaintext'
        db.add_column(u'front_website', 'eml_recover_plaintext',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Website.securitywidget'
        db.add_column(u'front_website', 'securitywidget',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Changing field 'Website.pw_max_length'
        db.alter_column(u'front_website', 'pw_max_length', self.gf('django.db.models.fields.SmallIntegerField')(default=2))

    def backwards(self, orm):
        # Renaming field 'Website.eml_registration_plaintext'
        db.rename_column(u'front_website', 'eml_registration_plaintext', 'eml_reg_plaintext')

        # Adding field 'Website.pw_salted'
        db.add_column(u'front_website', 'pw_salted',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Website.pw_plaintext'
        db.add_column(u'front_website', 'pw_plaintext',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Website.pw_alphabet_size'
        db.add_column(u'front_website', 'pw_alphabet_size',
                      self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Website.pw_hashfunction'
        db.add_column(u'front_website', 'pw_hashfunction',
                      self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Website.pw_min_length'
        db.add_column(u'front_website', 'pw_min_length',
                      self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Website.alphabet_limited'
        db.delete_column(u'front_website', 'alphabet_limited')

        # Deleting field 'Website.eml_recover_plaintext'
        db.delete_column(u'front_website', 'eml_recover_plaintext')

        # Deleting field 'Website.securitywidget'
        db.delete_column(u'front_website', 'securitywidget')


        # Changing field 'Website.pw_max_length'
        db.alter_column(u'front_website', 'pw_max_length', self.gf('django.db.models.fields.SmallIntegerField')(null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'front.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'front.website': {
            'Meta': {'object_name': 'Website'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'eml_recover_plaintext': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'eml_registration_plaintext': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'eml_remind_plaintext': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pw_alphabet_size_restricted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pw_max_length': ('django.db.models.fields.SmallIntegerField', [], {}),
            'securitywidget': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tls': ('django.db.models.fields.SmallIntegerField', [], {}),
            'twofactor': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['front']
