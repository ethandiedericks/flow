# Flow Finance

Flow Finance is a Django-based financial management system that allows users to track their income, expenses, and investments through a structured database model.

## Introduction

Flow Finance provides a robust platform for users to manage their financial transactions efficiently. With its Django-powered backend, it ensures a secure and structured approach to handling income, expenses, and investments.

## Features

- **Transaction Tracking:** Easily record income, expenses, and investments.
- **User-Centric:** Every transaction is associated with the respective user.
- **Flexible Source Management:** Classify transactions based on income sources, expense sources, and investment sources.
- **Date Management:** Track transaction dates and schedule future transactions.

## Installation

To set up Flow Finance locally, follow these steps:

1. Clone the repository: `git clone https://github.com/ethandiedericks/flow.git`
2. Create a virtual environment: (mac)`python3 -m venv .venv` 
3. Activate the virtual environment: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Configure your django secret key and debug settings in `settings.py`
6. Make migrations: `python manage.py makemigrations`
7. Apply migrations: `python manage.py migrate`
8. Create a superuser: `python manage.py createsuperuser`
9. Start the development server: `python manage.py runserver`