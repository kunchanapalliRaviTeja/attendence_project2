from django.db import connections
from django.db import models

class StudentDetails(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.CharField(max_length=100)
    mailid=models.CharField(max_length=100)
    sem=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    class Meta:
        db_table="studentdata"


class Presentees(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.CharField(max_length=100)
    sem=models.CharField(max_length=100)
    date=models.CharField(max_length=100)


class Absentees(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.CharField(max_length=100)
    sem=models.CharField(max_length=100)
    date=models.CharField(max_length=100)

        