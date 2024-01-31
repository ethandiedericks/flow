![Budget Page Image](https://raw.githubusercontent.com/ethandiedericks/flow/main/budget-page-readme-image.png)

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

1. Clone the repository:
   ```bash
   git clone https://github.com/ethandiedericks/flow.git
   ```
2. Enter flow directory:
   ```bash
   cd flow
   ```
3. Create a virtual environment: (mac)
   ```bash
   python3 -m venv .venv
   ```
4. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Create a copy of the .env.template file and name it .env:
   ```bash
   cp .env.template .env
   ```
7. Configure the .env file: 
    ```bash
    DJANGO_SECRET_KEY=your_secret_key_here
    DJANGO_DEBUG=True
    EMAIL_HOST=your_email_host
    EMAIL_HOST_USER=your_email_host_user
    EMAIL_HOST_PASSWORD=your_email_host_password
    EMAIL_PORT=your_email_port
    EMAIL_USE_TLS=True
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    DEFAULT_FROM_EMAIL=your_email
    ```
8. Make migrations:
   ```bash
   python manage.py makemigrations
   ```
9. Apply migrations:
   ```bash
    python manage.py migrate
    ```
10. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
11. Start the development server:
    ```bash
    python manage.py runserver
    ```
