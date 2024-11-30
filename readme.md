# Gas Utility Web Application

A web-based platform to manage customer service requests and support operations for a gas utility service provider. This application allows customers to submit service requests, track their status, and view their account information, while support staff can manage and update service request statuses.

### Prerequisites

To run this project, make sure you have the following software installed:

- Python 3.x
- pip (Python package manager)

### Steps to Install

**Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/gas-utility.git
   cd gas-utility
   ```

### Database Setup

1. **Make migrations**:

   ```bash
   python manage.py makemigrations
   ```

2. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

3. **Create a superuser** (for admin access):

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a user with admin privileges.

## Requirements

- Django 3.x or higher
- Python 3.x
- Database (SQLite is the default, but you can configure PostgreSQL or MySQL in the `settings.py` file)


## Usage

1. **Run the development server**:

   To start the development server and view the application in your browser:

   ```bash
   python manage.py runserver
   ```

2. **Access the application**:

   - For customers: Go to `http://127.0.0.1:8000/customer/` to submit service requests, track requests, and view account information.
   - For support: Go to `http://127.0.0.1:8000/support/` to manage service requests.

3. **Admin Panel**:
   Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials created earlier.

### Endpoints

- **Customer**:
  - `submit-request/`: Submit a service request.
  - `track-request/`: View the status of your submitted requests.
  - `account-info/`: View and manage your account information.

- **Support**:
  - `dashboard/`: Support representative dashboard to view and manage customer requests.
  - `customer-details/<int:customer_id>/`: View customer details associated with a request.
