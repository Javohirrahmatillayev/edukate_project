from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import CourseListView, IndexView, CourseDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)