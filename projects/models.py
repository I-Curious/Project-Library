from django.db import models

class project(models.Model):
    year = models.CharField(max_length=9)
    title = models.CharField(max_length=100)
    student1_name = models.CharField(max_length=50)
    student2_name = models.CharField(max_length=50, null = True, blank=True)
    student3_name = models.CharField(max_length=50, null = True, blank=True)
    student4_name = models.CharField(max_length=50, null = True, blank=True)
    student5_name = models.CharField(max_length=50, null = True, blank=True)
    student1_no = models.IntegerField()
    student2_no = models.IntegerField(null = True, blank=True)
    student3_no = models.IntegerField(null = True, blank=True)
    student4_no = models.IntegerField(null = True, blank=True)
    student5_no = models.IntegerField(null = True, blank=True)
    description = models.CharField(max_length=1000)
    mentor = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    tools_used = models.CharField(max_length=100, null = True, blank=True)
    report_link = models.CharField(max_length=100, null = True, blank=True)
    awards = models.CharField(max_length=100, null = True, blank=True)
    programme_choice = (
        ('UG','UnderGraduate'),
        ('PG','PostGraduate'),
    )
    programme = models.CharField(max_length=2, choices=programme_choice)
    type_choice = (
        ('IN','Internal'),
        ('EX','External'),
    )
    type = models.CharField(max_length=2, choices=type_choice)
    scope = models.CharField(max_length=1000)
