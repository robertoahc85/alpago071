from django.contrib import admin
from .models import School
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Formulario personalizado para validaciones avanzadas
class SchoolForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            try:
                validate_email(email)  # Utiliza el validador de Django
            except ValidationError:
                raise ValidationError("Por favor, ingresa un correo electrónico válido.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise ValidationError("El número de teléfono solo debe contener dígitos.")
        return phone

    class Meta:
        model = School
        fields = '__all__'

# Configuración avanzada del administrador
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    form = SchoolForm

    # Configuración de visualización
    list_display = (
        'name', 'institution_type', 'education_level', 'education_modality', 
        'shifts', 'phone', 'email', 'logo_preview', 'active', 'created_at'
    )
    list_filter = ('institution_type', 'education_level', 'education_modality', 'shifts', 'active', 'state')
    search_fields = ('name', 'email', 'phone', 'street', 'neighborhood', 'municipality', 'state', 'postal_code')
    readonly_fields = ('created_at', 'updated_at', 'logo_preview')
    ordering = ('-created_at',)

    # Organización en secciones
    fieldsets = (
        ("Información General", {
            'fields': ('name', 'institution_type', 'education_level', 'education_modality', 'shifts', 'active')
        }),
        ("Dirección", {
            'fields': ('street', 'number', 'neighborhood', 'municipality', 'state', 'postal_code')
        }),
        ("Contacto", {
            'fields': ('phone', 'email', 'website')
        }),
        ("Logotipo", {
            'fields': ('logo', 'logo_preview')
        }),
        ("Tiempos", {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    # Acciones personalizadas
    actions = ['mark_as_active', 'mark_as_inactive', 'download_school_data']

    def mark_as_active(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(request, f"{updated} escuela(s) marcadas como activas.")
    mark_as_active.short_description = "Marcar como activas"

    def mark_as_inactive(self, request, queryset):
        updated = queryset.update(active=False)
        self.message_user(request, f"{updated} escuela(s) marcadas como inactivas.")
    mark_as_inactive.short_description = "Marcar como inactivas"

    def download_school_data(self, request, queryset):
        # Simula la descarga de datos seleccionados
        schools = queryset.values_list('name', 'email', 'phone', 'address')
        with open('school_data.csv', 'w') as f:
            f.write("Nombre,Correo,Teléfono,Dirección\n")
            for school in schools:
                f.write(",".join(school) + "\n")
        self.message_user(request, "Datos exportados a 'school_data.csv'.")
    download_school_data.short_description = "Exportar datos seleccionados a CSV"

    # Métodos personalizados
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.logo.url)
        return "Sin logotipo"
    logo_preview.short_description = "Vista previa del logotipo"

