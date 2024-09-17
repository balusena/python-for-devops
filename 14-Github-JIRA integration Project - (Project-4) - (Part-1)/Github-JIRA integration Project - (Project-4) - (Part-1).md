# Python Github-JIRA integration Project - (Project-4) - (Part-1)

## 1.Introduction to RESTful APIs
REST (Representational State Transfer) is an architectural style for designing networked applications. It uses HTTP 
requests to perform CRUD (Create, Read, Update, Delete) operations on resources.

**Key Concepts:**
- **Endpoints:** URLs where API services are available.
- **Methods:** HTTP methods (GET, POST, PUT, DELETE) used to interact with resources.
- **Headers:** Metadata sent with HTTP requests, such as authentication tokens.
- **Body:** The data sent with POST or PUT requests, often in JSON format.

## 2. Making HTTP Requests Using Python
To interact with APIs, you need to make HTTP requests. The requests library in Python is a popular choice for this purpose.

- Installing the requests Library:
```
$ pip install requests
```
- Example: Making a GET Request
```
import requests

response = requests.get('https://api.github.com/repos/python/cpython')
print(response.json())  # Print JSON response
```
- Example: Making a POST Request
```
import requests

url = 'https://api.example.com/resource'
data = {'key': 'value'}
response = requests.post(url, json=data)
print(response.json())
```
## 3.Parsing JSON Responses and Error Handling
- Parsing JSON Responses:

- Most APIs return data in JSON format. Use the .json() method to parse this data.

- Example: Parsing JSON Response
```
response = requests.get('https://api.github.com/repos/python/cpython')
data = response.json()
print(data['full_name'])  # Access specific fields
```

- Error Handling:

- Handle errors by checking the response status code and handling exceptions.

- Example: Error Handling
```
try:
    response = requests.get('https://api.github.com/repos/python/cpython')
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json()
    print(data['full_name'])
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"Other error occurred: {err}")
```

## 4.Practice exercises and examples:
- Example: Write a Python API which listens on a github comment and creates a ticket in JIRA.

### 1.GitHub-JIRA Integration
- Objective: Create a Python script that listens for comments on a GitHub issue and creates a JIRA ticket based on the 
comment content.

- Steps:
- Set Up GitHub Webhook:
- Go to your GitHub repository settings.
- Navigate to "Webhooks" and click "Add webhook."
- Set the Payload URL to your server endpoint where you'll receive the webhook (e.g., https://your-server.com/github-webhook).
- Choose "application/json" as the Content type.
- Select "Let me select individual events" and choose "Issue comments."
- Click "Add webhook."
- Create the Python Server:
- Use a Python web framework like Flask to create an endpoint that listens to GitHub webhooks.

### 2.Code Snippet : Fetching Project Information
```
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://balasenapathi.atlassian.net/rest/api/3/project"

API_TOKEN=""

auth = HTTPBasicAuth("", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)
```

**Purpose:**
- This code is used to fetch project information from Jira.
- It sends a GET request to the /rest/api/3/project endpoint of the Jira API.
- It requires authentication using an API token and retrieves the names of the projects.

### Code Snippet 2: Creating an Issue
```
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://balasenapathi.atlassian.net/rest/api/3/issue"

API_TOKEN = ""

auth = HTTPBasicAuth("", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "AB"
    },
    "issuetype": {
      "id": "10006"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
```
**Purpose:**
- This code is used to create a new Jira issue.
- It sends a POST request to the /rest/api/3/issue endpoint of the Jira API.
- It requires authentication using an API token and includes a JSON payload with details about the new issue.

**Summary**

**Endpoints:** The first code snippet interacts with the /rest/api/3/issue endpoint to create issues, while the second snippet
interacts with the /rest/api/3/project endpoint to retrieve project details.

**Operations:** The first snippet is performing a POST request to create a new issue, whereas the second snippet is 
performing a GET request to fetch project details.

**However, in a broader application or script, you might use both snippets in a workflow where:**
- You first fetch project details (e.g., to get a list of available projects).
- Then create an issue in one of the projects.


  
