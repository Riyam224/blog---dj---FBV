from django.db import models

from django.urls import reverse
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True, null=False)
    featured = models.BooleanField(blank=True, null=True)

    def get_absolute_url(self):
        # return f"product/{self.id}/"
        return reverse('blog:detail', kwargs={'id': self.id})
