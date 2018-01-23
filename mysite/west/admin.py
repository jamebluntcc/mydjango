from django.contrib import admin
from .models import Character, Contact, Tag

# Register your models here.

admin.site.register([Character, Contact, Tag])
