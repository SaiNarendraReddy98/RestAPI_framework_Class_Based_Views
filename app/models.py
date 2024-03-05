from django.db import models

# Create your models here.

class School(models.Model):
    school_id = models.IntegerField(primary_key=True)
    school_name = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name
    

class Student(models.Model):
    school_id = models.ForeignKey(School,on_delete=models.CASCADE)
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField()
    student_class = models.CharField(max_length=100)
    student_phno = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name