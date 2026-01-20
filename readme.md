# Flask – Getting Started

This project demonstrates a basic Flask application with simple routing and JSON responses.
It is intended as a beginner-friendly setup for learning Flask fundamentals as part of a course.

---

## Prerequisites

- Python 3.8+
- pip (Python package manager)

Check Python version:

python --version

---

## Create a Virtual Environment

python -m venv venv

Activate the virtual environment:

Windows:
venv\Scripts\activate

macOS / Linux:
source venv/bin/activate

---

## 📚 Dependency Management

### Save dependencies
```bash
pip freeze > requirements.txt
```

### Restore dependencies
```bash
pip install -r requirements.txt
```
---

## Install Flask

pip install Flask

(Optional) Save dependencies to a file:

pip freeze > requirements.txt

---

## Project Structure

.
├── hello.py
├── requirements.txt
└── README.md

---

## Flask Application (hello.py)

from flask import Flask

app = Flask(__name__)  # __name__ refers to the current file (hello.py)

@app.route("/")
def hello():
    """
    Root endpoint.
    Called automatically when the user visits "/".
    """
    return "Hello, there.!"

@app.route("/ping", methods=["GET", "POST"])
def ping():
    """
    Ping endpoint.
    Responds to GET and POST requests.
    """
    return {"message": "why are you pinging me?"}

if __name__ == "__main__":
    # debug=True enables auto-reload and detailed error messages
    app.run(debug=True)

---

## Run the Application

Option 1: Using Python

python hello.py

Option 2: Using Flask CLI (Recommended)

flask --app hello run

The application will be available at:

http://127.0.0.1:5000

---

## Available Endpoints

/        GET        Returns a greeting message
/ping    GET, POST  Returns a JSON response

---

## Notes

- debug=True enables:
  - Automatic server reload on code changes
  - Detailed error pages for development
- Do not use debug=True in production environments

---

## Next Steps

- Learn Flask request handling (request, response)
- Add URL parameters and query strings
- Use Flask Blueprints for better project structure
- Connect a database using SQLAlchemy
- Build REST APIs with Flask

---

## Resources

Flask Documentation:
https://flask.palletsprojects.com/

---

Happy coding!


# colab notebook
https://colab.research.google.com/drive/126GHpghQWbs7us91zyu4uoOGtobbfUkt

# docker setup
- install docker and sign up
create the "Dockerfile"
'''
FROM python:3.13.4-slim-bookworm
WORKDIR /docker

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY ./ ./

CMD ["python", "-m", "flask", "--app", "loan", "run", "--host", "0.0.0.0", "--port", "8080"]
'''
# create a docker build
-this will create a docker image
'''
docker build -t flask_loan_app .   
'''
# check the images
docker images 

# run the the image
docker run -p 8080:5000 flask_loan_app  

# aws deployment ecr & ecs

## Install or update the AWS CLI
'''
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi /qn
aws --version
'''

## create a IAM user and get the access keygive these permissions
- AmazonEC2ContainerRegistryFullAccess
- AmazonEC2ContainerRegistryPowerUser
- AmazonECS_FullAccess
- AmazonECSTaskExecutionRolePolicy
- AmazonS3FullAccess
- AmazonSageMakerFullAccess
- IAMFullAccess
- IAMReadOnlyAccess
- IAMUserChangePassword
'''
aws configure
aws sts get-caller-identity
'''

## now login to ecr (docker setup should be ready locally and running)
'''
aws ecr get-login-password --region ap-south-2 | docker login --username AWS --password-stdin 289221384679.dkr.ecr.ap-south-2.amazonaws.com
docker build -t flask-app .
docker tag flask-app:latest 289221384679.dkr.ecr.ap-south-2.amazonaws.com/flask-app:latest
aws ecr create-repository `--repository-name flask-app` --region ap-south-2
docker push 289221384679.dkr.ecr.ap-south-2.amazonaws.com/flask-app:latest
'''


