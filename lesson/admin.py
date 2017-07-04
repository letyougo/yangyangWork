from django.contrib import admin

# Register your models here.
from models import *
class CourseD(admin.ModelAdmin):
    list_display = ('id','name')

class LessonD(admin.ModelAdmin):
    list_display = ('id','name','course','url')

admin.site.register(Course,CourseD)
admin.site.register(Lesson,LessonD)