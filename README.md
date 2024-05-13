# DoDo App

DoDo is a web-based todo application built using Django and Django REST Framework (DRF). Originally developed as an assignment for Continious Integration.

## Assignment

Develop a CI pipeline for this app which includes the following features

- Run when a PR is created with `develop` as base branch.
- Run when a Push event happens in `develop` branch.
- Run migrations in pipeline.
- Run unit tests.
- If a test fails, send a failure message in slack and terminate the pipeline.
- If and only if all test cases pass, push the docker image to dockerhub.
- Send a slack message in channel after the successful completion of pipeline.

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL

### Installation

As a best practice, it is advised to create a virtual environment to store this project's dependencies separately. You can install virtualenv with

1. Install virtualenv (optional)
    ```bash
    pip install virtualenv
    ```
2. Clone the repository.
   ```bash
   git clone https://github.com/abdullahxz/DoDo.git
   ```
3. cd into repo directory.
   ```bash
   cd DoDo
   ```
4. Create env (optional)
   ```bash
   python -m venv env
   ```
5. Activate virtualenv (optional)
   ```bash
   source env/bin/activate
   ```
6. Install depndencies
    ```bash
    pip install -r requirements.txt
    ```
7. Make sure you have a `.env` file with following variables.
    ```
    DB_NAME = xxx
    DB_USER = xxx
    DB_PASSWORD = xxx
    DB_HOST = xxx
    DB_PORT = xxx
    ```
8. Apply migrations
    ```bash
    python manage.py migrate
    ```
9. Seed data into database for development environment
    ```bash
    python manage.py seed_data
    ```
10. Run dev server
    ```bash
    python manage.py runserver
    ```
