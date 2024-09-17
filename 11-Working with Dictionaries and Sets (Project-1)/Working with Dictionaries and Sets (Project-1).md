# Python Working with Dictionaries and Sets (Project-1)

## 1.Dictionaries
A dictionary in Python is a data structure that allows you to store and retrieve values using keys. It is also known as
a hashmap or associative array in other programming languages. Dictionaries are implemented as hash tables, providing 
fast access to values based on their keys.

### 1.Creating a Dictionary:
```
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
```

### 2.Accessing Values:
```
print(my_dict['name'])  # Output: John
```

### 3.Modifying and Adding Elements:
```
my_dict['age'] = 26  # Modifying a value
my_dict['occupation'] = 'Engineer'  # Adding a new key-value pair
```

### 4.Removing Elements:
```
del my_dict['city']  # Removing a key-value pair
```

### 5.Checking Key Existence:
```
if 'age' in my_dict:
    print('Age is present in the dictionary')
```

### 6.Iterating Through Keys and Values:
```
for key, value in my_dict.items():
    print(key, value)
```

## 2.Sets and Set Operations
A set in Python is an unordered collection of unique elements. It is useful for mathematical operations like union, 
intersection, and difference.

### 1.Creating a Set:
```
my_set = {1, 2, 3, 4, 5}
```

### 2.Adding and Removing Elements:
```
my_set.add(6)  # Adding an element
my_set.remove(3)  # Removing an element
```

### 3.Set Operations:
```
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)  # Union of sets
intersection_set = set1.intersection(set2)  # Intersection of sets
difference_set = set1.difference(set2)  # Difference of sets
```

### 4.Subset and Superset:
```
is_subset = set1.issubset(set2)  # Checking if set1 is a subset of set2
is_superset = set1.issuperset(set2)  # Checking if set1 is a superset of set2
```

### 5.Practice Exercises and Examples

#### 1.Example: Managing a Dictionary of Server Configurations and Optimizing Retrieval

**Scenario:**
- Suppose you are managing server configurations using a dictionary.

```
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}
```

**Function for Retrieval:**

```
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')
```

**Example Usage:**

```
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")
```

## 3.Lists vs. Sets

### 1.Lists
- **Ordered Collection:**
  - Lists are ordered collections of elements. The order in which elements are added is preserved.
  - Elements can be accessed by their index.

 ```
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
 ```

- **Mutable:**
  - Lists are mutable, meaning you can modify their elements after creation.

```
my_list[1] = 10
```

- **Allows Duplicate Elements:**
  - Lists can contain duplicate elements.

```
my_list = [1, 2, 2, 3, 4]
```

- **Use Cases:**
  - Use lists when you need an ordered collection with the ability to modify elements.

### 2.Sets

- **Unordered Collection:**
  - Sets are unordered collections of unique elements. The order in which elements are added is not preserved.
  - Elements cannot be accessed by their index.

```
my_set = {1, 2, 3, 4, 5}
```

- **Mutable:**
  - Sets are mutable, meaning you can add and remove elements after creation.

```
my_set.add(6)
```

- **No Duplicate Elements:**
  - Sets do not allow duplicate elements. If you try to add a duplicate, it won't raise an error, but the set won't change.

```
my_set = {1, 2, 2, 3, 4}  # Results in {1, 2, 3, 4}
```

- **Use Cases:**
  - Use sets when you need an unordered collection of unique elements, and you want to perform set operations like union, intersection, and difference.

### 3.Common Operations:

- **Adding Elements:**
  - Lists use `append()` or `insert()` methods.
  - Sets use `add()` method.

- **Removing Elements:**
  - Lists use `remove()`, `pop()`, or `del` statement.
  - Sets use `remove()` or `discard()` methods.

- **Checking Membership:**
  - Lists use the `in` operator.
  - Sets use the `in` operator as well, which is more efficient for sets.

```
# Lists
if 3 in my_list:
    print("3 is in the list")

# Sets
if 3 in my_set:
    print("3 is in the set")
```

### 4.Choosing Between Lists and Sets
- **Use Lists When:**
  - You need to maintain the order of elements.
  - Duplicate elements are allowed.
  - You need to access elements by index.

- **Use Sets When:**
  - Order doesn't matter.
  - You want to ensure unique elements.
  - You need to perform set operations like union, intersection, or difference.

## 4.Practice exercises and examples:
- Example 1: Program to Retrieve Active Pull Request Creators from Kubernetes GitHub Repository
```
# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.

import requests

# URL to fetch pull requests from the GitHub API
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Make a GET request to fetch pull requests data from the GitHub API
response = requests.get(url)  # Add headers=headers inside get() for authentication

# Only if the response is successful
if response.status_code == 200:
    # Convert the JSON response to a dictionary
    pull_requests = response.json()

    # Create an empty dictionary to store PR creators and their counts
    pr_creators = {}

    # Iterate through each pull request and extract the creator's name
    for pull in pull_requests:
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    # Display the dictionary of PR creators and their counts
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
```

- Example 2: Managing a Dictionary of Server Configurations and Optimizing Retrieval

### 1.Scenario:
Suppose you are managing server configurations using a dictionary.

```
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}
```

### 2.Function for Retrieval:
```
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')
```

### 3.Example Usage:
```
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")
```
In this example, the function `get_server_status` optimizes the retrieval of the server status by using the `get` method
and providing a default value if the server name is not found.

```
# Server configurations dictionary
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Retrieving information
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

# Example usage
server_name = 'server2'
status = get_server_status(server_name)
print(f"{server_name} status: {status}")
```
