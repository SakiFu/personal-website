from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Summary(models.Model):

    text = models.TextField()

    def __str__(self):
        return self.text


@python_2_unicode_compatible
class Projects(models.Model):

    title = models.CharField(max_length=128)
    date_published = models.DateField(null=True, blank=True)
    project_desc = models.TextField()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Skills(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Education(models.Model):

    school = models.CharField(max_length=128)
    degree = models.CharField(max_length= 256)
    date_attended = models.DateField(null=True, blank=True)
    edu_desc = models.TextField()

    def __str__(self):
        return self.school


@python_2_unicode_compatible
class Experience(models.Model):

    title = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    date_worked = models.DateField(null=True, blank=True)
    job_desc = models.TextField()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Languages(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
