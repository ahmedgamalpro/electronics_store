from rest_framework import serializers
from .models import User, Cart,Carts_Item,Categories,Order,Product,Review



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','slug','avatar','created_at','updated_at','bio','company']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','created_by','status','created_at','updated_at']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts_Item
        fields = ['cart_id','product_id','price','quantity','created_at']


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id','slug','name','description','created_at','updated_at']




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['id','category_id','title','picture','summary','description','price','discount_type','discount_value','created_at','updated_at']



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields =['id','user_id','product_id','rating','comment','created_at']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields =['id','users_id','created_at']


