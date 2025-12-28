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