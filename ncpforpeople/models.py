from django.db import models


class People(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    problem = models.TextField(blank=True, null=True)
    contactno = models.CharField(max_length=15, blank=True, null=True)
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    process_date = models.DateField(db_column='Process Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    photo = models.FileField(blank=True, null=True)
    status1 = models.CharField(db_column='Status1', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'people'
