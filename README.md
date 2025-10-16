Simple Django Blog Application

This project is a beginner-friendly blog application built with the Django web framework. It serves as a practical, hands-on exercise for developers who want to solidify their understanding of core concepts like the Model-View-Template (MVT) architecture, user authentication, and consuming external APIs.

Features Implemented

Full User Authentication: Users can register for a new account and log in to access protected content.

Protected Content: The main blog post list is only visible to authenticated users.

Post Management (Admin): Blog posts are created and managed through the built-in Django admin panel.

Dynamic Content via API: The user's welcome page displays a random inspirational quote by consuming the public ZenQuotes API.

Tech Stack

Backend: Python 3, Django

Database: SQLite 3 (Default)

API Interaction: requests library

Frontend: HTML5, CSS3

⚙️ Setup and Installation

To get this project running locally, follow these steps:

Clone the Repository

git clone [https://github.com/your-username/simple-django-blog.git](https://github.com/your-username/simple-django-blog.git)
cd simple-django-blog


Create and Activate a Virtual Environment

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# On Windows
python -m venv .venv
.venv\Scripts\activate


Install Dependencies
This command will read the requirements.txt file and install Django and the requests library.

pip install -r requirements.txt


Apply Database Migrations

python manage.py migrate


Create a Superuser
This allows you to access the admin panel to create blog posts.

python manage.py createsuperuser


Run the Development Server

python manage.py runserver


The application will be available at http://127.0.0.1:8000/.

🚀 Usage

Create Blog Posts: Navigate to the admin panel (/admin/), log in with your superuser, and create a few sample posts.

Register a User: Go to /posts/register/ to create a new user account.

Log In: Go to /posts/login/ and log in with your new user. You will be redirected to a welcome page that displays the "Quote of the Day."

View Posts: From the welcome page, you can navigate to the main blog page to see the protected list of posts.
