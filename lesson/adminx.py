from django.contrib import admin

# Register your models here.
from models import *
import xadmin
class CourseD(admin.ModelAdmin):
    list_display = ('id','name')

class LessonD(admin.ModelAdmin):
    list_display = ('id','name','url','course')
    search_fields = ('name',)
    list_filter = ('course',)


xadmin.site.register(Course,CourseD)
xadmin.site.register(Lesson,LessonD)