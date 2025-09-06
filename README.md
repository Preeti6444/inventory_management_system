# Inventory Management System (Django)

A simple **Inventory Management System** built with **Django**.  
This project helps businesses manage **Products, Categories, and Suppliers**, with full **CRUD operations**.

---

## Features
- User Authentication (Admin & Staff)
- Manage Products (Add, Edit, Delete, View)
- Manage Categories
- Manage Suppliers
- Track Stock Levels
- Low-Stock Alerts
- REST API support (optional extension)
- Bootstrap-based dashboard

---
## Usage

1. Start the development server:
   ```bash
   python manage.py runserver
Open your browser and go to:

cpp
Copy code
http://127.0.0.1:8000/
Access the admin panel at:

arduino
Copy code
http://127.0.0.1:8000/admin/
Default superuser can be created with:

bash
Copy code
python manage.py createsuperuser
---

## Project Structure 
inventory_management_system/

├── inventory_management_system/   # Project settings

│   ├── settings.py

│   ├── urls.py

|   ├── asgi.py

│   ├── wsgi.py

├── inventory/  # Main app

│   ├── __init__.py   

│   ├── admin.py    

│   ├── api.py   

│   ├── apps.py  

│   ├── decorators.py    

│   ├── forms.py    

│   ├── models.py                  # Product, Category, Supplier models

│   ├── serializers.py  

│   ├── tests.py 

│   ├── views.py                   # CRUD views

│   ├── urls.py                    # App routes

│   ├── templates/  # HTML templates

        └── Inventory

            └── base.html

            └── category_list.html

            └── confirm_delete.html

            └── dashboard.html

            └── form.html

            └── no_permission.html

            └── products_list.html

            └── supplier_list.html
            
        └── base.html
        
│   ├── static/                    # CSS, JS, Bootstrap

├── manage.py

├── Procfile

├── db.sqlite3

├── .gitignore

├── requirements.txt

├── README.md

---
## API Endpoints
📌 API Endpoints
🔑 Authentication

POST /api/auth/login/ → Login and get token/session

POST /api/auth/logout/ → Logout

📦 Products

GET /api/products/ → List all products

POST /api/products/ → Create a new product

GET /api/products/{id}/ → Get details of a single product

PUT /api/products/{id}/ → Update a product

PATCH /api/products/{id}/ → Partial update

DELETE /api/products/{id}/ → Delete a product

🏷 Categories

GET /api/categories/ → List all categories

POST /api/categories/ → Create a new category

GET /api/categories/{id}/ → Get details of a single category

PUT /api/categories/{id}/ → Update a category

PATCH /api/categories/{id}/ → Partial update

DELETE /api/categories/{id}/ → Delete a category

🚚 Suppliers

GET /api/suppliers/ → List all suppliers

POST /api/suppliers/ → Create a new supplier

GET /api/suppliers/{id}/ → Get details of a single supplier

PUT /api/suppliers/{id}/ → Update a supplier

PATCH /api/suppliers/{id}/ → Partial update

DELETE /api/suppliers/{id}/ → Delete a supplier
## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default, can be switched to PostgreSQL/MySQL)
- **Version Control:** Git & GitHub

---

## Installation & Setup

Python 3.10+ (for Django 5.x)
virtualenv
django==5.2
requirements.txt
djangorestframework
django-filter

## Deployment 
On Render

Push your code to GitHub.

Connect your repository to Render/Heroku.

Add requirements.txt and Procfile.

Set environment variables (e.g., SECRET_KEY, DEBUG=False).

Deploy and test.
---

## Important Links

Live Demo:

[Live Site](https://inventory-management-system-10.onrender.com/)


Admin Panel:

[Admin Panel](https://inventory-management-system-10.onrender.com/admin/)


API Endpoints:

- [Products](https://inventory-management-system-10.onrender.com/products/)
- [Categories](https://inventory-management-system-10.onrender.com/categories/)
- [Suppliers](https://inventory-management-system-10.onrender.com/suppliers/)


GitHub Repo:

[GitHub Repository](https://github.com/Preeti6444/inventory_management_system)

📌 Putting it all together in your README.md
## Live Demo
- [Project Homepage](https://inventory-management-system-10.onrender.com/)
- [Admin Panel](https://inventory-management-system-10.onrender.com/admin/)

## API Endpoints
- [Products](https://inventory-management-system-10.onrender.com/api/products/)
- [Categories](https://inventory-management-system-10.onrender.com/api/categories/)
- [Suppliers](https://inventory-management-system-10.onrender.com/api/suppliers/)
---

## Screenshots
<img width="1920" height="1020" alt="Site administration _ Django site admin - Google Chrome 9_6_2025 6_59_24 PM" src="https://github.com/user-attachments/assets/d12ae552-161e-4439-9967-e7a14574e64f" />
<img width="1920" height="1020" alt="Site administration _ Django site admin - Google Chrome 9_6_2025 6_58_41 PM" src="https://github.com/user-attachments/assets/59be61da-81b2-4fd6-aa69-e5f5c22f9bfb" />
<img width="1920" height="1020" alt="Site administration _ Django site admin - Google Chrome 9_6_2025 6_58_29 PM" src="https://github.com/user-attachments/assets/72f787d6-9686-4e79-9738-80600d705a74" />
<img width="1920" height="1020" alt="Site administration _ Django site admin - Google Chrome 9_6_2025 6_58_24 PM" src="https://github.com/user-attachments/assets/719fb181-256a-4a87-8b8d-97113799e065" />
<img width="1920" height="1020" alt="Site administration _ Django site admin - Google Chrome 9_6_2025 6_37_05 PM" src="https://github.com/user-attachments/assets/a7bd7c99-458c-4718-8e5a-4a4807ea2b7b" />

cd inventory_management_system


