from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView
from .models import Course

class CourseListView(ListView):
    model = Course
    template_name = 'course.html'
    context_object_name = 'courses'

class IndexView(TemplateView):
    template_name = 'index.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'detail.html'
    context_object_name = 'course'