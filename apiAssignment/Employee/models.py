from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    years_with_company = models.FloatField()
    salary = models.DecimalField(max_digits = 20, decimal_places =2)
