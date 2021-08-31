from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

description = 'This is a wider card with supporting text ' \
              'below as a natural lead-in to additional content.' \
              ' This card has even longer content than the first to ' \
              'show that equal height action.'


class Category(models.Model):
    name = models.CharField(max_length=255)


class Item(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='items')
    description = models.TextField(default=description)
    price = models.IntegerField(default=0)
    discount_price = models.IntegerField(default=0)
    slug = models.SlugField(default='')
    added_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='items')

    class Meta:
        ordering = ['-added_on']
        verbose_name = 'Items on sale'

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    
    def get_total_item_price(self):
        return self.quantity * self.item.price
    
    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price
    
    def get_final_item_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_item_price()
        return total
    
    def __str__(self):
        return f" {self.user}"
