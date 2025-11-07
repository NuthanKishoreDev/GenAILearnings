# Demonstration of Python Core OOP Concepts and APIs
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def speak(self):
        return "Meow!"
def animal_sound(animal):
    print(f"{animal.name} the {animal.species} says: {animal.speak()}") 
dog = Dog(name="Buddy", breed="Golden Retriever")
cat = Cat(name="Whiskers", color="Tabby")
animal_sound(dog)
animal_sound(cat)

#create vehile class with inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def start_engine(self):
        return "Engine started"
    
class Car(Vehicle):
        def __init__(self, make, model, num_seats):
            super().__init__(make, model)
            self.num_seats = num_seats
        def start_engine(self):
            return f"A {self.make} {self.model} car with {self.num_seats} seats roars to life!"
class Motorcycle(Vehicle):
        def __init__(self, make, model, has_sidecar):
            super().__init__(make, model)
            self.has_sidecar = has_sidecar
        def start_engine(self):
            sidecar_status = "with a sidecar" if self.has_sidecar else "without a sidecar"
            return f"A {self.make} {self.model} motorcycle {sidecar_status} revs up!"

car = Car(make="Toyota", model="Camry", num_seats=5)
motorcycle = Motorcycle(make="Harley-Davidson", model="Street 750", has_sidecar=False)
print(car.start_engine())
print(motorcycle.start_engine())
# This code covers inheritance and polymorphism in Python OOPs


#Encapsulation  example BankAccount:
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # private attribute
        self.balance = balance                # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid withdrawal amount")

    def get_balance(self):
        return self.balance
account = BankAccount(account_number="123456789")
account.deposit(500)
account.withdraw(200)
print("Current Balance:", account.get_balance())
account.withdraw(1000) # Attempt to withdraw more than the balance
# This code demonstrates encapsulation in Python OOPs


#Inheritance & Polymorphism example Employee and Manager classes:
from abc  import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        return f"{self.name} is working as a {self.position}"

    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name, position="Manager")
        self.department = department

    def work(self):
        return f"{self.name} is managing the {self.department} department"
    
    def salary(self):
        return 80000

class Developer(Employee):
    def __init__(self, name, programming_language):
        super().__init__(name, position="Developer")
        self.programming_language = programming_language

    def work(self):
        return f"{self.name} is coding in {self.programming_language}"  
    
    def salary(self):
        return 70000
    
employees = [
    Manager(name="Alice", department="Sales"),
    Developer(name="Bob", programming_language="Python")
]

for emp in employees:
    print(emp.work())
    print(f"Earns: ${emp.salary()} salary")
    
# This code demonstrates inheritance and polymorphism in Python OOPs



# JSON API example using json module
import json

data = {"name": "Nuthan", "skills": ["Python", "GCP", "GenAI", "Java", "OOPs"]}

# Convert dict → JSON string
json_str = json.dumps(data)
print(type(json_str), json_str)
print(json_str)
# Convert JSON string → dict
parsed = json.loads(json_str)
print(type(parsed), parsed)
print(parsed)
# This code showcases the use of the json module in Python



