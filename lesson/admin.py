from django.contrib import admin

# Register your models here.
from models import *

class CourseD(admin.ModelAdmin):
    list_display = ('id','name')

class LessonD(admin.ModelAdmin):
    list_display = ('id','name','url','course')
    search_fields = ('name',)
    list_filter = ('course',)


admin.site.register(Course,CourseD)
admin.site.register(Lesson,LessonD)