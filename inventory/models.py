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
    # General Information
    code = models.CharField(max_length=255, verbose_name="Codigo", primary_key=True)
    model = models.CharField(max_length=255, verbose_name="Modelo")
    series = models.CharField(max_length=255, verbose_name="Serie")
    invima = models.CharField(max_length=255, verbose_name="Invima")
    n_inventary = models.CharField(max_length=255, verbose_name="Numero de inventario", null=True)
    p_maintenance = models.CharField(max_length=255, verbose_name="Periodicidad de Mantenimiento", null=True)
    p_calibration = models.CharField(max_length=255, verbose_name="Periodo de Calibracion", null=True)
    calibration  = models.BooleanField(default=False, verbose_name="Calibracion")
    characteristics = models.TextField(verbose_name="Caracteristicas", null=True)
    RISK_TYPE = (
            ('i', 'I'),
            ('ii', 'IIa'),
            ('iib', 'IIb'),
            ('iii', 'III')
            )
    risk_type = models.CharField(max_length=3, choices=RISK_TYPE, default=RISK_TYPE[0][0], verbose_name="Clisificacion de riesgo")
    # locations
    clinic = models.CharField(max_length=255, verbose_name="Clinica", default="HOSPITAL DIVINA MISERICORDIA")
    region  = models.CharField(max_length=255, verbose_name="Region", default="CARIBE")
    city  = models.CharField(max_length=255, verbose_name="City", default="MAGANGE")
    department  = models.CharField(max_length=255, verbose_name="Departamento", default="BOLIVAR")
    tower  = models.CharField(max_length=255, verbose_name="Torre", default="N/A")
    floor = models.CharField(max_length=255, verbose_name="Piso", null=True)
    phisycal_location  = models.CharField(max_length=255, verbose_name="Localizacion Fisica", null=True)

    # documentation
    service_manual = models.BooleanField(default=False, verbose_name="Manual de Servicio")
    maintenance_protocol  = models.BooleanField(default=False, verbose_name="Protocolo de mantenimiento")

    # Historical register
    PROPERTY = (
        ('ho', 'HOSPITAL'),
        ('pr', 'PRESTADO'),
        ('co', 'COMODATO'),
        ('me', 'MEDICO'),
        )
    property = models.CharField(max_length=2, choices=PROPERTY, default=PROPERTY[0][0], verbose_name="Propietario")
    supplier = models.CharField(max_length=255, verbose_name="Proveedor", null=True)
    warranty = models.CharField(max_length=255, verbose_name="Garantia", null=True)
    date_purchase = models.DateField(verbose_name="Fecha de Compra", null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo", null=True)


    # technical data
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
    consumption = models.CharField(max_length=255, verbose_name="Consumo", null=True)
    power = models.CharField(max_length=255, verbose_name="Potencia", null=True)
    weight = models.CharField(max_length=255, verbose_name="Peso", null=True)
    temperature = models.CharField(max_length=255, verbose_name="Temperatura", null=True)
    pressure = models.CharField(max_length=255, verbose_name="Presion", null=True)
    capacity = models.CharField(max_length=255, verbose_name="Capacidad", null=True)

    # tecnology type
    electric = models.BooleanField(default=False, verbose_name="Electrico")
    electronic = models.BooleanField(default=False, verbose_name="Electronico")
    mechanic = models.BooleanField(default=False, verbose_name="Mecanico")
    electromagnetic = models.BooleanField(default=False, verbose_name="Electromagnetico")
    hydraulic = models.BooleanField(default=False, verbose_name="Hidraulico")
    tire = models.BooleanField(default=False, verbose_name="neumatico")
    steam = models.BooleanField(default=False, verbose_name="Vapor")
    other = models.CharField(max_length=255, verbose_name="Otro", null=True)

    STATE = (
        ('1', 'OPTIMO'),
        ('2', 'BUENO'),
        ('3', 'REGULAR'),
        ('4', 'MALO'),
        ('5', 'OBSOLETO'),
        )
    state = models.CharField(max_length=2, choices=STATE, default=STATE[0][1], verbose_name="Estado Funcionamiento")
    condition = models.CharField(max_length=2, choices=STATE, default=STATE[0][1], verbose_name="Condicion Operativa")
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
