from django.contrib import admin

# Register your models here.
from .models import event
class eventAdmin(admin.ModelAdmin):
    class Meta:
        model = event

admin.site.register(event, eventAdmin)
