# 🐍 Day 1: Python Fundamentals, Core Libraries & Project Foundation

## 🎯 Key Objectives
By the end of this session, you will be able to:
1. Write clean, reusable, enterprise-level Python code using **Object-Oriented Programming (OOP)**.
2. Understand and use the most important **Python Standard Libraries** for real-world automation and enterprise development.
3. Understand how **APIs** and **JSON** are used for microservice communication.
4. Set up a **local Python + GCP-ready environment** for scalable cloud integrations.

---

## 🧩 Section 0: Python Core Libraries for Enterprise Readiness

### 1️⃣ `os` – Operating System Interface
Used for interacting with the system: directories, files, environment variables.

#### Example
```python
import os

print(os.getcwd())
os.makedirs("data/logs", exist_ok=True)
os.environ["API_KEY"] = "12345"
print(os.getenv("API_KEY"))
```

💡 *Use case:* Manage environment configs or directories dynamically.

---

### 2️⃣ `sys` – Python Runtime Environment
Allows inspecting and controlling the runtime environment.

#### Example
```python
import sys

print("Python Version:", sys.version)
print("Script Arguments:", sys.argv)
```

💡 *Use case:* Useful for CLI tools or runtime argument parsing.

---

### 3️⃣ `datetime` – Date and Time Handling
```python
from datetime import datetime, timedelta

now = datetime.now()
print("Current:", now)
print("Yesterday:", now - timedelta(days=1))
```

💡 *Use case:* Logging, scheduling, or calculating expiry times.

---

### 4️⃣ `csv` – Structured Data Handling
```python
import csv

with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Department", "Salary"])
    writer.writerow(["Nuthan", "AI", "90000"])

with open("employees.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

💡 *Use case:* Manage datasets before sending them to cloud databases.

---

### 5️⃣ `json` – Data Serialization
You’ve already seen this above — the universal data format for APIs and configs.

---

### 6️⃣ `logging` – Production Logging
```python
import logging

logging.basicConfig(filename="app.log", level=logging.INFO)

logging.info("Application started")
logging.warning("Low disk space warning")
logging.error("An error occurred")
```

💡 *Use case:* Store debug or audit trails.

---

### 7️⃣ `random` – Randomization Utilities
```python
import random

numbers = [10, 20, 30, 40, 50]
print(random.choice(numbers))
print(random.sample(numbers, 3))
print(random.randint(1, 100))
```

💡 *Use case:* Test data generation.

---

### 8️⃣ `math` & `statistics`
```python
import math, statistics

values = [10, 20, 30, 40, 50]
print("Mean:", statistics.mean(values))
print("Std Dev:", statistics.stdev(values))
print("Square Root of 49:", math.sqrt(49))
```

💡 *Use case:* Analytics and ML preprocessing.

---

### 9️⃣ `pathlib` – Modern Path Handling
```python
from pathlib import Path

data_folder = Path("data")
data_folder.mkdir(exist_ok=True)
file_path = data_folder / "info.txt"

file_path.write_text("Python Day 1 Training Complete")
print(file_path.read_text())
```

💡 *Use case:* Safe cross-platform file management.

---

### 🔟 `subprocess` – Execute System Commands
```python
import subprocess

result = subprocess.run(["echo", "Hello GCP!"], capture_output=True, text=True)
print(result.stdout)
```

💡 *Use case:* Automate GCP CLI or shell commands.

---

### 🧠 Practice Task – Core Library Integration

**Goal:** Create `system_report.py` that:
- Uses `os`, `sys`, and `datetime`.
- Logs the report using `logging`.
- Saves outputs to `report.log`.

#### Example Output
```
System Report Generated at 2025-11-07 12:00:00
Python Version: 3.11.7
Working Directory: C:\Users\Nuthan\Projects
Report saved successfully!
```

---

## 🧠 Section 1: Theory — Core OOP & APIs

### 1️⃣ Python Architecture for Enterprise
Organize your Python apps modularly for scalability.

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
| **Encapsulation** | Hide internal details | Private variables |
| **Inheritance** | Reuse logic | Child classes |
| **Polymorphism** | Same interface, different behavior | Overridden methods |

#### Example 1: Encapsulation
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

#### Example 2: Inheritance & Polymorphism
```python
class Employee:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Employee"

class Manager(Employee):
    def get_role(self):
        return "Manager"
```

---

### 3️⃣ JSON and APIs
```python
import json

data = {"name": "Nuthan", "skills": ["Python", "GCP", "GenAI"]}
json_str = json.dumps(data)
parsed = json.loads(json_str)
print(parsed["skills"][0])
```

---

### 4️⃣ Virtual Environments
```bash
python -m venv myenv
myenv\Scripts\activate
pip install flask google-cloud-storage requests
```

---

### 5️⃣ requests Library
```python
import requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true")
data = response.json()
print("Temperature:", data["current_weather"]["temperature"], "°C")
```

---

## 🧩 Section 2: Real-World Examples

### 🏢 Order Processing Module
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
```

### 🌦️ Weather Alert API
```python
import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()
    temp = data["current_condition"][0]["temp_C"]
    return f"The temperature in {city} is {temp}°C"
```

---

## 🧪 Section 3: Hands-on Labs

### Lab 1.1: Setup
```bash
pip install google-cloud-storage fastapi uvicorn
gcloud init
```

### Lab 1.2: OOP Project
```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
```

### Lab 1.3: API Mockup
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

---

## 🧩 Mini Quiz
1. Why use a virtual environment? → To isolate dependencies.
2. Three OOP pillars? → Encapsulation, Inheritance, Polymorphism.
3. POST method use? → To create resources.

---

## 💻 Coding Tasks

| Level | Task | Description |
|--------|------|--------------|
| 🟢 Easy | CSV → JSON | Convert CSV file to JSON |
| 🟡 Medium | Error Handling | Add try/except to FastAPI |
| 🔴 Advanced | Consume Public API | Use `requests` + OOP modeling |

---

## 🚀 End-of-Day Deliverable
✅ Fully functional FastAPI with `/products` endpoint  
✅ Version-controlled project in Git  
✅ Demonstrates OOP, APIs, and JSON integrations  
✅ Bonus: Logging, CSV, Pathlib, and OS module usage

---

## 🌟 Next Steps (Day 2 Preview)
- Cloud API Development with GCP Storage SDK  
- Python + GCS Data Pipeline  
- Intermediate project: AI-ready API connector
