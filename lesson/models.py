#_*_encoding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'专题')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'专题'
        verbose_name_plural = verbose_name


    def to_obj(self):

        return dict(
            id=self.id,
            name=self.name,
            # lesson=[l.to_obj() for l in self.lesson_set.all()]
        )

    def to_obj2(self):

        return dict(
            id=self.id,
            name=self.name,
            lesson=[l.to_obj() for l in self.lesson_set.all()]
        )

class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name=u'所属专题')
    name = models.CharField(max_length=50, verbose_name=u'课程')
    url = models.CharField(max_length=512)


    def __unicode__(self):
        return self.name


    def to_obj(self):
        return dict(
            id=self.id,
            name=self.name,
            url=self.url,
        )


    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name





