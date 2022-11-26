from django.db import models

# Create your models here.

class Users(models.Model):
    """
    class for defining basic site users
    """

    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    study_year = models.SmallIntegerField()
    specialisation = models.CharField(max_length=255)

    # subject_list = models.ManyToManyField()
    models.ForeignKey('Subjects', blank=True, on_delete=models.CASCADE)


class Subjects(models.Model):
    """
    Class for enumarting the subjects present
    """
    name = models.CharField(max_length=255)
    # id = models.BigIntegerField(max_length=255)

    models.ManyToManyField(Users)

    # A ZIPPED file
    # https://stackoverflow.com/questions/72802359/django-view-to-download-a-file-from-server

    source = models.BinaryField()






