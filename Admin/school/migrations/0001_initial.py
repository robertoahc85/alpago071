# Generated by Django 5.1.3 on 2024-12-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre de la escuela')),
                ('street', models.CharField(max_length=255, verbose_name='Calle')),
                ('number', models.CharField(max_length=10, verbose_name='Número')),
                ('neighborhood', models.CharField(max_length=255, verbose_name='Colonia')),
                ('municipality', models.CharField(max_length=255, verbose_name='Municipio')),
                ('state', models.CharField(max_length=255, verbose_name='Estado')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Código postal')),
                ('phone', models.CharField(max_length=15, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='school_logos/', verbose_name='Logotipo')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Sitio web')),
                ('established_date', models.DateField(blank=True, null=True, verbose_name='Fecha de fundación')),
                ('institution_type', models.CharField(choices=[('public', 'Pública'), ('private', 'Privada'), ('mixed', 'Mixta')], max_length=10, null=True, verbose_name='Tipo de institución')),
                ('education_level', models.CharField(choices=[('preschool', 'Preescolar'), ('primary', 'Primaria'), ('secondary', 'Secundaria'), ('high_school', 'Preparatoria'), ('university', 'Universidad')], max_length=15, null=True, verbose_name='Nivel educativo')),
                ('education_modality', models.CharField(choices=[('in_person', 'Presencial'), ('online', 'En línea'), ('hybrid', 'Híbrida')], max_length=10, null=True, verbose_name='Modalidad educativa')),
                ('shifts', models.CharField(choices=[('morning', 'Matutino'), ('afternoon', 'Vespertino'), ('night', 'Nocturno')], max_length=10, null=True, verbose_name='Turnos')),
                ('active', models.BooleanField(default=True, verbose_name='¿Activo?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última actualización')),
            ],
        ),
    ]