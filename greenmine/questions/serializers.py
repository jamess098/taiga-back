# -*- coding: utf-8 -*-

from rest_framework import serializers

from greenmine.questions.models import Question
from greenmine.scrum.serializers import PickleField

import reversion


class QuestionSerializer(serializers.ModelSerializer):
    tags = PickleField()
    comment = serializers.SerializerMethodField('get_comment')
    history = serializers.SerializerMethodField('get_history')

    class Meta:
        model = Question
        fields = ()

    def get_comment(self, obj):
        return ''

    def get_questions_diff(self, old_question_version, new_question_version):
        old_obj = old_question_version.field_dict
        new_obj = new_question_version.field_dict

        diff_dict = {
            'modified_date': new_obj['modified_date'],
            'by': old_question_version.revision.user,
            'comment': old_question_version.revision.comment,
        }

        for key in old_obj.keys():
            if key == 'modified_date':
                continue

            if old_obj[key] == new_obj[key]:
                continue

            diff_dict[key] = {
                'old': old_obj[key],
                'new': new_obj[key],
            }

        return diff_dict

    def get_history(self, obj):
        diff_list = []
        current = None

        for version in reversed(list(reversion.get_for_object(obj))):
            if current:
                questions_diff = self.get_questions_diff(version, current)
                diff_list.append(questions_diff)

            current = version

        return diff_list
