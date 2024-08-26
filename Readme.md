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

## SQL Assignment

As part of this project, we have a SQL assignment to analyze customer spending patterns. Here's the task:

Write a SQL query to find the top 5 customers who have spent the most money on the platform. The output should include the following columns: customer_id, customer_name, email, total_spent, and most_purchased_category (the category of products they spent the most money on).

Here's a sample solution:

```sql
SELECT 
    c.customer_id,
    c.customer_name,
    c.email,
    SUM(oi.quantity * oi.price_per_unit) AS total_spent,
    MAX(p.category) AS most_purchased_category
FROM 
    Customers c
JOIN 
    Orders o ON c.customer_id = o.customer_id
JOIN 
    Order_Items oi ON o.order_id = oi.order_id
JOIN 
    Products p ON oi.product_id = p.product_id
WHERE 
    o.order_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY 
    c.customer_id, c.customer_name, c.email
ORDER BY 
    total_spent DESC
LIMIT 5;
```

This query assumes the following:
- We have tables named Customers, Orders, Order_Items, and Products.
- We're considering orders from the last year only.
- The most_purchased_category is determined by the category with the highest total spend.

Note: Depending on your specific database schema, you might need to adjust the table and column names accordingly.

## Security Considerations

- Always use HTTPS in production
- Keep your `SECRET_KEY` in `settings.py` confidential
- Regularly update dependencies to patch security vulnerabilities

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)