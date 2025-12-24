from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView, TemplateView, DetailView, FormView, RedirectView
from django.contrib.auth import login, logout, get_user_model
from django.urls import reverse_lazy
from .models import Course, Subject, Teacher
from .forms import CustomUSerCreationForm, CustomUserLoginForm
from django.contrib import messages

User = get_user_model()


class RegisterView(FormView):
    template_name = 'account/signup.html'
    form_class = CustomUSerCreationForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = CustomUserLoginForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
    
class LogoutView(RedirectView):
    pattern_name = 'login'
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

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

class IndexView(ListView):
    model = Course
    template_name = "index.html"
    context_object_name = "courses"
    
class CourseDetailView(DetailView):
    model = Course
    template_name = 'detail.html' 
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = self.object.modules.prefetch_related('contents__item').all()
        return context
    
class ContactView(TemplateView):
    template_name = 'contact.html'
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        full_message = f"""
        Name: {name}
        Email: {email}
        Message:
        {message}
        """
        send_mail(
            subject=subject,
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list = ["deozey7@gmail.com"],
            fail_silently=False,
        )
        
        messages.success(request, "Your message has been sent succesfully!")
            
        return redirect('contact')
    
class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['subjects_count'] = Subject.objects.count()
        context['courses_count'] = Course.objects.count()
        context['instructors_count'] = User.objects.filter(is_staff=True).count()
        context['students_count'] = User.objects.filter(is_active=True).count()

        return context
    
    
class TeachersListView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'
    paginate_by = 6

    def get_queryset(self):
        return Teacher.objects.filter(is_active=True)