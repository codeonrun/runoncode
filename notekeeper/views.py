from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class Index(generic.TemplateView):
    template_name = 'notekeeper/index.html'


