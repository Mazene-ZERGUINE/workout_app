from django.db import models

# Create your models here.
class Exercices(models.Model):  
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    ex_title = models.CharField(max_length=60)
    ex_load = models.CharField(max_length=20)
    ex_reps = models.CharField(max_length=20)



