from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return self.name


class Modifier(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    item = models.ManyToManyField(Item, related_name="modifiers")

    def __str__(self):
        return self.name
