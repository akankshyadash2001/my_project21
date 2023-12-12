from django.db import models
class Dept(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    DNAME=models. CharField(max_length=100)
    LOC=models. CharField(max_length=100)
class Emp(models.Model):
    EMPNO=models.IntegerField(primary_key=True)
    ENAME=models. CharField(max_length=100)
    JOB=models. CharField(max_length=100)
    MGR=models.IntegerField()
    HIREDATE=models.DateField()
    SAL=models.IntegerField()
    COMM=models.IntegerField()
    DEPTNO=models.ForeignKey(Dept,on_delete=models.CASCADE)

# Create your models here.
