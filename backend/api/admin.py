from django.contrib import admin
from .models import User, Cart,Carts_Item,Categories,Order,Product,Review
# Register your models here.


admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Carts_Item)
admin.site.register(Categories)

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Review)