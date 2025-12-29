from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    max_students = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    STATUS_CHOICES = (
        ('ACTIVE','ACTIVE'),
        ('DROPPED','DROPPED'),
    )
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    status =  models.CharField(choices=STATUS_CHOICES,max_length=100,default="ACTIVE")
    
    class Meta:
        unique_together = ('student','course')
    
    def __str__(self):
        return f"{self.student.name} - {self.course.title} - {self.status}"