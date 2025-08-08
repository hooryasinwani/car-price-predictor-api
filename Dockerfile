# version of Python
FROM python:3.10-slim

# Setting the working directory inside the container to /app
WORKDIR /app

# Copying the requirements file in first
COPY requirements.txt .

# Installing all the libraries from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# copying all your project files 
COPY . .

# Telling Docker the app will listen on port 5001
EXPOSE 5001

# command to run when the container starts
CMD ["python", "api.py"]