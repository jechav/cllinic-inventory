from django.db import models


class TimeStampedModel(models.Model):
    """
    Una clase abstracta que registra la fecha de creacion y
    modificacion del modelo
    """
    name = models.CharField(max_length=255, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    modified = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    def __unicode__(self):
      return self.name

    class Meta:
      abstract = True

class Accessory(TimeStampedModel):
    model = models.CharField(max_length=255, verbose_name="Modelo")
    feature = models.CharField(max_length=255, verbose_name="Caracteristicas")
    class Meta:
      verbose_name_plural = "Accesorios"
      verbose_name = "Accesorio"

class Location(TimeStampedModel):
    class Meta:
      verbose_name_plural = "Servicio"
      verbose_name = "Servicio"

class Sublocation(TimeStampedModel):
    service = models.ForeignKey(Location, verbose_name="Servicio"); 
    class Meta:
      verbose_name_plural = "Localizaciones"
      verbose_name = "Localizacion"

class Brand(TimeStampedModel):
    class Meta:
      verbose_name_plural = "Marcas"
      verbose_name = "Marca"

class Manufacture(TimeStampedModel):
    class Meta:
      verbose_name_plural = "Frabricantes"
      verbose_name = "Fabricante"

class Product(TimeStampedModel):
    model = models.CharField(max_length=255, verbose_name="Modelo")
    series = models.CharField(max_length=255, verbose_name="Serie")
    voltage = models.IntegerField(verbose_name="Voltaje")
    VOLTAGE_TYPE = (
        ('ac', 'AC'),
        ('dc', 'DC'),
        )
    voltage_type = models.CharField(max_length=2, choices=VOLTAGE_TYPE, default=VOLTAGE_TYPE[0][0], verbose_name="Tipo de Voltaje")
    FREQUENCY = (
        ('60', '60hz'),
        ('50', '50hz'),
        )
    frequency = models.CharField(max_length=2, null=True, choices=FREQUENCY, default=FREQUENCY[0][0], verbose_name="Frecuencia")
    PROPERTY = (
        ('ho', 'HOSPITAL'),
        ('pr', 'PRESTADO'),
        ('co', 'COMODATO'),
        ('me', 'MEDICO'),
        )
    property = models.CharField(max_length=2, choices=PROPERTY, default=PROPERTY[0][0], verbose_name="Propietario")
    STATE = (
        ('on', 'OPERATIVO'),
        ('of', 'DANADO'),
        )
    state = models.CharField(max_length=2, choices=STATE, default=STATE[0][0], verbose_name="Estado")
    TYPE = (
        ('fx', 'FIJO'),
        ('mv', 'MOVIL'),
        )
    type = models.CharField(max_length=2, choices=TYPE, default=TYPE[0][0], verbose_name="Tipo")

    """
    RELATIONSHIPS
    """
    location = models.ForeignKey(Sublocation, verbose_name="Localizacion")
    brand = models.ForeignKey(Brand, verbose_name="Marca")
    manufacture = models.ForeignKey(Manufacture, verbose_name="Fabricante")
    accessories = models.ManyToManyField(Accessory, verbose_name="Accesorios", blank=True)
    class Meta:
      verbose_name_plural = "Equipos"
      verbose_name = "Equipo"
