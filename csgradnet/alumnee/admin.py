from django.contrib import admin

# Register your models here.

from . models import alumnee
from .models import portfolio
from .models import internship
from . models import education
# Register your modelodels here.

class alumneeAdmin(admin.ModelAdmin):
    class Meta:
        model = alumnee

admin.site.register(alumnee, alumneeAdmin)
admin.site.register(portfolio)
admin.site.register(internship)
admin.site.register(education)
