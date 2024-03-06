
from django.urls import path, include
from .views import (
    UserList,
    ProductList,
    CategoriesList,
    CartList,
    CartItemList,
    ReviewList
)

urlpatterns = [
    path('users', UserList.as_view()),
    path('products', ProductList.as_view()),
    path('category', CategoriesList.as_view()),
    path('cart', CartList.as_view()),
    path('cart-item', CartItemList.as_view()),
    path('review', ReviewList.as_view()),
]