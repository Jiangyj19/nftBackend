from django.db import models

# Create your models here.
class Contract(models.Model):
    address = models.CharFiled(max_length = 30)

    def __str__(self):
        return self.address