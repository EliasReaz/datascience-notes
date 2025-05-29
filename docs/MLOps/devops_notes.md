# 📁 MLOps Basics: Docker, FastAPI, and Flask

Welcome! This guide explains essential backend tools:

* 🚢 **Docker**: Package and run your apps anywhere
* ⚡ **FastAPI**: Fast, async-ready web APIs
* 🔥 **Flask**: Lightweight web apps and APIs

---

## 🚢 Docker

### What is Docker?

Docker is like a **magic container box** that carries your app and everything it needs (code, Python, libraries) so it runs **anywhere** - your laptop, server, or the cloud.

### When to Use Docker

* You want to **share your project** easily with someone else.
* Your app works on your machine, but not on someone else's.
* You're deploying your app to a cloud service.

---

### 🔍 Key Concepts

| Term           | What It Means                                            |
| -------------- | -------------------------------------------------------- |
| **Image**      | A snapshot/blueprint of your app and everything it needs |
| **Container**  | A running instance of an image                           |
| **Dockerfile** | A script with steps to create an image                   |

---

### 📂 Sample Dockerfile

```Dockerfile
# Use the official Python image from Docker Hub
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the default command to run the app
CMD ["python", "app.py"]
```

---

### ⚖️ Docker Commands

#### Build Docker Image:

```bash
docker build -t myapp .
```

* `-t myapp`: names the image `myapp`
* `.`: current directory contains the Dockerfile

#### Run Docker Container:

```bash
docker run -p 8000:8000 myapp
```

* `-p 8000:8000`: maps your computer's port 8000 to Docker's port 8000

#### Run Python Shell Inside Docker

```bash
docker run -it python:3.10
```

* `-it`: interactive terminal
* Opens Python shell inside a container

#### Mount Local Folder into Container

```bash
docker run -v $(pwd):/app -w /app python:3.10 python app.py
```

* `-v $(pwd):/app`: mounts your current folder to `/app` inside container
* `-w /app`: sets the working directory

---

## ⚡ FastAPI

### 🤔 What is FastAPI?

FastAPI is a Python web framework used to build APIs that are fast, async, and come with automatic documentation.

FastAPI is a fast, modern way to build APIs with Python. It's like building an express highway 🚗 for your data.

### When to Use FastAPI

* You need a REST API for your app or machine learning model.
* You want built-in docs (OpenAPI, Swagger).
* You care about speed and async support.

### How to Use

#### Step 1: Install FastAPI and Uvicorn

```bash
pip install fastapi uvicorn
```

#### Step 2: Create main.py

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}
```

#### Step 3: Run the App

```bash
uvicorn main:app --reload
```

#### Example Use Case

* You built a machine learning model and want to expose a `/predict` endpoint for it. FastAPI makes this super easy.

---

| Term         | What It Means                                               |
| ------------ | ----------------------------------------------------------- |
| **API**      | A way to connect programs (like a menu at a restaurant)|
| **Endpoint** | A specific URL that your app listens to (e.g. `/predict`)   |
| **GET/POST** | Types of HTTP requests (read vs. send data)                 |
| **Pydantic** | Helps validate data like forms with rules                   |
| **Uvicorn**  | The web server that runs FastAPI                            |

---

### 🔹 A Sample `main.py` with Comments

```python
# Import FastAPI library
from fastapi import FastAPI

# Create the FastAPI app instance
app = FastAPI()

# Define a GET endpoint for the homepage
@app.get("/")
def home():
    # Return a JSON response
    return {"message": "Hello FastAPI"}

# Define a GET endpoint with a path parameter
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

# Use a query parameter with a default value
@app.get("/search")
def search(q: str = "default"):
    return {"result": q}

# Use a POST endpoint with data validation
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    # Pydantic auto-validates the item structure
    return {"item": item}
```

---

### 🔧 Run FastAPI App

```bash
uvicorn main:app --reload
```

* `main:app`: file name = `main.py`, object = `app`
* `--reload`: restarts server on code changes

---

#### 📂 Dockerfile for FastAPI

```Dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### 🧪 Docker + FastAPI Example

#### requirements.txt

```bash
fastapi
uvicorn
```

#### Build and Run

```bash
docker build -t fastapi-app .        # Swagger UI
docker run -p 8000:8000 fastapi-app  # FastAPI homepage
```

#### Access (FastAPI)

* http://localhost:8000/docs → Swagger UI

* http://localhost:8000 → FastAPI homepage

---

## 🔥 Flask

### 🤔 What is Flask?

Flask is a minimal Python web framework. You can build anything: a website, API, or dashboard.

It’s like a barebones food truck 🍔 where you add features as you need.

---
| Term          | Meaning                                     |
| ------------- | ------------------------------------------- |
| **Route**     | A URL that triggers a function              |
| **Template**  | HTML file rendered dynamically              |
| **Flask App** | Main object that connects routes to logic   |
| **Flask CLI** | Command line tool to run apps (`flask run`) |

---

### 🔹 Sample `app.py` with Comments

```python
# Import Flask class
from flask import Flask, jsonify, render_template

# Create the Flask app instance
app = Flask(__name__)

# Define a basic homepage route
@app.route("/")
def hello():
    return "Hello from Flask!"

# Define a route with a variable path
@app.route("/hello/<name>")
def greet(name):
    return f"Hello, {name}!"

# Define a JSON API endpoint
@app.route("/api")
def api_data():
    return jsonify({"data": 123})

# Render HTML from a template
@app.route("/home")
def home():
    return render_template("home.html")
```

---

### 🔧 Run Flask App

```bash
export FLASK_APP=app.py
flask run
```

---

### 📂 Dockerfile for Flask

```Dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]
```

#### 🧪 Docker + Flask Example

#### requirements.tx

```bash
flask
```

#### Build and Run Flask

```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```
```
#### Access (Flask)

* http://localhost:5000 → Flask homepage
---

## 📚 Summary Table

| Tool    | Purpose                     | Common Use                             |
| ------- | --------------------------- | -------------------------------------- |
| Docker  | Package apps + environments | Make sure apps run the same everywhere |
| FastAPI | High-speed web APIs         | ML models, web APIs with docs          |
| Flask   | Lightweight web framework   | Quick websites, APIs, dashboards       |

---
