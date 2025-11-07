# Demonstration of Python Core Libraries
import os
os.makedirs("data/logs", exist_ok=True)
os.environ["API_KEY"] = "12345"
print(os.getcwd())
print(os.getenv("API_KEY"))

with open("C:\\GCP\\GenAILearnings\\Google Agent Space Boot Camp(6 days)\\Day-1 Python Fundamentals\\data\\logs\\app.log", "w") as log_file:
    log_file.write("Application started\n")
print("Log file created at:", os.path.abspath("C:\\GCP\\GenAILearnings\\Google Agent Space Boot Camp(6 days)\\Day-1 Python Fundamentals\\data\\logs\\app.log"))
print("Directory 'data/logs' created and log file initialized.")
print("Environment variable 'API_KEY' set.")
# This code creates a directory structure, sets an environment variable,
# and writes a log file, demonstrating the use of the os module in Python.

import sys

print("Python Version:", sys.version)
print("\n Script Arguments:", sys.argv)
print("\n Module Search Path:", sys.path)
print("Platform Information:", sys.platform)

# This code retrieves and prints information about the Python environment
# using the sys module, including version, script arguments, module search path, and platform details.
import math
print("Value of Pi:", math.pi)
print("Square root of 16:", math.sqrt(16))
print("Cosine of 0 degrees:", math.cos(0))
print("Factorial of 5:", math.factorial(5))
print("Power of 5 raised to 10:", 5**10)

# This code demonstrates the use of the math module in Python
# by performing various mathematical operations and printing the results.
import datetime
now = datetime.datetime.now()
print("Current Date and Time:", now)
print("Formatted Date:", now.strftime("%Y-%m-%d"))
print("Indian Formatted Date:", now.strftime("%d-%m-%Y"))
print("Formatted Time:", now.strftime("%H:%M:%S"))
# This code uses the datetime module to get the current date and time,
# and formats it in different ways for display.

import random
random_number = random.randint(1, 100)
print("Random Number between 1 and 100:", random_number)
#random opt from 4 digit OTP
random_4_digit = random.randint(0000, 9999)
print("Random 4-Digit OTP:", random_4_digit)

#random choice from a list
random_choice = random.choice(['apple', 'banana', 'cherry'])
print("Random Choice from list:", random_choice)
# This code demonstrates the use of the random module in Python
# by generating a random integer and selecting a random item from a list.
import json
data = {"name": "John Doe","age": 30,"city": "New York"}
json_string = json.dumps(data)
print("JSON String:", json_string)
parsed_data = json.loads(json_string)
print("Parsed Data:", parsed_data)
# This code showcases the use of the json module in Python
# by converting a Python dictionary to a JSON string and then parsing it back to a dictionary.

import re
pattern = r'\b\d{3}-\d{2}-\d{4}\b'
pattern1= r'\b\d{3}=\d{3}-\d{4}\b' #mobile number pattern
mobile_number = "My mobile number is 984=123-0443."
match1 = re.search(pattern1, mobile_number)
if match1:
    print("Found Mobile Number:", match1.group())
else:
    print("No Mobile Number found.")
    
text = "My SSN is 123-45-6789."
match = re.search(pattern, text)
if match:
    print("Found SSN:", match.group())
else:
    print("No SSN found.")
# This code demonstrates the use of the re module in Python
# by searching for a pattern (SSN format) in a given text string.

import time
start_time = time.time()
time.sleep(2)  # Simulate a delay
end_time = time.time()
print("Elapsed Time:", end_time - start_time, "seconds")
# This code uses the time module to measure the elapsed time
# for a simulated delay using sleep function.
import shutil
source = "data/logs/app.log"
destination = "data/logs/app_backup.log"
shutil.copy(source, destination)
print("Log file backed up to:", destination)
# This code demonstrates the use of the shutil module in Python
# by copying a log file to create a backup.

import tempfile
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b'This is a temporary file.')
    temp_file_path = temp_file.name 
