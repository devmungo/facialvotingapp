from django.db import models
from django.contrib.auth.models import User


from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)


    class Meta:

        verbose_name_plural = 'categories'


    def __str__(self):

        return self.name


    def get_absolute_url(self):

        return reverse('list-category', args=[self.slug])

class Product(models.Model):

    #FK 

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)


    title = models.CharField(max_length=250)

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=255)

    vote = models.IntegerField(default=0)

    image = models.ImageField(upload_to='images/')


    class Meta:

        verbose_name_plural = 'products'


    def __str__(self):

        return self.title



    def get_absolute_url(self):

        return reverse('product-info', args=[self.slug])


class Conf(models.Model):
    confirmation_code = models.CharField(max_length=16)
    votername = models.CharField(max_length=50)
    voted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.votername



