# Python Tasks for DevOps (Part 1) - File Operations (Project-2)

## 1.Introduction to File Operations and Boto3
In DevOps, file operations are crucial for automating infrastructure management, updating configurations, and interacting
with logs. With Python, you can easily manipulate files and directories. Additionally, Boto3 is a popular AWS SDK for 
Python, allowing you to integrate with AWS services (like S3) for cloud-based file operations.

## 2.Automating File Operations
Automating file operations, such as reading, writing, or modifying configuration files, can streamline many infrastructure
tasks.

## 3.Practice exercises and examples:
- Example: Update a server resources in the server.conf file up on external notification.

- file: **server.conf**
```
# Server Configuration File

# Network Settings
PORT = 8080
MAX_CONNECTIONS=600
TIMEOUT = 30

# Security Settings
SSL_ENABLED = true
SSL_CERT = /path/to/certificate.pem

# Logging Settings
LOG_LEVEL = INFO
LOG_FILE = /var/log/server.log

# Other Settings
ENABLE_FEATURE_X = true
```
- file: update_server.py
```
def update_server_config(file_path, key, value):
    # Read the existing content of the server configuration file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Update the configuration value for the specified key
    with open(file_path, 'w') as file:
        for line in lines:
            # Check if the line starts with the specified key
            if key in line:
                # Update the line with the new value
                file.write(key + "=" + value + "\n")
            else:
                # Keep the existing line as it is
                file.write(line)

# Path to the server configuration file
server_config_file = 'server.conf'

# Key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'
new_value = '600'  # New maximum connections allowed

# Update the server configuration file
update_server_config(server_config_file, key_to_update, new_value)
```
**Summary**

The script updates the MAX_CONNECTIONS setting in server.conf to 600. It reads the file, searches for the key, and replaces
the old value with the new one. If the key is found, the line is updated; if not, the file remains unchanged.