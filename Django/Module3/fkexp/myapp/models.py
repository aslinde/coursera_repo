from django.db import models

# Create your models here.
#Menu Category
class MenuCategory(models.Model):
    category_name = models.CharField(max_length=100)
#Menu
class Menu(models.Model):
    menu_item = models.CharField(max_length=100)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")
