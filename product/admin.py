from django.contrib import admin

# Register your models here.
from product.models import Drink, Category, Allergy

admin.site.register(Drink)
admin.site.register(Category)
admin.site.register(Allergy)
