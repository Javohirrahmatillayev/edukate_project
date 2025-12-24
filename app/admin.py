from django.contrib import admin
from .models import Teacher, Subject, Course, Module, Text, File, Video, Image, CustomUser
from django.contrib.auth.admin import UserAdmin



class TextInline(admin.StackedInline):
    model = Text
    fk_name = 'module'
    extra = 1

class VideoInline(admin.StackedInline):
    model = Video
    fk_name = 'module'
    extra = 1

class ImageInline(admin.TabularInline):
    model = Image
    fk_name = 'module'
    extra = 1

class FileInline(admin.TabularInline):
    model = File
    fk_name = 'module'
    extra = 1



class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1
    show_change_link = True  


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'expertise', 'experience_years', 'is_active', 'created_at')
    search_fields = ('full_name', 'expertise')
    list_filter = ('is_active', 'expertise')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'subject', 'created_at')
    list_filter = ('subject', 'owner')
    search_fields = ('title', 'overview')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline] # Kurs ichida faqat Modullar ro'yxati chiqadi



@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('title',  'owner', 'created_at')
    
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Admin list page
    list_display = (
        'email',
        'full_name',
        'gender',
        'birth_date',
        'is_staff',
        'is_active',
    )
    list_filter = ('is_staff', 'is_active', 'gender')

    # Admin detail page (edit)
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal info', {
            'fields': ('full_name', 'gender', 'birth_date', 'age')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    # Create user in admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'full_name',
                'gender',
                'birth_date',
                'password1',
                'password2',
                'is_staff',
                'is_active',
            ),
        }),
    )

    # Search & ordering
    search_fields = ('email', 'full_name')
    ordering = ('email',)