print("Temporary file created at:", temp_file_path)
# This code showcases the use of the tempfile module in Python
# by creating a temporary file and writing data to it.
import urllib.request
url = "http://www.example.com"
response = urllib.request.urlopen(url)
html = response.read()
print("Fetched HTML content from example.com")
# This code demonstrates the use of the urllib module in Python
# by fetching HTML content from a specified URL.
import collections
Counter = collections.Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print("Fruit Count:", Counter)
# This code uses the collections module in Python
# to count the occurrences of items in a list using Counter.
import itertools
combinations = list(itertools.combinations(['A', 'B', 'C'], 2))
print("Combinations of 2 from ['A', 'B', 'C']:", combinations)
# This code demonstrates the use of the itertools module in Python
# by generating all possible combinations of a specified length from a list.
import hashlib
hash_object = hashlib.sha256(b'Hello, World!')
hex_dig = hash_object.hexdigest()
print("SHA-256 Hash of 'Hello, World!':", hex_dig)

#csv module
import csv

with open("C:\\GCP\\GenAILearnings\\Google Agent Space Boot Camp(6 days)\\Day-1 Python Fundamentals\\data\\employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Department", "Salary"])
    writer.writerow(["Nuthan", "AI", "90000"])

with open("C:\\GCP\\GenAILearnings\\Google Agent Space Boot Camp(6 days)\\Day-1 Python Fundamentals\\data\\employees.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#logging module
import logging

logging.basicConfig(filename="C:\\GCP\\GenAILearnings\\Google Agent Space Boot Camp(6 days)\\Day-1 Python Fundamentals\\data\\logs\\app.log", level=logging)

try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Division by zero error", exc_info=True, stack_info=True,extra={'user': 'Nuthan'})


logging.info("Application started", extra={'user': 'Nuthan'})
logging.warning("Low disk space warning", extra={'user': 'Nuthan'})
logging.error("An error occurred", extra={'user': 'Nuthan'})


#random module
import random

numbers = [10, 20, 30, 40, 50]
random.shuffle(numbers)
print("Shuffled Numbers:", numbers)
print("Random Float:", random.uniform(1.5, 10.5))
print("Random Choice:", random.choice(numbers))
print("Random Sample:", random.sample(numbers, 3))

#math and statistics module
import math, statistics

values = [10, 20, 30, 40, 50]
print("Mean:", statistics.mean(values))
print("Std Dev:", statistics.stdev(values))
print("Square Root of 49:", math.sqrt(49))

#Pathlib module
from pathlib import Path
path = Path("C:/GCP/GenAILearnings/Google Agent Space Boot Camp(6 days)/Day-1 Python Fundamentals/data/logs")
print("Path Exists:", path.exists())
print("Is Directory:", path.is_dir())
print("Files in Directory:", list(path.iterdir()))
print("Parent Directory:", path.parent)
print("File Name:", path.name)
print("File Suffix:", path.suffix)
print("Absolute Path:", path.resolve())

# Example of creating a file.txt file using pathlib
file_path = path / "example.txt"
file_path.write_text("This is an example file created using pathlib.")
print("File created at:", file_path)

print("Pathlib module demonstration completed.")

#Assignment - 1
# ---------------------
'''
Goal: Create below that:

Uses os, sys, and datetime.
Logs the report using logging.
Saves outputs to report.log.

Example Output
System Report Generated at 2025-11-07 12:00:00
Python Version: 3.11.7
Working Directory: C:\Users\Nuthan\Projects
Report saved successfully!
'''
import os,sys,datetime,logging

logging.basicConfig(filename="C:\\GCP\\GenAILearnings\\Google Agent Space Boot Camp(6 days)\\Day-1 Python Fundamentals\\data\\logs\\report.log", level=logging.INFO)
now = datetime.datetime.now()
working_dir = os.getcwd()
python_version = sys.version
report = f"""System Report Generated at {now}
Python Version: {python_version}
Working Directory: {working_dir}
"""

logging.info(f"System report generated successfully for: {report}")