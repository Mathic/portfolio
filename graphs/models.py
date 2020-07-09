from django.contrib.auth.models import User

from django.db import models

import plotly.plotly as py
import plotly.graph_objs as go

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

class GraphData(models.Model):
    graph_year = models.IntegerField()
    average_temperature = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    average_precipitation = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    source_text = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    longitude = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    event = models.CharField(max_length=1000, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.graph_year)

class Month(models.Model):
    month = models.CharField(max_length=3)
    total_temperature = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_precipitation = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    year = models.ForeignKey(GraphData, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.month)

# unused, broken in Heroku PostGreSQL
class YearsGraph(models.Model):
    year = models.IntegerField()
    ottawa_average_t = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    ottawa_average_p = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    victoria_average_t = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    victoria_average_p = models.DecimalField(max_digits=6, decimal_places=3, default=0)

    def __str__(self):
        return str(self.year)

class MonthsGraph(models.Model):
    month = models.CharField(max_length=3)
    ottawa_average_t = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    ottawa_average_p = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    victoria_average_t = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    victoria_average_p = models.DecimalField(max_digits=6, decimal_places=3, default=0)

    def __str__(self):
        return str(self.month)

class TestTable(models.Model):
    test = models.CharField(max_length=10)

    def __str__(self):
        return str(self.test)
