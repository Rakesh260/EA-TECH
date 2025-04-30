# EA-TECH
Mini E-Commerce Platform
This is a basic e-commerce web application built using Django and Django REST Framework, featuring JWT authentication, product listing, cart management, checkout, and a simple admin panel.

## Features
User Registration and Login (JWT Authentication)

Product Listings and Detail View

Add to Cart and View Cart

Checkout Process (Dummy "Order Confirmed")

Admin Panel:

Add/Edit/Delete Products

View Orders


## Tech Stack

Backend: Django, Django REST Framework

Authentication: JWT (via djangorestframework-simplejwt)

Frontend: Django Templates + Bootstrap

Database: SQLite (for development)

##  Project Structure

ecommerce_project/

│
├── accounts/          # User registration, login, JWT setup

│
├── shop/              # Product, Cart, Order logic

│
├── templates/         # HTML templates (Bootstrap-based)

│
├── static/            # CSS and other assets

│
├── db.sqlite3
├── manage.py
└── requirements.txt

Extras:

APIView-based views

Class-based views

HTML rendering from API views

## Setup Instructions
Clone the Repository:

git clone (https://github.com/Rakesh260/EA-TECH/)

Create and activate a virtual environment:

python -m venv env

source env/bin/activate 

Install dependencies:

pip install -r requirements.txt

Run Migrations:

python manage.py migrate

Create Superuser (for admin panel):

python manage.py createsuperuser


Run the Development Server:

python manage.py runserver





