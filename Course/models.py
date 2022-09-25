from django.db import models

class course(models.Model) :
    subject = models.CharField(max_length=255, blank=True)

class lesson(models.Model) :
    subject = models.CharField(max_length=255, blank=True)