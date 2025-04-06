# Python Tasks for DevOps (Part 2) (Project-3)

## 1.Using Fabric for Remote Task Automation
Fabric is a Python library designed to simplify the automation of remote tasks via SSH. It allows you to execute commands,
upload files, and manage remote servers efficiently.

**Key Features:**
- Remote Command Execution: Run shell commands on remote servers.
- File Transfer: Upload and download files to/from remote servers.
- Task Management: Define and execute tasks using Python functions.

### Example: Deploying a Web Application

#### 1.Install Fabric
```
$ pip install fabric
```
#### 2.Create a fabfile.py
```
from fabric import task

@task
def deploy(c):
    # Define paths and service name
    app_zip = 'app.zip'
    remote_path = '/var/www/myapp'
    service_name = 'myapp.service'

    # Upload application files
    print("Uploading application files...")
    c.put(app_zip, '/tmp/app.zip')

    # Connect to remote server and deploy
    with c.cd(remote_path):
        print("Deploying application...")
        c.run('unzip -o /tmp/app.zip', pty=False)
        c.run(f'systemctl restart {service_name}', pty=False)

    # Check if the application is running
    print("Checking application status...")
    result = c.run(f'systemctl is-active {service_name}', warn=True, pty=False)
    if result.stdout.strip() == 'active':
        print("Deployment successful. Application is running.")
    else:
        print("Deployment failed. Rolling back...")
        c.run(f'systemctl stop {service_name}', pty=False)
        c.run('rm -rf /var/www/myapp/*', pty=False)
        c.run('unzip /tmp/backup.zip -d /var/www/myapp', pty=False)
        c.run(f'systemctl start {service_name}', pty=False)
        print("Rollback completed.")

@task
def backup(c):
    # Backup current application files
    remote_path = '/var/www/myapp'
    c.run(f'zip -r /tmp/backup.zip {remote_path}', pty=False)
```
#### 3.Run the Fabric Task
```
$ fab backup deploy -H username@remote_server_ip
```

## 2.AWS Automation with Boto3
Boto3 is the AWS SDK for Python that enables you to interact programmatically with AWS services. It allows for efficient
management and automation of AWS resources.

**Key Features:**
- EC2 Management: Launch, terminate, and manage EC2 instances.
- S3 Management: Create, delete, and manage S3 buckets and objects.

### Example: EC2 and S3 Automation

#### 1.Install Boto3
```
$ pip install boto3
```
#### 2.Create a Python Script (aws_automation.py)
```
import boto3

# Initialize AWS clients
ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

# Function to launch an EC2 instance
def launch_instance(ami_id, instance_type):
    print("Launching EC2 instance...")
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        KeyName='your-key-pair',  # Replace with your key pair name
        SecurityGroupIds=['sg-xxxxxxxx'],  # Replace with your security group ID
        SubnetId='subnet-xxxxxxxx'  # Replace with your subnet ID
    )
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Instance launched with ID: {instance_id}")
    return instance_id

# Function to upload a file to S3
def upload_to_s3(bucket_name, file_name):
    print(f"Uploading {file_name} to bucket {bucket_name}...")
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"File {file_name} uploaded.")

# Function to delete an EC2 instance
def delete_instance(instance_id):
    print(f"Terminating EC2 instance {instance_id}...")
    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} terminated.")

# Function to delete an S3 bucket
def delete_bucket(bucket_name):
    print(f"Deleting S3 bucket {bucket_name}...")
    s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} deleted.")

# Example usage
if __name__ == "__main__":
    # Launch EC2 instance
    instance_id = launch_instance('ami-12345678', 't2.micro')  # Replace with appropriate AMI ID and instance type

    # Upload file to S3
    upload_to_s3('my-bucket-name', 'example.txt')  # Replace with your bucket name and file

    # After some operations, delete instance and bucket
    delete_instance(instance_id)
    delete_bucket('my-bucket-name')
```
#### 3.Run the boto3 automation Task
```
$ python3 aws_automation.py
```

## 3.Managing EC2 Instances
EC2 Instances are virtual servers that you can use for various computing tasks in AWS. Effective management of these 
instances includes starting, stopping, and terminating them as well as scaling them based on demand.

**Example Operations:**
### 1.Starting an Instance
- Objective: Initiate an EC2 instance to run applications.

- Steps:
- Open the EC2 Console: Navigate to the EC2 dashboard in the AWS Management Console.
- Select an Instance: Choose the instance you want to start.
- Click "Instance State" dropdown.
- Select "Start Instance."

