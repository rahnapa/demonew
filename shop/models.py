from django.db import models
from django.urls import reverse

# Create your models here.
class Categery(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='categery',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='categery'
        verbose_name_plural='categeries'

    def get_url(self):
        return reverse('shop:products_by_categery', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    categery=models.ForeignKey(Categery,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product', blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'
    def get_url(self):
        return reverse('shop:prodcatdetail',args=[self.categery.slug,self.slug])



    def __str__(self):
        return '{}'.format(self.name)
