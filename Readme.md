### accounts/README.md

# Accounts App

This Django app handles user authentication for the E-commerce Analysis project.

## Features

- User signup
- User login
- JWT token generation and refresh

## API Endpoints

- `/signup/`: POST request to create a new user account
- `/login/`: POST request to log in and obtain JWT tokens
- `/token/`: POST request to obtain a new pair of JWT tokens
- `/token/refresh/`: POST request to refresh an existing JWT token

## Usage

### Signup

```
POST /accounts/signup/
{
  "username": "your_username",
  "password": "your_password"
}
```

### Login

```
POST /accounts/login/
{
  "username": "your_username",
  "password": "your_password"
}
```

### Obtain new token pair

```
POST /accounts/token/
{
  "username": "your_username",
  "password": "your_password"
}
```

### Refresh token

```
POST /accounts/token/refresh/
{
  "refresh": "your_refresh_token"
}
```

## Authentication

This app uses JWT (JSON Web Tokens) for authentication. After logging in or signing up, you will receive an access token and a refresh token. Include the access token in the Authorization header of your requests:

```
Authorization: Bearer <your_access_token>
```

When the access token expires, use the refresh token to obtain a new pair of tokens.

# Products App

This Django app manages product data and analysis for the E-commerce Analysis project.

## Features

- CSV file upload for product data
- Data cleaning and preprocessing
- Summary report generation

## Models

### Product

- `product_id`: CharField
- `product_name`: CharField
- `category`: CharField
- `price`: DecimalField
- `quantity_sold`: IntegerField
- `rating`: FloatField
- `review_count`: IntegerField

## API Endpoints

- `/upload-data/`: POST request to upload CSV file (requires authentication)
- `/clean-data/`: POST request to clean and preprocess data (requires authentication)
- `/summary-report/`: GET request to generate and download the summary report (requires authentication)

## Usage

### Upload Data

```
POST /products/upload-data/
Headers: Authorization: Bearer <access_token>
Body: Form-data with key 'file' and value as the CSV file
```

### Clean Data

```
POST /products/clean-data/
Headers: Authorization: Bearer <access_token>
```

### Generate Summary Report

```
GET /products/summary-report/
Headers: Authorization: Bearer <access_token>
```

## Data Format

The CSV file for data upload should contain the following columns:
- product_id
- product_name
- category
- price
- quantity_sold
- rating
- review_count

## Summary Report

The generated summary report will be a CSV file containing:
- category
- total_revenue
- top_product (the product name of the highest selling product in that category)
- top_product_quantity_sold


# E-commerce Analysis Django Application

This Django application provides an API for uploading, cleaning, and analyzing e-commerce product data. It includes user authentication, data management, and report generation features.

## Project Structure

This project is organized into multiple Django apps:

1. `accounts`: Handles user authentication
2. `products`: Manages product data and analysis

For detailed information about each app, please refer to their respective README files:

- [Accounts App README](./accounts/README.md)
- [Products App README](./products/README.md)

## Features

- User signup and login with JWT authentication
- CSV file upload for product data
- Data cleaning and preprocessing
- Summary report generation

## Prerequisites

- Python 3.8+
- MySQL 5.7+

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/https://github.com/AmanGupta0112/ecommerce-analysis.git
   cd ecommerce-analysis
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install django djangorestframework djangorestframework-simplejwt mysqlclient pandas
   ```

4. Create a MySQL database named `ecommerce_analysis`.

5. Update the database configuration in `ecommerce_analysis/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'ecommerce_analysis',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

6. Add the `accounts` and `products` apps to your `INSTALLED_APPS` in `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'accounts',
       'products',
       'rest_framework',
       'rest_framework_simplejwt',
   ]
   ```

7. Configure JWT settings in `settings.py`:
   ```python
   from datetime import timedelta

   SIMPLE_JWT = {
       'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
       'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
   }
   ```

8. Include the app URLs in your main `urls.py`:
   ```python
   from django.urls import path, include

   urlpatterns = [
       path('accounts/', include('accounts.urls')),
       path('products/', include('products.urls')),
   ]
   ```

9. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

## Usage

1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. Use the API endpoints as described in the app-specific README files.

## Security Considerations

- Always use HTTPS in production
- Keep your `SECRET_KEY` in `settings.py` confidential
- Regularly update dependencies to patch security vulnerabilities

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
