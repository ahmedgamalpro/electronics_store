
from django.urls import path, include
from .views import (
    UserList,
    UserDetail,
    ProductList,
    ProductDetail,
    CategoriesList,
    CategoriesDetail,
    CartList,
    CartDetail,
    CartItemList,
    CartItemDetail,
    ReviewList,
    ReviewDetail,
    OrderList,
    OrderDetail
)

urlpatterns = [
    path('users', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('products', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('category', CategoriesList.as_view()),
    path('category/<int:pk>/', CategoriesDetail.as_view()),
    path('cart', CartList.as_view()),
    path('cart/<int:pk>/', CartDetail.as_view()),
    path('cart-item', CartItemList.as_view()),
    path('cart-item/<int:pk>/', CartItemDetail.as_view()),
    path('review', ReviewList.as_view()),
    path('review/<int:pk>/', ReviewDetail.as_view()),
    path('order', OrderList.as_view()),
    path('order/<int:pk>/', OrderDetail.as_view()),
]