# Python Github-JIRA integration Project - (Project-4) - (Part-2)

## 1.Introduction to Flask
Flask is a lightweight, flexible Python web framework used for building web applications and APIs. It follows a minimalistic
approach, providing only essential components, allowing developers to add features as needed. Flask is easy to set up and 
ideal for small to medium-sized projects that prioritize simplicity and flexibility.

## 2.Write your first API in python.
This code sets up a basic Flask web application with a single route (/). When accessed, the route returns the message
"Hello, World!". The app listens on all available network interfaces (0.0.0.0) and runs when executed directly, serving
content on the default port (5000).

- Code: flask-app.py
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run("0.0.0.0")
```
- Output:
```
$ python3 flask-app.py
 * Serving Flask app 'flask-app.py' (press CTRL+C to quit)
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

Hello, World!
```
**Note:** This means the Flask server is running, and you can access the app at http://0.0.0.0:5000/ from any device on 
the local network. If you are running this on your local machine, you can access it at http://localhost:5000/.

## 3.Handling API Calls

### Step 1: Build the API using Flask
In Flask, you can define routes for different API endpoints.

- Example of a simple API:
```
from flask import Flask, jsonify, request

app = Flask(__name__)

# Example GET route
@app.route('/api/get_data', methods=['GET'])
def get_data():
    data = {"message": "Hello, this is a GET request"}
    return jsonify(data)

# Example POST route
@app.route('/api/post_data', methods=['POST'])
def post_data():
    json_data = request.get_json()
    response = {"message": "Received", "data": json_data}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
```
- GET request: Access the /api/get_data route using a browser or API tool like Postman.
- POST request: Send JSON data to the /api/post_data route using Postman or curl.

### Step 2: Test API Locally
You can test your Flask API on your local machine before deploying.
   
- Run the app using python app.py.
- Test API with:
   - Browser for GET requests: http://localhost:5000/api/get_data
   - Postman or curl for POST requests:
```
$ curl -X POST http://localhost:5000/api/post_data -H "Content-Type: application/json" -d '{"name": "Test"}'
```

## 4.Deploying Your Flask API to a Server

### Option 1: Deploy Using a Virtual Private Server (VPS)
- Step 1: Choose a VPS

**Use cloud platforms like:**
- AWS EC2
- DigitalOcean
- Linode

Create a virtual machine with Ubuntu or any other Linux distribution.

- Step 2: Set Up Environment on Server

1. **SSH into your VPS:**
```
$ ssh your_user@your_server_ip
```
2. **Install Python and pip:**
```
$ sudo apt update
$ sudo apt install python3 python3-pip
```
3. **Install Flask:**
```
$ pip3 install Flask
```
4. **Copy your Flask app to the server, either using:**
- scp (secure copy from your local machine to the server)
- Or use Git to clone the repository on your server.

- Step 3: Run Flask App with a Production Server (e.g., Gunicorn)
Flask’s built-in server isn’t suitable for production, so use Gunicorn or uWSGI.

1. **Install Gunicorn:**
```
$ pip3 install gunicorn
```
2. **Run your app:**
```
gunicorn --bind 0.0.0.0:8000 app:app
```
**Note:** This will run your Flask app on port 8000. You can configure it to use other ports or a custom domain.

- Step 4: Configure Nginx (Optional but recommended)
Use Nginx as a reverse proxy to route traffic to your Flask app.

1. **Install Nginx:**
```
$ sudo apt install nginx
```
2. **Configure Nginx to route to Gunicorn:**
- Open the Nginx config file: sudo nano /etc/nginx/sites-available/default
- Add a configuration to proxy traffic to your app running on port 8000
```
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```
3. **Restart Nginx:**
```
$ sudo systemctl restart nginx
```
**Note:** Your Flask API should now be accessible via the server’s IP or domain.

### Option 2: Deploy Using a Platform-as-a-Service (PaaS)
- Step 1: Heroku
1. **Install Heroku CLI:**
```
$ curl https://cli-assets.heroku.com/install.sh | sh
```
2. **Login and Create a Heroku App:**
```
$ heroku login
$ heroku create
```
3. **Create a Procfile for Flask: In your project folder, add a Procfile:**
```
web: gunicorn app:app
```
4. **Push your app to Heroku:**
```
$ git init
$ git add .
$ git commit -m "Initial commit"
$ heroku git:remote -a your_app_name
$ git push heroku master
```
5. **Access the App: Your app will be live on https://your_app_name.herokuapp.com.**

- Step 2: AWS Elastic Beanstalk
- Install AWS CLI and Elastic Beanstalk CLI.
- Initialize your app using
```
eb init
```
- Deploy the app
```
eb create
eb open
```
**Note:** Elastic Beanstalk automates the deployment and scaling of Flask apps on AWS.

**Summary**
- **API handling:** Use Flask to define endpoints for GET/POST requests.
- **Deployment:** For VPS deployment, set up a server with Python, run Flask with Gunicorn, and optionally use Nginx as 
a reverse proxy. For PaaS, deploy easily with Heroku or AWS Elastic Beanstalk.

## 5.Practice exercises and examples:
- Example: Write a Python API which listens on a github comment and creates a ticket in JIRA.

- Code : github-jira.py
```
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://balasenapathi.atlassian.net/rest/api/3/issue"

    API_TOKEN=""

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
                            "text": "Order entry fails when selecting supplier.",
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
        "summary": "Main order flow broken",
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
**Summary:**
This code creates a Flask API that listens for POST requests at the /createJira endpoint. When triggered, it sends a 
request to the JIRA API to create an issue in a JIRA project. The API uses the requests library to make a POST request 
to JIRA, passing a JSON payload with details about the issue. The created issue's response is returned as JSON.