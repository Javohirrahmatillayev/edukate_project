from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import CourseListView, IndexView, CourseDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/subject/<int:subject_id>/', CourseListView.as_view(), name = 'courses_by_subject'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    # path('login/', views.login_view, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)