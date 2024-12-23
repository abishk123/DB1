from django.db import models

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)

    def __str__(self):
        return str(self.deptno)

class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.DecimalField(max_digits=9, decimal_places=2)
    comm=models.DecimalField(max_digits=9, decimal_places=2, null=True, blank= True)
    #null = true is used to insert null values into DB
    #blank= True is used to process null values from forms to backend
    hiredate=models.DateField()
    #auto_now= True used to add data insertion date
    #auto_now_add = True used to add model creation date
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL, null=True, blank= True)
    age=models.IntegerField(null=True)

    def __str__(self):
        return self.ename


