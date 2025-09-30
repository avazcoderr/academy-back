# academy-back
Academy-back

Installation

To set up the project locally, follow these steps:

1. Clone the repository

    ```bash
    git@github.com:avazcoderr/academy-back.git
    cd academy-back
    ```

2. Create a virtual environment

    ```bash
    python3 -m venv venv
    source venv/bin/activate # For Windows, use `venv\Scripts\activate`
    ```

3. Install required packages

    ```bash
    pip install -r requirements.txt
    ```   

4. PostgreSQL setup

Install PostgreSQL and create database:

```bash
# Install PostgreSQL (Ubuntu/Debian)
sudo apt update
sudo apt install postgresql postgresql-contrib

# Create database
sudo -u postgres psql
CREATE DATABASE my_db;
CREATE USER pharma_user WITH PASSWORD 'your_strong_password';
GRANT ALL PRIVILEGES ON DATABASE my_db TO my_user;
\q
```

5. Configure Environment Variables
Rename the .env.example file to .env and replace your_secret_key with your actual Django secret key, along with any other necessary environment-specific values:

    ```bash
    SECRET_KEY=your_secret_key
    ```

6. Apply migrations

    ```bash
    python manage.py migrate
    ```

7. Create a superuser

    ```bash
    python manage.py createsuperuser
    ```

8. Run the project

    ```bash
    python manage.py runserver
    ```
   
Usage

After starting the project, you can access the following URLs:

    http://localhost:8000/ - Home page
    http://localhost:8000/admin/ - Admin panel

