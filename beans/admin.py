from django.contrib import admin
from beans.models import Bean

class BeanAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bean, BeanAdmin)
