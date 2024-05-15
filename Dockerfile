# Use the official Python image as the base image
FROM python:3.10

# Set environment variables for PostgreSQL
ENV DB_NAME: ${{ secrets.DB_NAME }}
ENV DB_USER: ${{ secrets.DB_USER }}
ENV DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
ENV DB_HOST: ${{ secrets.DB_HOST }}
ENV DB_PORT: ${{ secrets.DB_PORT }}

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Apply migrations
RUN python manage.py migrate

# Seed data into the database (optional)
# RUN python manage.py seed_data

# Run unit tests (optional)
# RUN python manage.py test

# Expose the port where the Django development server will run
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
