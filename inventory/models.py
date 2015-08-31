from django.db import models


class TimeStampedModel(models.Model):
    """
    Una clase abstracta que registra la fecha de creacion y
    modificacion del modelo
    """
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    modified = models.DateTimeField(auto_now=True, verbose_name="fecha de modificacion")

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True

class Accessory(TimeStampedModel):
  model = models.CharField(max_length=255)
  feature = models.CharField(max_length=255)

class Location(TimeStampedModel):
  pass

class Brand(TimeStampedModel):
  pass

class Manufacture(TimeStampedModel):
  pass

class Product(TimeStampedModel):
    model = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    voltage = models.IntegerField()
    VOLTAGE_TYPE = (
        ('ac', 'AC'),
        ('dc', 'DC'),
    )
    voltage_type = models.CharField(max_length=2, choices=VOLTAGE_TYPE, default=VOLTAGE_TYPE[0][0])
    FREQUENCY = (
        ('60', '60hz'),
        ('50', '50hz'),
    )
    frequency = models.CharField(max_length=2, null=True, choices=FREQUENCY, default=FREQUENCY[0][0])
    PROPERTY = (
        ('ho', 'HOSPITAL'),
        ('pr', 'PRESTADO'),
        ('co', 'COMODATO'),
        ('me', 'MEDICO'),
    )
    property = models.CharField(max_length=2, choices=PROPERTY, default=PROPERTY[0][0])
    STATE = (
        ('on', 'OPERATIVO'),
        ('of', 'DANADO'),
    )
    state = models.CharField(max_length=2, choices=STATE, default=STATE[0][0])
    TYPE = (
        ('fx', 'FIJO'),
        ('mv', 'MOVIL'),
    )
    type = models.CharField(max_length=2, choices=TYPE, default=TYPE[0][0])

    """
    RELATIONSHIPS
    """
    location = models.ForeignKey(Location)
    brand = models.ForeignKey(Brand)
    manufacture = models.ForeignKey(Manufacture)
    accessories = models.ManyToManyField(Accessory)
