from django.db import models


# Create your models here.

class Allergy(models.Model):
    class Meta:
        db_table = "allergy"

    allergy_name = models.CharField(max_length=256)


class Category(models.Model):
    class Meta:
        db_table = "category"

    name = models.CharField(max_length=256)


class Drink(models.Model):
    class Meta:
        db_table = "drink"

    name = models.CharField(max_length=256)
    nutrition = models.CharField(max_length=256)
    allergy = models.ManyToManyField(Allergy)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
