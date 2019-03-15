from django.db import models

class job(models.Model):
    #Bilder

    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary

