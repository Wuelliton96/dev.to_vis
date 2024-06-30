from django.contrib import admin
from myapp import	models
# Register your models here.
admin.site.register(models.Inspetor)
admin.site.register(models.RegistraVistoria)

#admin.site.register(models.Vistoria)
#admin.site.register(models.VistoriaImage)

class VistoriaImageInlineAdmin(admin.TabularInline):
    model = models.VistoriaImage
    extra = 0

class VistoriaAdmin(admin.ModelAdmin):
    inlines = [VistoriaImageInlineAdmin]


admin.site.register(models.Vistoria, VistoriaAdmin)