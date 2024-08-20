from django.db import models
# dashboard/models.py
from django.db import models

class AMRData(models.Model):
    isolate_id = models.CharField(max_length=255)
    study = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    age_group = models.CharField(max_length=50)
    speciality = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    in_out_patient = models.CharField(max_length=50)
    year = models.IntegerField()
    phenotype = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    amoxycillin_clavulanate = models.CharField(max_length=50, null=True, blank=True)
    amoxycillin_clavulanate_I = models.CharField(max_length=50, null=True, blank=True)
    # Add all other drug columns similarly

    def __str__(self):
        return self.species


