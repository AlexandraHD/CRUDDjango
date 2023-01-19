from django.db import models

# Create your models here.
class Registros(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    pet_type = models.CharField(max_length=30)
    pet_name = models.CharField(max_length=30)
    vaccine = models.CharField(max_length=5)
    
    def __str__(self):
        text = "{0} / {1}"
        return text.format(self.user_name, self.pet_type)