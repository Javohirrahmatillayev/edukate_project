from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView
from .models import Course, Subject

class CourseListView(ListView):
    model = Course
    template_name = 'course.html'
    context_object_name = 'courses'
    paginate_by = 6
    
    def get_queryset(self):
        subject_id = self.kwargs.get('subject_id')
        if subject_id:
            return Course.objects.filter(subject_id = subject_id)
        
        return Course.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject_id = self.kwargs.get('subject_id')
        if subject_id:
            context['current_subject'] = get_object_or_404(Subject, id =subject_id)
        return context

class IndexView(TemplateView):
    template_name = 'index.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'detail.html' 
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = self.object.modules.prefetch_related('contents__item').all()
        return context
    
