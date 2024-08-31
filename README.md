
# Project Name

A content publishing platform designed for TC and its various departments, enabling users to create, share, and engage with articles, similar to Medium.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Environment Variables](#environment-variables)
6. [Usage](#usage)
7. [Running Tests](#running-tests)
8. [Deployment](#deployment)
9. [Contributing](#contributing)

## Introduction

This project is a [Django REST Framework](https://www.django-rest-framework.org/) application with the following services:

- **Docker**: Containerization of the application.
- **Nginx**: A web server that serves static files and proxies requests to Django.
- **Mailhog**: A tool to test email sending locally.
- **Celery**: A task queue to handle asynchronous tasks.
- **PostgreSQL**: A relational database.

## Features

- RESTful API endpoints built with Django REST Framework.
- Asynchronous task handling using Celery.
- Dockerized environment for easy setup and deployment.
- Local email testing with Mailhog.
- Production-ready deployment configuration using Nginx.

## Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/oseni99/DRF-School-Medium.git
   ```

2. **Build and start the Docker containers**:

   ```bash
   docker-compose up --build -d
   ```

3. **Apply migrations**:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Create a superuser**:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

## Environment Variables

You will need to configure the following environment variables in a `.env` file at the root of your project:

```plaintext
# Django settings
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1

# Database settings
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Celery settings
CELERY_BROKER_URL=redis://redis:6379/0
```

## Usage

1. **Access the Django application**:
   - The API will be available at `http://localhost:8000/`.

2. **Access the Mailhog interface**:
   - Mailhog can be accessed at `http://localhost:8025/`.

3. **View Celery task results**:
   - Celery tasks will be managed by the `celery` service defined in `docker-compose.yml`.

4. **Access Nginx**:
   - Nginx will be configured to serve the Django application and static files.

## Running Tests

To run the tests, use the following command:

```bash
docker-compose exec web python manage.py test
```

## Deployment

For deployment, consider the following steps:

1. **Set up your production environment**:
   - Update the `.env` file with production settings.

2. **Run Docker Compose with the production configuration**:

   ```bash
   docker-compose -f docker-compose.prod.yml up --build -d
   ```

3. **Configure Nginx for production**:
   - Update the Nginx configuration in `docker/nginx/default.conf` as needed.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.
