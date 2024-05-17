from django.db import models


class Genero(models.Model):
    getNombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.getNombre 


class Pelicula(models.Model):
    # todos los CharField deben tener max_length
    # CharField es un tipo de campo en Django para almacenar texto de longitud limitada. 
    pelCodigo = models.CharField(max_length=9)
    pelTitulo = models.CharField(max_length=50)
    pelProtagonista = models.CharField(max_length=50)
    pelDuracion = models.IntegerField()
    pelResumen = models.CharField(max_length=2000)

    # ruta imagen, null por defecto es false, se pone true para que acepte nulos
    pelFoto = models.ImageField(
        upload_to=f"fotos/", null=True, blank=True) 
    pelGenero = models.ForeignKey(Genero, on_delete=models.PROTECT)


    def __str__(self) -> str:
        return self.pelTitulo
