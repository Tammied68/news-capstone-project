# 📰 News Management System (Capstone Project)

## Repository

Github Repository:
https://github.com/Tammied68/news-capstone-project

## 📌 Overview

This project is a Django-based News Management System developed as part of a capstone assignment. It demonstrates full-stack web development skills including authentication, role-based access control, REST APIs, documentation, version control, and containerization.

A role-based News Publishing Platform built with Django, Django REST Framework, and MariaDB.

The system supports multiple user roles and allows controlled creation, approval, and consumption of news articles.



## ✨ Features

### 👥 User Roles

* **Reader**

  * View approved articles
  * Subscribe to publishers and journalists

* **Journalist**

  * Create and manage articles
  * Submit articles for approval

* **Editor**

  * Review and approve submitted articles

* **Admin**

  * Full access via Django admin panel



### 📰 Article Workflow

1. Journalist creates an article
2. Article is marked as **pending**
3. Editor reviews and approves the article
4. Approved articles become visible to readers



### 🔐 Authentication

* Django built-in authentication system
* Login is **username-based**
* Role-based access control enforced


### 🌐 API

* Endpoint: `/api/subscribed-articles/`
* Returns articles based on user subscriptions
* Requires API key via `X-API-KEY` header


## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite
* Docker
* Git & GitHub
* Sphinx (documentation)


## ⚙️ Setup with Virtual Environment

```bash
# Clone the repository
git clone https://github.com/Tammied68/Capstone-Project-Consolidation.git

cd Capstone-Project-Consolidation
```


# Activate environment
source venv312/bin/activate   # Mac/Linux
venv312\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

## Database Configuration

This project uses SQLite as the default database.

Database migrations can be applied using:

```bash
python manage.py migrate
```

No additional database server configuration is required.

# Run migrations
python manage.py migrate

# Run server
python manage.py runserver


## 🐳 Running with Docker
Build the Docker image:

docker build -t news_capstone .

Run the Docker container:

docker run --rm -p 8000:8000 news_capstone

Access the application:

http://127.0.0.1:8000/
## 🐳 Docker Verification
Docker containerization was successfully verified for this project.

Verification steps completed:

Docker image built successfully.
Django application started successfully inside the container.
System checks completed without errors.
Application was accessible through port 8000.
MariaDB configuration was successfully used by the application.

Verification output:

System check identified no issues (0 silenced).
Starting development server at http://0.0.0.0:8000/
Build:



> Passwords can be reset using:

docker exec -it <container_name> python manage.py changepassword <username>


## 📚 Documentation was generated using Sphinx.

To rebuild documentation:

```bash
cd docs
sphinx-apidoc -o source ../
make html
```

Generated files can be found in:

```text
docs/build/html/
```

## 📦 Project Structure


accounts/       # Custom user model & roles
news/           # Core application logic
docs/           # Sphinx-generated documentation
Dockerfile      # Container configuration
requirements.txt
README.md
capstone.txt


## 🔄 Version Control

This project uses Git with structured branching:

* `main` → final merged project
* `docs` → documentation and docstrings
* `container` → Docker setup

## ⚠️ Notes

* Do not commit sensitive data (e.g., API keys, passwords)
* Uses SQLite for simplicity
* Authentication uses **username**, not email

## 📌 Capstone Submission

This repository fulfills the following requirements:

* Version control with Git
* Branching strategy (`docs`, `container`)
* Documentation using Sphinx
* Docker containerization
* Requirements file for dependencies


## Screenshots

### REST API Authentication and Successful Response

Demonstrates API key authentication and successful retrieval of approved subscribed articles.

![REST API Authentication and Response](image-1.png)

### REST API Unit Tests

Demonstrates successful execution of the Django REST Framework API test suite.

![REST API Unit Tests](image-2.png)

### MariaDB Database Verification

Demonstrates successful MariaDB configuration and creation of the `news_capstone_db` database used by the application.

![MariaDB Database Verification](image-3.png)



## 👩‍💻 Author

Tammie Davis

University of Chicago | HyperionDev Software Engineering Bootcamp Capstone Project
