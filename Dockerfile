<<<<<<< HEAD
# Base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Set the command to run the Flask app
CMD ["flask", "run", "--host", "0.0.0.0"]
=======
# Base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app


# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Set the command to run the Flask app
CMD ["flask", "run", "--host", "0.0.0.0"]
>>>>>>> c9a1bd2d4a3a94049529156193b42d5741fcb8c7
