from django.contrib import admin
from .models import Category, Product, Cart, CartItem
from .models import (
    Category,
    Product,
    Cart,
    CartItem,
    Order,
    OrderItem,
    Wishlist,
    Review,
    UserProfile,
)
admin.site.register(Order)
admin.site.register(OrderItem)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "price",
        "stock",
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "created_at",
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cart",
        "product",
        "quantity",
    )
    
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created_at')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'product',
        'rating',
        'created_at'
    )

    list_filter = ('rating',)

    search_fields = (
        'user__username',
        'product__name'
    )

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "phone",
    )