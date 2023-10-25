# Application Name

This application is a comprehensive e-commerce platform offering a wide range of functionalities to users. It is built with Python Flask and uses PostgreSQL for the database.

## How to run

Start by running the setup_db.py file, and then start running the app.py.

## Test users
| Users | Username    | Password    |
| :---:   | :---: | :---: |
| Admin | admin   | 1234   |
| User | user1   | 1234   |

## Application Functionality

Here are the key functionalities implemented in this application:

- **User Authentication:** The application includes functionality for user registration and login. Passwords are securely hashed using Werkzeug's security module.

- **User Preferences:** User preferences, such as username and role, are stored in a session. Preferences for product filter types are stored in a cookie and are available when the user revisits the page.


- **Input Validation:** Certain validation rules are enforced on user input. For example, during registration, if the user tries to register a password with less than 5 characters, an error is displayed.

- **Store Page:** The store page displays products according to a filter type, which can be 'all', 'deal', or 'best-seller'. The filter preference is stored in a cookie for future visits.

- **Dynamic Discounts:** The store page calculates and displays the discount percentage for each product based on its original and current prices.

- **Shopping Cart:** Users can add items to a shopping cart. The application keeps track of what’s in a user’s cart even if they log out or leave the site. This feature uses session data for authenticated users and local storage for guest users.

- **Security Measures:** The application enforces strong security measures, such as two-factor authentication and data encryption, to protect user data and prevent unauthorized access.

## Admin Panel

### Features

- **User Management:** Admins can view a paginated list of all registered users along with their ID, username, and email. Admins have the power to update or delete user accounts.

- **Product Management:** Admins can view the details of each product, including ID, title, current price, original price, and whether the product is a best seller. They can also update the price of a product or add a new product to the store through modal interfaces.

- **Order Management:** Admins have an overview of all orders placed through the platform. This includes details such as order ID, the user who placed the order, the total price, and the status of the order. Admins can also update the status of an order.

- **File Upload:** The application allows for file uploads, specifically images for products. Uploaded images are stored in the static directory.

- **Data Visualization and Reporting for Admin:** Admins have access to advanced data visualization tools and reports that show sales, orders, and user registration trends.

## Frontend Overview

This application uses several technologies and features on the frontend:

- **Frontend Technologies:** The application uses Bootstrap 5.2.3 for styling and layout. It also includes custom CSS and JavaScript files located in the `static` directory. The JavaScript file is used for various frontend functionalities. 

- **Login Modal:** There is a modal for user login, which is shown when the "LOG IN" button is clicked.

- **Flash Messages:** The application displays flash messages to inform users about successful actions or errors. These messages are styled differently for success and error cases.

- **Navbar:** The application includes a responsive navbar that includes links to different parts of the website such as "STORE", "ABOUT US", and "CONTACT". For logged-in users, it also shows links to their "ACCOUNT" and "ORDERS". If the logged-in user is an admin, an "ADMIN" link is also displayed, which leads to the Admin Panel.

- **Information Modal:** There is a modal designed to show various kinds of information to the user.

- **Product Block:** There is a placeholder for a products section, which presumably will display the products offered in the store.

- **Main Content Block:** The main content of each page is loaded into a content block. This allows each page to have its own unique content while inheriting common elements from the base template.

## Directory Structure

- /static/: Contains all static files like CSS, JavaScript, and images.
- /templates/: Contains all HTML templates.
- app.py: The main application file.
- setup_db.py: A script for setting up the database.
- /migrations/: Contains the database migration files.

