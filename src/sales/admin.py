from django.contrib import admin
from sales.models import Position, Sale, CSV

# Register your models here.

admin.site.register(Position)
admin.site.register(Sale)
admin.site.register(CSV)