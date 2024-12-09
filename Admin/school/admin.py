from django.contrib import admin
from .models import School
from django.utils.html import format_html
from .forms import SchoolAdminForm


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    form = SchoolAdminForm
    list_display = (
        'name', 'get_institution_type', 'get_education_level', 
        'get_education_modality', 'get_shifts', 'phone', 'email', 
        'logo_preview', 'active', 'created_at'
    )
    list_filter = ('institution_type', 'education_level', 'education_modality', 'shifts', 'active', 'state')
    search_fields = ('name', 'email', 'phone', 'street', 'neighborhood', 'municipality', 'state', 'postal_code')
    readonly_fields = ('created_at', 'updated_at', 'logo_preview')
    ordering = ('-created_at',)

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
    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        updated = queryset.update(active=True)
        self.message_user(request, f"{updated} escuela(s) marcadas como activas.")
    mark_as_active.short_description = "Marcar como activas"

    def mark_as_inactive(self, request, queryset):
        updated = queryset.update(active=False)
        self.message_user(request, f"{updated} escuela(s) marcadas como inactivas.")
    mark_as_inactive.short_description = "Marcar como inactivas"

    # Métodos personalizados para mostrar valores multiselección
    def get_institution_type(self, obj):
        return ", ".join(obj.institution_type)
    get_institution_type.short_description = "Tipo de institución"

    def get_education_level(self, obj):
        return ", ".join(obj.education_level)
    get_education_level.short_description = "Nivel educativo"

    def get_education_modality(self, obj):
        return ", ".join(obj.education_modality)
    get_education_modality.short_description = "Modalidad educativa"

    def get_shifts(self, obj):
        return ", ".join(obj.shifts)
    get_shifts.short_description = "Turnos"

    # Vista previa del logotipo
    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.logo.url)
        return "Sin logotipo"
    logo_preview.short_description = "Vista previa del logotipo"
