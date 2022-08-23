from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# Model for Teachers
class Teacher(models.Model):
    user = models.OneToOneField(User, related_name="teacher", on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.user.username


# Model for Students
class Student(models.Model):
    user = models.OneToOneField(User, related_name="student", on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=150, null=True, blank=True)
    class_name = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username
