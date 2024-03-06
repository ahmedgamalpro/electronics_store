from django.db import models
import uuid 



CART_STATUS = (
    ("ACTIVE","Active"),
    ("ORDERED","Ordered"),
    ("ABANDONNED","Abandonned")
)
DISCOUNT_TYPE=(
    ("NONE","None"),
    ("PERCENT","Percent"),
    ("AMOUNT","Amount")
)
# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    slug = models.SlugField(max_length=250)
   
    avatar = models.URLField( max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bio = models.TextField()
    company = models.CharField(max_length=50)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return f'{self.name} | {self.email} | {self.bio}'

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey("User", on_delete=models.CASCADE)
    status = models.CharField(choices=CART_STATUS, max_length=50,default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Carts_Item(models.Model):
    cart_id = models.ForeignKey("Cart", on_delete=models.CASCADE)
    prodcut_id = models.ForeignKey("Product", on_delete=models.CASCADE)
    #price = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class Categories(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(max_length=250)
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} '

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_id = models.ForeignKey("Categories", on_delete=models.CASCADE)
    title = models.TextField()
    picture = models.URLField( max_length=250)
    summary = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    discount_type = models.CharField(choices=DISCOUNT_TYPE, max_length=50,default="NONE")
    discount_value = models.FloatField(blank=True,null=True)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['title'] 
    def __str__(self):
        return f'{self.title} '

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    users_id = models.ForeignKey("User" , on_delete=models.CASCADE)
    product_id = models.ForeignKey("Product" , on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    users_id = models.ForeignKey("User" , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

