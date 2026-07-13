from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/<int:id>/', views.product_details, name='product_details'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_cart_item/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('increase-cart/<int:item_id>/', views.increase_cart, name='increase_cart'),
path('decrease-cart/<int:item_id>/', views.decrease_cart, name='decrease_cart'),
path('orders/', views.orders, name='orders'),
path('orders/<int:order_id>/', views.order_details, name='order_details'),
path('wishlist/', views.wishlist, name='wishlist'),
path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
path('remove-wishlist/<int:wishlist_id>/', views.remove_wishlist, name='remove_wishlist'),
path( 'review/<int:product_id>/', views.add_review,name='add_review'),
path('profile/',views.profile,name='profile'),
path('dashboard/', views.dashboard, name='dashboard'),
]