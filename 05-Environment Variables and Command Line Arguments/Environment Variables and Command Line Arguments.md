# Python Environment Variables and Command Line Arguments

## 1.Reading and Writing Environment Variables in Python
Environment variables are dynamic values in the operating system that can affect the behavior of running processes. They
are often used for configuration purposes, such as API keys, database credentials, or environment-specific settings.

Reading Environment Variables
Python provides a way to access environment variables using the os module.
```
import os

# Set an environment variable
os.environ['NEW_VAR'] = 'my_value'
print(f"New Variable: {os.environ['NEW_VAR']}")
```
**Note:** Setting environment variables using os.environ will only affect the current process and its children, but not 
the global system environment.

## 2.Using the os and dotenv Modules

### 1.Using os Module
The os module is the standard way to work with environment variables in Python, as shown above. You can read, write, and
modify environment variables using os.

### 2.Using dotenv Module
The dotenv module allows you to store environment variables in a .env file, which is useful for securing sensitive information
like API keys, database credentials, etc.

- Installing python-dotenv
```
pip install python-dotenv
```
- .env File Example
```
DB_USER=my_database_user
DB_PASSWORD=my_secure_password
```
- Loading Environment Variables from .env File
```
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

print(f"Database User: {db_user}")
print(f"Database Password: {db_password}")
```
## 3.Securing Sensitive Information in Environment Variables
To secure sensitive data such as API keys, database passwords, or tokens, follow these practices.

**Use Environment Variables:** Store sensitive information in environment variables instead of hardcoding it into your scripts.
**Use .env Files:** For development, use a .env file (and make sure to add it to .gitignore so it's not checked into version control).
**Access Control:** Limit who can view or modify environment variables on your systems.
**Environment-Specific Settings:** Use different environment variables for development, testing, and production environments.

- Example .gitignore entry
```
# Ignore .env files to protect sensitive data
.env
```

## 4.Handling Command Line Arguments in Python
Python provides a module called argparse to handle command-line arguments.

- Basic Usage of argparse
```
import argparse

# Initialize the parser
parser = argparse.ArgumentParser(description="A script to demonstrate command line arguments")

# Add arguments
parser.add_argument('--name', type=str, help='Your name')
parser.add_argument('--age', type=int, help='Your age')

# Parse the arguments
args = parser.parse_args()

# Access arguments
print(f"Hello, {args.name}. You are {args.age} years old.")
```
- Running the Script
```
python3 script.py --name John --age 30
Hello, John. You are 30 years old.
```
**Common Argument Types**
- --flag or -f: Options with values (e.g., --name John)
- store_true:Boolean flag (e.g., --verbose)

## 5.Practice Exercises and Examples

### Exercise 1: Environment Variables
Create a Python script that reads a database connection string from environment variables and prints the information.
```
import os

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

if db_host and db_user and db_password:
    print(f"Connecting to DB at {db_host} with user {db_user}.")
else:
    print("Database credentials are missing!")
```

### Exercise 2: Command-Line Arguments for DevOps Automation
Develop a Python script that accepts command-line arguments to customize DevOps automation tasks, such as deploying to 
different environments (dev, test, prod).
```
import argparse

# Initialize the parser
parser = argparse.ArgumentParser(description="Deploy a service to different environments")

# Add arguments
parser.add_argument('--env', type=str, required=True, choices=['dev', 'test', 'prod'], help='The environment to deploy to')
parser.add_argument('--service', type=str, required=True, help='The service name')

# Parse the arguments
args = parser.parse_args()

# Perform deployment based on environment
if args.env == 'dev':
    print(f"Deploying {args.service} to Development environment")
elif args.env == 'test':
    print(f"Deploying {args.service} to Testing environment")
elif args.env == 'prod':
    print(f"Deploying {args.service} to Production environment")
```
- Running the Script
```
python3 deploy.py --env dev --service web_app
Deploying web_app to Development environment
```
