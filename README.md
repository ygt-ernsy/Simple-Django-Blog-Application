Simple Django Blog Application

This project is a beginner-friendly blog application built with the Django web framework. It serves as a practical, hands-on exercise for developers who have completed the official Django tutorial and want to solidify their understanding of core concepts like the Model-View-Template (MVT) architecture, the Django ORM, and user authentication.

Features Implemented

As of the current version, the application supports the following features:

User Account Creation: New users can create an account through a public-facing registration page.

Secure User Login: Registered users can log in to access protected content.

Protected Content: The main blog post index and detail pages are only accessible to authenticated users.

Blog Post Display:

Logged-in users can view a list of the most recent blog posts.

Users can click on any post title to view its full content on a dedicated detail page.

Admin Post Management: A superuser can create, read, update, and delete blog posts using the built-in Django admin interface.

Tech Stack

Backend: Python 3, Django

Database: SQLite 3 (Default for development)

Frontend: HTML5, CSS3

⚙️ Setup and Installation

To get this project running locally, follow these steps:

Clone the Repository

git clone [https://github.com/your-username/simple-django-blog.git](https://github.com/your-username/simple-django-blog.git)
cd simple-django-blog


Create and Activate a Virtual Environment

On macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate


On Windows:

python -m venv .venv
.venv\Scripts\activate


Install Dependencies

pip install Django


Apply Database Migrations
This will create the necessary database tables for posts and users.

python manage.py migrate


Create a Superuser
This will allow you to access the admin panel and create your first blog posts.

python manage.py createsuperuser


Run the Development Server

python manage.py runserver


The application will be available at http://127.0.0.1:8000/.

🚀 Usage

Create Blog Posts:

Navigate to the admin panel at http://127.0.0.1:8000/admin/.

Log in with the superuser credentials you created.

In the "Posts" section, create 2-3 sample blog posts.

Create a User Account:

Navigate to the registration page at http://127.0.0.1:8000/posts/register/.

Fill out the form to create a new user account.

Log In and View Posts:

Go to the login page at http://127.0.0.1:8000/posts/login/.

Log in with your newly created user.

You will be redirected to a welcome page. From there, you can navigate to the main blog page to view the posts you created in the admin panel.

🚧 Next Steps

This project is a work in progress. The immediate next step is to complete the authentication flow:

Implement User Logout Functionality: Add the final piece to the user session management.
