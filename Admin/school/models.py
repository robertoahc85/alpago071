from django.db import models
from multiselectfield import MultiSelectField

class School(models.Model):
    # Opciones para Tipo de institución
    INSTITUTION_TYPE_CHOICES = [
        ('private', 'Privada'),
        ('public', 'Pública'),
        ('mixed', 'Mixta'),
    ]

    # Opciones para Nivel educativo
    EDUCATION_LEVEL_CHOICES = [
        ('primary', 'Primaria'),
        ('secondary', 'Secundaria'),
        ('high_school', 'Preparatoria'),
        ('university', 'Universidad'),
    ]

    # Opciones para Modalidad educativa
    EDUCATION_MODALITY_CHOICES = [
        ('in_person', 'Presencial'),
        ('online', 'En línea'),
        ('hybrid', 'Híbrida'),
    ]

    # Opciones para Turnos
    SHIFT_CHOICES = [
        ('morning', 'Matutino'),
        ('afternoon', 'Vespertino'),
        ('night', 'Nocturno'),
    ]

    # Opciones para Estados de México
    MEXICO_STATES = [
        ('AG', 'Aguascalientes'),
        ('BC', 'Baja California'),
        ('BS', 'Baja California Sur'),
        ('CH', 'Chihuahua'),
        ('CL', 'Colima'),
        ('CM', 'Campeche'),
        ('CO', 'Coahuila'),
        ('CS', 'Chiapas'),
        ('DF', 'Ciudad de México'),
        ('DG', 'Durango'),
        ('GT', 'Guanajuato'),
        ('GR', 'Guerrero'),
        ('HG', 'Hidalgo'),
        ('JA', 'Jalisco'),
        ('MX', 'Estado de México'),
        ('MI', 'Michoacán'),
        ('MO', 'Morelos'),
        ('NA', 'Nayarit'),
        ('NL', 'Nuevo León'),
        ('OA', 'Oaxaca'),
        ('PU', 'Puebla'),
        ('QE', 'Querétaro'),
        ('QR', 'Quintana Roo'),
        ('SI', 'Sinaloa'),
        ('SL', 'San Luis Potosí'),
        ('SO', 'Sonora'),
        ('TB', 'Tabasco'),
        ('TL', 'Tlaxcala'),
        ('TM', 'Tamaulipas'),
        ('VE', 'Veracruz'),
        ('YU', 'Yucatán'),
        ('ZA', 'Zacatecas'),
    ]

    # Campos del modelo
    name = models.CharField(max_length=255, verbose_name="Nombre de la escuela")
    institution_type = MultiSelectField(
        choices=INSTITUTION_TYPE_CHOICES,
        verbose_name="Tipo de institución",
        max_length=50
    )
    education_level = MultiSelectField(
        choices=EDUCATION_LEVEL_CHOICES,
        verbose_name="Nivel educativo",
        max_length=50
    )
    education_modality = MultiSelectField(
        choices=EDUCATION_MODALITY_CHOICES,
        verbose_name="Modalidad educativa",
        max_length=50
    )
    shifts = MultiSelectField(
        choices=SHIFT_CHOICES,
        verbose_name="Turnos",
        max_length=50
    )
    street = models.CharField(max_length=255, verbose_name="Calle")
    number = models.CharField(max_length=10, verbose_name="Número")
    neighborhood = models.CharField(max_length=255, verbose_name="Colonia")
    municipality = models.CharField(max_length=255, verbose_name="Municipio")
    state = models.CharField(
        max_length=2,
        choices=MEXICO_STATES,
        verbose_name="Estado"
    )
    postal_code = models.CharField(max_length=10, verbose_name="Código postal")
    phone = models.CharField(max_length=15, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Correo electrónico")
    logo = models.ImageField(upload_to='school_logos/', verbose_name="Logotipo", null=True, blank=True)
    website = models.URLField(verbose_name="Sitio web", null=True, blank=True)
    students = models.ManyToManyField('student.Student', related_name='schools', verbose_name="Alumnos asignados")
    active = models.BooleanField(default=True, verbose_name="¿Activo?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return self.name
