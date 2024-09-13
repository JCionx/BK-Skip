# Use a Python base image
FROM mcr.microsoft.com/playwright/python:v1.45.1-jammy

# Set the working directory
WORKDIR /opt/app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy your Python application
COPY main.py /opt/app/main.py
COPY icon.png /opt/app/icon.png
COPY img_pt.png /opt/app/img_pt.png
COPY Helvetica.ttf /opt/app/Helvetica.ttf

# Expose the port for your application (adjust if needed)
EXPOSE 8080

# Command to run the Python application
CMD ["python", "/opt/app/main.py"]
