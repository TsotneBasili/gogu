# Django Online Store Backend

## Overview
A beginner-friendly Django REST Framework backend for an online store. This project provides a complete backend system for managing products, categories, users, shopping carts, and orders.

## Current State
**Date: November 8, 2025**

### Completed Features
- ✅ **Step 1: Category Model**
  - Created Django project `store_backend` with `catalog` app
  - Implemented Category model with: name, slug, description, image, is_activated, created_at
  - Set up Django admin interface for category management
  - Pre-populated database with 9 default furniture categories
  - Server running on port 5000

- ✅ **Step 2: Product Model**
  - Created Product model with all required fields
  - Added color choices (10 options: black, white, brown, gray, beige, blue, red, green, natural wood, other)
  - Added material choices (8 options: wood, metal, plastic, glass, fabric, leather, composite, other)
  - Configured admin interface with filters and inline editing
  - Related to Category with ForeignKey relationship

- ✅ **Step 3: User Authentication**
  - Created accounts app for user management
  - Implemented user registration with custom form (username, email, first_name, last_name, password)
  - Set up login and logout functionality
  - Created profile view for authenticated users
  - Built simple HTML templates for registration, login, and profile pages
  - Configured authentication settings (LOGIN_URL, LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL)

### In Progress
- Step 4: Shopping cart
- Step 5: Order management
- Step 6: REST API endpoints

## Project Architecture

### Apps
- **catalog**: Product catalog management (categories, products)
- **accounts**: User authentication and profile management
- More apps will be added for cart and orders

### Models
**Category** (`catalog/models.py`)
- Fields: name, slug, description, image, is_activated, created_at
- Methods: `__str__()`, `get_absolute_url()`
- Admin: Registered with search, filters, and prepopulated slugs

**Product** (`catalog/models.py`)
- Fields: name, slug, category (FK), description, price, stock, is_available, featured, color, material, created_at, updated_at
- Color choices: Black, White, Brown, Gray, Beige, Blue, Red, Green, Natural Wood, Other
- Material choices: Wood, Metal, Plastic, Glass, Fabric, Leather, Composite, Other
- Methods: `__str__()`, `get_absolute_url()`
- Admin: Registered with filters by category, availability, featured status, color, material; inline editing for price, stock, availability, featured

### Default Categories
The database is pre-populated with:
- Chair, Sofa, Table, Wardrobe, Bed, Cabinet, Shelf, Armchair, Outdoor Furniture

## Database
- **Type**: SQLite (Django default)
- **Location**: `db.sqlite3`
- **Migrations**: All applied successfully

## Admin Access
- **URL**: http://localhost:5000/admin
- **Username**: admin
- **Password**: (Use the password you set when creating the superuser)

## Commands Reference

### Run Development Server
```bash
python manage.py runserver 0.0.0.0:5000
```

### Create Migrations
```bash
python manage.py makemigrations
```

### Apply Migrations
```bash
python manage.py migrate
```

### Access Django Shell
```bash
python manage.py shell
```

### Create Superuser
```bash
python manage.py createsuperuser
```

## Next Steps
1. Create Product model with color and material choices
2. Implement user registration and authentication
3. Build shopping cart functionality
4. Create order management system
5. Set up REST API endpoints for all models

## Dependencies
- Django 5.2.8
- Django REST Framework 3.16.1
- Pillow 12.0.0 (for image handling)

## Project Structure
```
store_backend/
├── catalog/              # Product catalog app
│   ├── migrations/       # Database migrations
│   ├── models.py        # Category model
│   └── admin.py         # Admin configuration
├── store_backend/       # Main project settings
│   ├── settings.py      # Project configuration
│   └── urls.py          # URL routing
├── media/               # Uploaded files
├── manage.py            # Django management script
└── db.sqlite3          # SQLite database
```

## Notes
- Project follows Django best practices for beginners
- Simple, clean structure with minimal complexity
- All code is well-documented and easy to understand
