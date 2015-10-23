from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class ResumeView(TemplateView):
    # model = Resume
    template_name = 'resume.html'
    detect = False
