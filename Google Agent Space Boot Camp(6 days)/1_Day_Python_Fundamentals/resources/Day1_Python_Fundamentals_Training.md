# 🐍 Day 1: Python Fundamentals & Project Foundation

## 🎯 Key Objectives
By the end of this session, you will be able to:
1. Write clean, reusable, enterprise-level Python code using **Object-Oriented Programming (OOP)**.
2. Understand how **APIs** and **JSON** are used for microservice communication.
3. Set up a **local Python + GCP environment** for scalable cloud integrations.

---

## 🧠 Section 1: Theory — Core Concepts

### 1️⃣ Python Architecture for Enterprise
Enterprise systems rely on modular architecture. Python projects should be organized into packages, modules, and classes for better scalability, testability, and reusability.

Key design rules:
- Follow **Single Responsibility Principle (SRP)**.
- Use **classes** to encapsulate business logic.
- Avoid hardcoding values — use configuration files or environment variables.

Example enterprise folder structure:
```
project_root/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── user.py
│   │   └── product.py
│   ├── api/
│   │   └── main.py
│   └── utils/
│       └── file_handler.py
├── requirements.txt
└── README.md
```

---

### 2️⃣ The Three Pillars of OOP

| Concept | Description | Example |
|----------|--------------|----------|
| **Encapsulation** | Restricting access to certain object components | Private variables and getter/setter methods |
| **Inheritance** | Creating new classes from existing ones | Child classes reusing parent functionality |
| **Polymorphism** | Same interface, different behavior | Overriding methods across subclasses |

#### 📘 Example 1: Encapsulation
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("Nuthan", 1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
```

#### 📘 Example 2: Inheritance & Polymorphism
```python
class Employee:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Employee"

class Manager(Employee):
    def get_role(self):
        return "Manager"

class Developer(Employee):
    def get_role(self):
        return "Developer"

employees = [Manager("Nina"), Developer("Alex")]
for e in employees:
    print(f"{e.name} is a {e.get_role()}")
```

Output:
```
Nina is a Manager
Alex is a Developer
```

---

### 3️⃣ JSON and APIs
**JSON (JavaScript Object Notation)** is a lightweight data format used in web services for structured communication.

#### Example: JSON Basics
```python
import json

data = {"name": "Nuthan", "skills": ["Python", "GCP", "GenAI"]}
json_str = json.dumps(data)  # Convert dict to JSON
print(json_str)

parsed = json.loads(json_str)  # Convert back to dict
print(parsed["skills"][0])
```

#### Common HTTP Methods in REST APIs
| Method | Purpose |
|--------|----------|
| GET | Retrieve data |
| POST | Create new resource |
| PUT | Update an existing resource |
| DELETE | Remove a resource |

---

### 4️⃣ Virtual Environments
A **virtual environment** ensures isolated dependencies for your project.

#### Commands
```bash
python -m venv myenv
myenv\Scripts\activate   # Windows
source myenv/bin/activate  # Linux/Mac
pip install flask google-cloud-storage requests
```

---

### 5️⃣ Using the `requests` Library
This library allows your Python code to interact with REST APIs.

#### Example: Fetch Weather Data
```python
import requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true")
data = response.json()

print("Temperature:", data["current_weather"]["temperature"], "°C")
```

---

## 🧩 Section 2: Real-World Projects

### 🏢 Example 1: Enterprise Order Processing
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def total(self):
        return sum(p.price * q for p, q in self.items)

laptop = Product("Laptop", 90000)
mouse = Product("Mouse", 2000)

order = Order()
order.add_item(laptop, 1)
order.add_item(mouse, 2)

print("Total Order Value:", order.total())
```

### 🌦️ Example 2: Weather Alert Script
```python
import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()
    current = data["current_condition"][0]
    temp = current["temp_C"]
    return f"The temperature in {city} is {temp}°C"

print(get_weather("Bangalore"))
```

---

## 🧪 Section 3: Hands-on Labs

### Lab 1.1: Environment Setup
1. Install Python 3.10+
2. Create virtual environment and activate it.
3. Install SDKs:
   ```bash
   pip install google-cloud-storage fastapi uvicorn
   gcloud init
   ```

---

### Lab 1.2: OOP Project
```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

user = User("Nuthan", "nuthan@example.com")
product = Product("AI Course", 5000)

print(f"{user.name} bought {product.name} for ₹{product.price}")
```

---

### Lab 1.3: FastAPI Mock API
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Laptop", "price": 90000},
        {"id": 2, "name": "Mouse", "price": 2000}
    ]
```

Run:
```bash
uvicorn main:app --reload
```
Then open http://127.0.0.1:8000/products

---

## 🧩 Mini Quiz
1. Why use a virtual environment?  
   → To isolate dependencies per project.  
2. Three pillars of OOP?  
   → Encapsulation, Inheritance, Polymorphism.  
3. What does POST signify?  
   → It’s used to create new resources on the server.

---

## 💻 Coding Tasks

| Difficulty | Task | Description |
|-------------|------|--------------|
| 🟢 Easy | CSV → JSON | Convert CSV file to JSON using `csv` and `json` modules |
| 🟡 Medium | API Error Handling | Add `try...except` to FastAPI endpoints |
| 🔴 Advanced | Consume API | Use `requests` to fetch external API and model data using OOP |

#### Example (Easy Task)
```python
import csv, json

def csv_to_json(csv_file, json_file):
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        data = list(reader)
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)

csv_to_json("products.csv", "products.json")
```

---

## 🚀 End-of-Day Deliverable
✅ A running FastAPI web API with `/products` endpoint.  
✅ Managed using **Git version control**.  
✅ Demonstrates Python OOP, API handling, and JSON integration.

---

## 🌟 Next Steps (Day 2 Preview)
On Day 2, you’ll move to **API Development and Cloud Storage Integration**, connecting Python to **Google Cloud Storage** and building your first GenAI data pipeline.
