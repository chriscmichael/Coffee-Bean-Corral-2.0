from django.contrib import admin
from cups.models import Cup


class CupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cup, CupAdmin)
