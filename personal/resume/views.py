# from django.shortcuts import render
from .models import Summary, Education, Skills, Experience, Languages, Projects
from django.views.generic import TemplateView
from django.forms.models import ModelForm
# from django.core.urlresolvers import reverse_lazy, reverse

import os


# Create your views here.
class ResumeView(TemplateView):
    # model = Resume
    template_name = 'resume.html'
    detect = False


class IndexView(TemplateView):
    template_name = 'index.html'
    detect = False
