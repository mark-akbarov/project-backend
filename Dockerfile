# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables for Django settings (optional)
ENV DJANGO_SETTINGS_MODULE=myapp.settings.production

# Set working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run your application
CMD ["gunicorn", "myapp.wsgi:application", "--bind", "0.0.0.0:8000"]
