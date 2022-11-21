from django.db import models

# Create your models here.
class Familia(models.Model):
    
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha_de_nacimiento=models.DateField()

    def __str__(self) -> str:
        return super().__str__()
        