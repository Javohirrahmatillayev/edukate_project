from .models import Subject

def subject_renderer(request):
    return {
        'all_subjects': Subject.objects.all()   
    }