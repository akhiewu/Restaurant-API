from unicodedata import category
from django.contrib import admin
from .models import Restaurant, Catagory, Food

# Register your models here.


admin.site.register(Restaurant)
admin.site.register(Catagory)
admin.site.register(Food)
