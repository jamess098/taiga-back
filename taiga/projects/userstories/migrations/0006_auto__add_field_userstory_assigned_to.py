# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserStory.assigned_to'
        db.add_column('userstories_userstory', 'assigned_to',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, default=None, related_name='userstories_assigned_to_me', null=True, to=orm['users.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserStory.assigned_to'
        db.delete_column('userstories_userstory', 'assigned_to_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'domains.domain': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Domain'},
            'default_language': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '20'}),
            'domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'public_register': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'scheme': ('django.db.models.fields.CharField', [], {'max_length': '60', 'default': 'None', 'null': 'True'})
        },
        'milestones.milestone': {
            'Meta': {'ordering': "['project', 'created_date']", 'unique_together': "(('name', 'project'),)", 'object_name': 'Milestone'},
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'disponibility': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'default': '0.0', 'null': 'True'}),
            'estimated_finish': ('django.db.models.fields.DateField', [], {'blank': 'True', 'default': 'None', 'null': 'True'}),
            'estimated_start': ('django.db.models.fields.DateField', [], {'blank': 'True', 'default': 'None', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_milestones'", 'null': 'True', 'to': "orm['users.User']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'milestones'", 'to': "orm['projects.Project']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'blank': 'True', 'max_length': '250'})
        },
        'projects.issuestatus': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'IssueStatus'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'#999999'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issue_statuses'", 'to': "orm['projects.Project']"})
        },
        'projects.issuetype': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'IssueType'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'#999999'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issue_types'", 'to': "orm['projects.Project']"})
        },
        'projects.membership': {
            'Meta': {'ordering': "['project', 'role']", 'object_name': 'Membership'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'default': 'None', 'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships'", 'to': "orm['projects.Project']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memberships'", 'to': "orm['users.Role']"}),
            'token': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': 'None', 'max_length': '60', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'default': 'None', 'related_name': "'memberships'", 'null': 'True', 'to': "orm['users.User']"})
        },
        'projects.points': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'Points'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'points'", 'to': "orm['projects.Project']"}),
            'value': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'default': 'None', 'null': 'True'})
        },
        'projects.priority': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'Priority'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'#999999'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'priorities'", 'to': "orm['projects.Project']"})
        },
        'projects.project': {
            'Meta': {'ordering': "['name']", 'object_name': 'Project'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'default_issue_status': ('django.db.models.fields.related.OneToOneField', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'related_name': "'+'", 'to': "orm['projects.IssueStatus']", 'unique': 'True', 'null': 'True'}),
            'default_issue_type': ('django.db.models.fields.related.OneToOneField', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'related_name': "'+'", 'to': "orm['projects.IssueType']", 'unique': 'True', 'null': 'True'}),
            'default_points': ('django.db.models.fields.related.OneToOneField', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'related_name': "'+'", 'to': "orm['projects.Points']", 'unique': 'True', 'null': 'True'}),
            'default_priority': ('django.db.models.fields.related.OneToOneField', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'related_name': "'+'", 'to': "orm['projects.Priority']", 'unique': 'True', 'null': 'True'}),
            'default_question_status': ('django.db.models.fields.related.OneToOneField', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'related_name': "'+'", 'to': "orm['projects.QuestionStatus']", 'unique': 'True', 'null': 'True'}),
            'default_severity': ('django.db.models.fields.related.OneToOneField', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'related_name': "'+'", 'to': "orm['projects.Severity']", 'unique': 'True', 'null': 'True'}),
            'default_task_status': ('django.db.models.fields.related.OneToOneField', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'related_name': "'+'", 'to': "orm['projects.TaskStatus']", 'unique': 'True', 'null': 'True'}),
            'default_us_status': ('django.db.models.fields.related.OneToOneField', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'related_name': "'+'", 'to': "orm['projects.UserStoryStatus']", 'unique': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'default': 'None', 'related_name': "'projects'", 'null': 'True', 'to': "orm['domains.Domain']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_issue_ref': ('django.db.models.fields.BigIntegerField', [], {'default': '1', 'null': 'True'}),
            'last_task_ref': ('django.db.models.fields.BigIntegerField', [], {'default': '1', 'null': 'True'}),
            'last_us_ref': ('django.db.models.fields.BigIntegerField', [], {'default': '1', 'null': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'through': "orm['projects.Membership']", 'symmetrical': 'False', 'related_name': "'projects'", 'to': "orm['users.User']"}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_projects'", 'to': "orm['users.User']"}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'blank': 'True', 'max_length': '250'}),
            'tags': ('picklefield.fields.PickledObjectField', [], {'blank': 'True'}),
            'total_milestones': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'default': '0', 'null': 'True'}),
            'total_story_points': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True'}),
            'videoconferences': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '250', 'null': 'True'})
        },
        'projects.questionstatus': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'QuestionStatus'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'#999999'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'question_status'", 'to': "orm['projects.Project']"})
        },
        'projects.severity': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'Severity'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'#999999'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'severities'", 'to': "orm['projects.Project']"})
        },
        'projects.taskstatus': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'TaskStatus'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'#999999'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'task_statuses'", 'to': "orm['projects.Project']"})
        },
        'projects.userstorystatus': {
            'Meta': {'ordering': "['project', 'order', 'name']", 'unique_together': "(('project', 'name'),)", 'object_name': 'UserStoryStatus'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'#999999'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'us_statuses'", 'to': "orm['projects.Project']"})
        },
        'users.role': {
            'Meta': {'ordering': "['order', 'slug']", 'unique_together': "(('slug', 'project'),)", 'object_name': 'Role'},
            'computable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'roles'", 'to': "orm['auth.Permission']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roles'", 'to': "orm['projects.Project']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'blank': 'True', 'max_length': '250'})
        },
        'users.user': {
            'Meta': {'ordering': "['username']", 'object_name': 'User'},
            'color': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "'#669933'", 'max_length': '9'}),
            'colorize_tags': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'default_language': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '20'}),
            'default_timezone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'notify_changes_by_me': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notify_level': ('django.db.models.fields.CharField', [], {'default': "'all_owned_projects'", 'max_length': '32'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'blank': 'True', 'max_length': '500', 'null': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': 'None', 'max_length': '200', 'null': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'userstories.rolepoints': {
            'Meta': {'ordering': "['user_story', 'role']", 'unique_together': "(('user_story', 'role'),)", 'object_name': 'RolePoints'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'role_points'", 'to': "orm['projects.Points']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'role_points'", 'to': "orm['users.Role']"}),
            'user_story': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'role_points'", 'to': "orm['userstories.UserStory']"})
        },
        'userstories.userstory': {
            'Meta': {'ordering': "['project', 'order']", 'unique_together': "(('ref', 'project'),)", 'object_name': 'UserStory'},
            'assigned_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'default': 'None', 'related_name': "'userstories_assigned_to_me'", 'null': 'True', 'to': "orm['users.User']"}),
            'blocked_note': ('django.db.models.fields.TextField', [], {'blank': 'True', 'default': "''"}),
            'client_requirement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'finish_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'related_name': "'user_stories'", 'null': 'True', 'default': 'None', 'to': "orm['milestones.Milestone']"}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'related_name': "'owned_user_stories'", 'null': 'True', 'to': "orm['users.User']"}),
            'points': ('django.db.models.fields.related.ManyToManyField', [], {'through': "orm['userstories.RolePoints']", 'symmetrical': 'False', 'related_name': "'userstories'", 'to': "orm['projects.Points']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_stories'", 'to': "orm['projects.Project']"}),
            'ref': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True', 'blank': 'True', 'default': 'None', 'null': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'on_delete': 'models.SET_NULL', 'blank': 'True', 'related_name': "'user_stories'", 'null': 'True', 'to': "orm['projects.UserStoryStatus']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'tags': ('picklefield.fields.PickledObjectField', [], {'blank': 'True'}),
            'team_requirement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'watchers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'watched_us'", 'null': 'True', 'to': "orm['users.User']"})
        }
    }

    complete_apps = ['userstories']