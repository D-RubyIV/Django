import os
from django.db import models
from django.contrib.auth.models import User
from pathlib import Path
from enum import Enum
from django.contrib.auth.models import AbstractUser, BaseUserManager
from ckeditor.fields import RichTextField

class Role(models.TextChoices):
    ADMIN = "Admin"
    USER = "User"
    MENDATOR = "Mendator"
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)
    enable = models.BooleanField(default=False)
    accessToken = models.CharField(max_length=500, default="")
    refreshToken = models.CharField(max_length=500, default="")
    def __str__(self) -> str:
        return self.user.username
    
    
class Product(models.Model):
    productName = models.CharField(max_length=200, null=True, blank=True)
    productPrice = models.FloatField(null=True, blank=True)
    productSold = models.IntegerField(null=True, blank=True)
    productRemain = models.IntegerField(null=True, blank=True)
    productImage = models.ImageField(null=True, blank=True, upload_to="product/")
    productDescription = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.productName
    
    @property
    def getUrlImage(self):
        try:
            path = self.productImage.url
        except Exception as e:
            print(e)
            path = ""
        return path
    
    def __str__(self) -> str:
        return f'Product object ({self.id}) {self.productName}'


class Order(models.Model):
    orderUser = Customer.user
    orderStatus = models.BooleanField(null=True, blank=True)
    
    
class OderDetail(models.Model):
    userOrder = models.ForeignKey(Order, on_delete=models.CASCADE,null=True, blank=True)
    producOrdert = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    amountOrder = models.IntegerField(null=True, blank=True)
    
class Blog(models.Model):
    userPost = models.ForeignKey(User, on_delete=models.CASCADE)
    post = RichTextField(null=True, blank=True)