# SHOPEASE

Shopease is a Django-based e-commerce web application built with a simple product catalog, cart management, checkout workflow, wishlist support, order history, user authentication, reviews, and an admin dashboard.

## Project Overview

- Framework: Django 6.0.6
- Database: SQLite (`db.sqlite3`) by default
- App name: `shopease`
- Project name: `ecommerce`
- Templates stored in `ecommerce/shopease/templates`
- Static assets in `ecommerce/shopease/static`
- Media uploads stored in `ecommerce/media`

## Key Features

- Product listing and search
- Product category filtering
- Product detail pages with reviews
- User registration and login
- Persistent user cart with add/remove/increase/decrease quantity
- Checkout page with order creation and stock adjustment
- Order history and order detail pages
- Wishlist management
- User profile page
- Admin dashboard and model management

## Models

- `Category`: Product categories
- `Product`: Product catalog with name, description, price, stock, image, and category
- `Cart` / `CartItem`: User shopping cart and item quantities
- `Order` / `OrderItem`: Purchase records with payment and shipping details
- `Wishlist`: User wishlist items
- `Review`: Product review with rating and text
- `UserProfile`: Extended user profile with phone, address, and profile image

## URL Structure

The main routes provided by the `shopease` app include:

- `/` — Home page
- `/products/` — Product listing
- `/products/<id>/` — Product details
- `/cart/` — Cart page
- `/checkout/` — Checkout page
- `/login/` — Login page
- `/register/` — Registration page
- `/logout/` — Logout endpoint
- `/profile/` — User profile page
- `/wishlist/` — Wishlist page
- `/orders/` — Orders listing
- `/orders/<id>/` — Order details
- `/dashboard/` — Admin-style dashboard
- `/admin/` — Django admin site

## Setup Instructions

### Prerequisites

- Python 3.8+ installed
- Recommended: Virtual environment
- `pip` available

### Installation

1. Open a terminal and change into the project folder:

```powershell
cd "C:\Users\ELCOT\OneDrive - ELCOT\Desktop\shopease\ecommerce"
```

2. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install django==6.0.6 pillow
```

> `pillow` is required for image fields used by product and profile uploads.

### Database migration

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Create a superuser

```powershell
python manage.py createsuperuser
```

### Run the development server

```powershell
python manage.py runserver
```

Then open `http://127.0.0.1:8000/` in your browser.

## Django Admin

Visit `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.

Manage:

- Categories
- Products
- Carts and Cart Items
- Orders and Order Items
- Wishlists
- Reviews
- User Profiles

## Local Media and Static Configuration

- Static files served from: `ecommerce/shopease/static`
- Media uploads served from: `ecommerce/media`
- Media URL: `/media/`

## Important Notes

- `DEBUG` is currently enabled in `ecommerce/ecommerce/settings.py`. Disable it for production.
- `SECRET_KEY` is stored in settings and should be replaced with a secure secret in a production environment.
- `ALLOWED_HOSTS` is empty; add allowed hostnames before deployment.
- The SQLite database is configured at `ecommerce/db.sqlite3`.

## Suggested Improvements

- Add pagination for products and orders
- Add email notifications for order confirmation
- Add support for multiple payment methods
- Add user address forms and shipping options
- Harden authentication and production settings

## Project Structure

```text
shopease/
  ecommerce/                 # Django project root
    db.sqlite3
    manage.py
    ecommerce/               # project configuration
      settings.py
      urls.py
      wsgi.py
    shopease/                # app code
      models.py
      views.py
      urls.py
      admin.py
      templates/
      static/
  media/                     # uploaded media files
```

## Contact

For development or customization, update the app logic in `ecommerce/shopease/views.py` and model definitions in `ecommerce/shopease/models.py`.

---

This README provides the core details for running and extending the Shopease Django application.