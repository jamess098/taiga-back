# -*- coding: utf-8 -*-

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.views import login as auth_login, logout as auth_logout
from django import http

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics

from greenmine.base.serializers import LoginSerializer, UserLogged, UserSerializer
from greenmine.base.models import User
from greenmine.scrum import models


class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'login': reverse('login', request=request, format=format),
            'logout': reverse('logout', request=request, format=format),
            'projects': reverse('project-list', request=request, format=format),
            'milestones': reverse('milestone-list', request=request, format=format),
            'user-stories': reverse('user-story-list', request=request, format=format),
            'attachments': reverse('attachment-list', request=request, format=format),
            'tasks': reverse('task-list', request=request, format=format),
            'issues': reverse('issue-list', request=request, format=format),
            'severities': reverse('severity-list', request=request, format=format),
            'issue-status': reverse('issue-status-list', request=request, format=format),
            'task-status': reverse('task-status-list', request=request, format=format),
            'user-story-status': reverse('user-story-status-list', request=request, format=format),
            'priorities': reverse('priority-list', request=request, format=format),
            'issue-types': reverse('issue-type-list', request=request, format=format),
            'points': reverse('points-list', request=request, format=format),
            'documents': reverse('document-list', request=request, format=format),
            'questions': reverse('question-list', request=request, format=format),
            'question_responses': reverse('question-response-list', request=request, format=format),
            'wiki_pages': reverse('wiki-page-list', request=request, format=format),
            'wiki_page_attachments': reverse('wiki-page-attachment-list', request=request, format=format),
            'users': reverse('user-list', request=request, format=format),
        })



#class UserFilter(django_filters.FilterSet):
#    no_milestone = django_filters.NumberFilter(name="mileston", lookup_type='isnull')
#
#    class Meta:
#        model = UserStory
#        fields = ['project', 'milestone', 'no_milestone']


class UserList(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        projects = models.Project.objects.filter(members=self.request.user)
        return super(UserList, self).get_queryset().filter(projects__in=projects)\
                    .order_by('id').distinct()

    def pre_save(self, obj):
        pass


class Login(APIView):
    def post(self, request, format=None):
        username = request.DATA.get('username', None)
        password = request.DATA.get('password', None)

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                user = authenticate(username=username, password=password)
                login(request, user)

                return_data = LoginSerializer(UserLogged(**{
                    'token': request.session.session_key,
                    'username': request.user.username,
                    'first_name': request.user.first_name,
                    'last_name': request.user.last_name,
                    'email': request.user.email,
                    'last_login': request.user.last_login,
                    'color': request.user.color,
                    'description': request.user.description,
                    'default_language': request.user.default_language,
                    'default_timezone': request.user.default_timezone,
                    'colorize_tags': request.user.colorize_tags,
                }))

                return Response(return_data.data)
        except User.DoesNotExist:
            pass

        return Response({"detail": "Invalid username or password"}, status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    def post(self, request, format=None):
        logout(request)
        return Response()
