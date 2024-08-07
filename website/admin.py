from django.contrib import admin
from .models import Record #imports from models .py in our same directory

admin.site.register(Record) #will show record in admin page

# Register your models here.