- Boto3 Example:
```
import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

def start_instance(instance_id):
    response = ec2.start_instances(InstanceIds=[instance_id])
    print(f"Starting instance {instance_id}.")
    return response

# Example usage
if __name__ == "__main__":
    instance_id = 'i-1234567890abcdef0'  # Replace with your instance ID
    start_instance(instance_id)
```

### 2.Stopping an Instance
- Objective: Temporarily stop an EC2 instance to save costs or perform maintenance.

- Steps:
- Open the EC2 Console: Navigate to the EC2 dashboard.
- Select an Instance: Choose the instance you want to stop.
- Stop the Instance:
- Click "Instance State" dropdown.
- Select "Stop Instance."

- Boto3 Example:
```
def stop_instance(instance_id):
    response = ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Stopping instance {instance_id}.")
    return response

# Example usage
if __name__ == "__main__":
    instance_id = 'i-1234567890abcdef0'  # Replace with your instance ID
    stop_instance(instance_id)
```

### 3.Terminating an Instance
- Objective: Permanently delete an EC2 instance.

- Steps:
- Open the EC2 Console: Go to the EC2 dashboard.
- Select an Instance: Choose the instance you want to terminate.
- Terminate the Instance:
- Click "Instance State" dropdown.
- Select "Terminate Instance."

- Boto3 Example:
```
def terminate_instance(instance_id):
    response = ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"Terminating instance {instance_id}.")
    return response

# Example usage
if __name__ == "__main__":
    instance_id = 'i-1234567890abcdef0'  # Replace with your instance ID
    terminate_instance(instance_id)
```

### 4.Scaling EC2 Instances
- Objective: Adjust the number of EC2 instances based on demand.
      
- Boto3 Example for Auto Scaling:
```
auto_scaling = boto3.client('autoscaling')

def create_auto_scaling_group():
    response = auto_scaling.create_auto_scaling_group(
        AutoScalingGroupName='my-auto-scaling-group',
        LaunchConfigurationName='my-launch-configuration',
        MinSize=1,
        MaxSize=3,
        DesiredCapacity=2,
        VPCZoneIdentifier='subnet-xxxxxxxx',  # Replace with your subnet ID
    )
    print("Auto Scaling Group created.")
    return response

if __name__ == "__main__":
    create_auto_scaling_group()
```

## 4.Managing S3 Buckets
S3 Buckets are storage containers used to store objects (files) in AWS. Managing S3 buckets involves creating, uploading
objects to, and deleting buckets.

### 1.Example Operations:
- 1. Creating a Bucket
- Objective: Set up a new S3 bucket to store files.

- Steps:
- Open the S3 Console: Navigate to the S3 dashboard.
- Create a Bucket:
- Click "Create bucket."
- Provide a unique bucket name and configure settings.
- Click "Create bucket."

- Boto3 Example:
```
import boto3

# Initialize S3 client
s3 = boto3.client('s3')

def create_bucket(bucket_name):
    response = s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} created.")
    return response

# Example usage
if __name__ == "__main__":
    bucket_name = 'my-new-bucket'  # Replace with your bucket name
    create_bucket(bucket_name)
```

### 2.Uploading Objects
- Objective: Add files to an S3 bucket.

- Steps:
- Open the S3 Console: Go to the S3 dashboard.
- Upload a File:
- Navigate to the bucket.
- Click "Upload."
- Select and upload the file.

- Boto3 Example:
```
def upload_to_s3(bucket_name, file_name):
    response = s3.upload_file(file_name, bucket_name, file_name)
    print(f"File {file_name} uploaded to bucket {bucket_name}.")
    return response

# Example usage
if __name__ == "__main__":
    bucket_name = 'my-existing-bucket'  # Replace with your bucket name
    file_name = 'example.txt'  # Replace with your file name
    upload_to_s3(bucket_name, file_name)
```

### 3. Deleting a Bucket
- Objective: Remove an S3 bucket and all its contents.

- Steps:
- Open the S3 Console: Navigate to the S3 dashboard.
- Delete a Bucket:
- Navigate to the bucket.
- Empty the bucket (if necessary).
- Click "Delete bucket."

- Boto3 Example:
```
def delete_bucket(bucket_name):
    # First delete all objects in the bucket
    bucket = s3.Bucket(bucket_name)
    bucket.objects.all().delete()
    # Then delete the bucket itself
    response = s3.delete_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} deleted.")
    return response

# Example usage
if __name__ == "__main__":
    bucket_name = 'my-existing-bucket'  # Replace with your bucket name
    delete_bucket(bucket_name)
```

