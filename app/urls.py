from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import course_list, index, course_detail

urlpatterns = [
    path('', index, name='index'),
    path('courses/', course_list, name='course_list'),
    path('courses/<int:pk>/', course_detail, name='course_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)