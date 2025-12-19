from django.db import models
from decimal import Decimal 
from django.contrib.contenttypes.models import ContentType
from django.templatetags.static import static
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='instructors/', blank=True, null=True)

    expertise = models.CharField(
        max_length=255,
        help_text="Masalan: Python, Frontend, Data Science"
    )

    experience_years = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name



class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(Teacher,related_name='courses',on_delete=models.SET_NULL,null=True)
    subject = models.ForeignKey(Subject,related_name='courses',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    overview = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=6, decimal_places= 1)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def image_url(self):
        if not self.image:
            return static('/not_found_image.png')
        return self.image.url
    
    class Meta:
        ordering = ['-created_at']

    
    


class Module(models.Model):
    course = models.ForeignKey(Course,related_name='modules',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    overview = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.title


class Content(models.Model):
    module = models.ForeignKey(Module,related_name='contents',on_delete=models.CASCADE)
    
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            "model__in":(
                'text',
                'video',
                'image',
                'file'
            )
        }
    )
    
    object_id = models.PositiveIntegerField()

    item = GenericForeignKey(
        'content_type',
        'object_id'
    )
    


class ItemBase(models.Model):
    owner = models.ForeignKey(Module,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class Text(ItemBase):
    module = models.ForeignKey(Module, related_name='texts', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()

class File(ItemBase):
    module = models.ForeignKey(Module, related_name='files', on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='files')

class Video(ItemBase):
    module = models.ForeignKey(Module, related_name='videos', on_delete=models.CASCADE, null=True, blank=True)
    video = models.FileField(upload_to='videos/', verbose_name="Video File")
    
    def __str__(self):
        return self.title

class Image(ItemBase):
    module = models.ForeignKey(Module, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images')
