from django.db import models
from django.contrib.auth.models import User  # Assuming you are using Django's built-in User model

class Category_A(models.Model):
    users = models.ManyToManyField(User, related_name="categories_a")

    def __str__(self):
        return ", ".join(user.username for user in self.users.all())

    class Meta:
        verbose_name = "Category A"
        verbose_name_plural = "Category A"

class Category_B(models.Model):
    users = models.ManyToManyField(User, related_name="categories_b")

    def __str__(self):
        return ", ".join(user.username for user in self.users.all())

    class Meta:
        verbose_name = "Category B"
        verbose_name_plural = "Category B"

class Category_C(models.Model):
    users = models.ManyToManyField(User, related_name="categories_c")

    def __str__(self):
        return ", ".join(user.username for user in self.users.all())

    class Meta:
        verbose_name = "Category C"
        verbose_name_plural = "Category C"

class Category_D(models.Model):
    users = models.ManyToManyField(User, related_name="categories_d")

    def __str__(self):
        return ", ".join(user.username for user in self.users.all())

    class Meta:
        verbose_name = "Category D"
        verbose_name_plural = "Category D"