## 5.Practice Exercise: Deploying a Web Application Using Boto3, Fabric, EC2, and S3
- Objective: Automate the deployment of a web application to a remote server using an EC2 instance, manage application 
files with S3, and deploy the application using Fabric.

### Setting Up AWS Resources

#### 1.1.Launch an EC2 Instance
- First, create an EC2 instance to host your web application.

- Boto3 Script to Launch EC2 Instance:
```
import boto3

def launch_instance(ami_id, instance_type, key_name, security_group_id, subnet_id):
    ec2 = boto3.client('ec2')
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1,
        KeyName=key_name,
        SecurityGroupIds=[security_group_id],
        SubnetId=subnet_id
    )
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Instance launched with ID: {instance_id}")
    return instance_id

if __name__ == "__main__":
    ami_id = 'ami-12345678'  # Replace with your AMI ID
    instance_type = 't2.micro'
    key_name = 'your-key-pair'  # Replace with your key pair name
    security_group_id = 'sg-xxxxxxxx'  # Replace with your security group ID
    subnet_id = 'subnet-xxxxxxxx'  # Replace with your subnet ID
    launch_instance(ami_id, instance_type, key_name, security_group_id, subnet_id)
```
#### 1.2.Create an S3 Bucket
- Create an S3 bucket to store the application files.

- Boto3 Script to Create S3 Bucket:
```
import boto3

def create_bucket(bucket_name):
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} created.")
    return response

if __name__ == "__main__":
    bucket_name = 'my-deploy-bucket'  # Replace with your bucket name
    create_bucket(bucket_name)
```
#### 2. Upload Application Files to S3
- Boto3 Script to Upload Files to S3:
```
import boto3

def upload_file_to_s3(bucket_name, file_name):
    s3 = boto3.client('s3')
    response = s3.upload_file(file_name, bucket_name, file_name)
    print(f"File {file_name} uploaded to bucket {bucket_name}.")
    return response

if __name__ == "__main__":
    bucket_name = 'my-deploy-bucket'  # Replace with your bucket name
    file_name = 'app.zip'  # Replace with your application file
    upload_file_to_s3(bucket_name, file_name)
```
#### 3. Deploy Application Using Fabric

#### 3.1 Create a Fabric Script

- Fabric Script (fabfile.py):
```
from fabric import task

@task
def deploy(c):
    bucket_name = 'my-deploy-bucket'  # Replace with your bucket name
    app_file = 'app.zip'
    remote_path = '/var/www/myapp'
    instance_ip = 'your_ec2_instance_ip'  # Replace with your EC2 instance IP
    service_name = 'myapp.service'

    # Connect to the remote server
    with c.cd(remote_path):
        print("Downloading application files from S3...")
        c.run(f'aws s3 cp s3://{bucket_name}/{app_file} /tmp/{app_file}', pty=False)

        print("Deploying application...")
        c.run(f'unzip -o /tmp/{app_file} -d {remote_path}', pty=False)
        c.run(f'systemctl restart {service_name}', pty=False)

    print("Deployment complete. Checking application status...")
    result = c.run(f'systemctl is-active {service_name}', warn=True, pty=False)
    if result.stdout.strip() == 'active':
        print("Application is running.")
    else:
        print("Deployment failed. Rolling back...")
        c.run(f'systemctl stop {service_name}', pty=False)
        c.run(f'rm -rf {remote_path}/*', pty=False)
        c.run(f'aws s3 cp s3://{bucket_name}/backup.zip /tmp/backup.zip', pty=False)
        c.run(f'unzip /tmp/backup.zip -d {remote_path}', pty=False)
        c.run(f'systemctl start {service_name}', pty=False)
        print("Rollback completed.")

@task
def backup(c):
    remote_path = '/var/www/myapp'
    bucket_name = 'my-deploy-bucket'  # Replace with your bucket name
    c.run(f'zip -r /tmp/backup.zip {remote_path}', pty=False)
    c.run(f'aws s3 cp /tmp/backup.zip s3://{bucket_name}/backup.zip', pty=False)
    print("Backup complete.")
```
#### 3.2 Run the Fabric Script
- Deploy the application using Fabric:
```
fab backup deploy -H username@your_ec2_instance_ip
```
**Note:** Replace username with your SSH username and your_ec2_instance_ip with the public IP address of your EC2 instance.

**Summary**

This exercise walks you through deploying a web application by combining Boto3 for AWS automation and Fabric for remote
task execution. The EC2 instance is used to host the application, while S3 is used to store and manage application files.
Adjust the scripts and configuration to fit your specific environment and requirements.