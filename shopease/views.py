from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import (
    Product,
    Cart,
    CartItem,
    Order,
    OrderItem,
    Wishlist,
    Category,
    Review,
    UserProfile,
)


def home(request):
    return render(request, 'home.html')

def products(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    search = request.GET.get('search')
    category = request.GET.get('category')

    if search:
        products = products.filter(name__icontains=search)

    if category:
        products = products.filter(category__id=category)

    context = {
        "products": products,
        "categories": categories
    }

    return render(request, "products.html", context)
    
def product_details(request, id):

    product = get_object_or_404(Product, id=id)

    reviews = Review.objects.filter(
        product=product
    ).order_by('-created_at')

    return render(
        request,
        "product_details.html",
        {
            "product": product,
            "reviews": reviews
        }
    )

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")

def register(request):
       if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful")
        return redirect('login')

       return render(request, "register.html")

def logout_page(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'profile.html')

@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

@login_required
def cart(request):

    cart, created = Cart.objects.get_or_create(user=request.user)

    items = CartItem.objects.filter(cart=cart)

    grand_total = 0

    for item in items:
        grand_total += item.product.price * item.quantity

    return render(request, "cart.html", {
        "items": items,
        "grand_total": grand_total
    })

@login_required
def remove_cart_item(request, item_id):

    item = get_object_or_404(CartItem, id=item_id)

    if item.cart.user == request.user:
        item.delete()

    return redirect('cart')

@login_required
def increase_cart(request, item_id):

    item = get_object_or_404(CartItem, id=item_id)

    if item.cart.user == request.user:
        item.quantity += 1
        item.save()

    return redirect('cart')

@login_required
def decrease_cart(request, item_id):

    item = get_object_or_404(CartItem, id=item_id)

    if item.cart.user == request.user:

        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()

    return redirect('cart')

@login_required
def orders(request):

    user_orders = Order.objects.filter(user=request.user).order_by('-ordered_at')

    return render(request, "orders.html", {
        "orders": user_orders
    })

@login_required
def checkout(request):

    cart = get_object_or_404(Cart, user=request.user)
    items = CartItem.objects.filter(cart=cart)

    total = sum(item.product.price * item.quantity for item in items)

    if request.method == "POST":

        address = request.POST.get("address")
        phone = request.POST.get("phone")
        payment = request.POST.get("payment")

        order = Order.objects.create(
            user=request.user,
            address=address,
            phone=phone,
            payment_method=payment,
            total_amount=total
        )

        for item in items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

            # Reduce stock
            item.product.stock -= item.quantity
            item.product.save()

        # Empty the cart
        items.delete()
        cart.delete()

        messages.success(request, "Order Placed Successfully!")

        return redirect("orders")

    return render(request, "checkout.html", {
        "items": items,
        "total": total
    })

@login_required
def order_details(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    items = OrderItem.objects.filter(order=order)

    return render(
        request,
        "order_details.html",
        {
            "order": order,
            "items": items
        }
    )

@login_required
def add_to_wishlist(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    messages.success(request, "Added to Wishlist")

    return redirect('wishlist')

@login_required
def wishlist(request):

    items = Wishlist.objects.filter(user=request.user)

    return render(
        request,
        "wishlist.html",
        {
            "items": items
        }
    )

@login_required
def remove_wishlist(request, wishlist_id):

    item = get_object_or_404(
        Wishlist,
        id=wishlist_id,
        user=request.user
    )

    item.delete()

    messages.success(request, "Removed from Wishlist")

    return redirect('wishlist')

@login_required
def add_review(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":

        rating = request.POST.get("rating")

        review = request.POST.get("review")

        Review.objects.update_or_create(

            user=request.user,

            product=product,

            defaults={
                "rating": rating,
                "review": review
            }

        )

        messages.success(
            request,
            "Review Submitted Successfully"
        )

    return redirect(
        "product_details",
        id=product.id
    )

@login_required
def profile(request):

    profile = UserProfile.objects.get(user=request.user)

    total_orders = Order.objects.filter(
        user=request.user
    ).count()

    wishlist = Wishlist.objects.filter(
        user=request.user
    ).count()

    cart = CartItem.objects.filter(
        cart__user=request.user
    ).count()

    context = {

        "profile": profile,

        "orders": total_orders,

        "wishlist": wishlist,

        "cart": cart

    }

    return render(
        request,
        "profile.html",
        context
    )

@login_required
def dashboard(request):

    total_products = Product.objects.count()

    total_categories = Category.objects.count()

    total_orders = Order.objects.count()

    total_users = User.objects.count()

    total_sales = Order.objects.aggregate(
        Sum('total_amount')
    )['total_amount__sum']

    if total_sales is None:
        total_sales = 0

    context = {

        "products": total_products,

        "categories": total_categories,

        "orders": total_orders,

        "users": total_users,

        "sales": total_sales

    }

    return render(request, "dashboard.html", context)
