# Python Working with Lists (Part 2)

## 1. List Comprehensions
List comprehensions provide a concise way to create lists. It allows for creating a new list by performing some operation
on each item in an existing list or iterating through a sequence.

- Example
```
# Using list comprehension to create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)
```
- Output
```
[1, 4, 9, 16, 25]
```

## 2. Nested Lists and Advanced List Operations
Nested lists are lists within lists, allowing for multi-dimensional data structures (e.g., matrices or grids).

- Example
```
# Example of a nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing an element in a nested list
print(matrix[1][2])  # Output: 6

# Using list comprehension to flatten a nested list
flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)
```
- Output
```
6
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 3. Practice Example: Print List of Files in the List of Folders Provided
This example demonstrates how to iterate over a list of folders, get the list of files in each folder, and print them 
using Python.

```
import os

# List of folder paths (you can add your folder paths here)
folders = [
    '/path/to/folder1',
    '/path/to/folder2',
    '/path/to/folder3'
]

# Get list of files in each folder and print them
for folder in folders:
    if os.path.exists(folder):
        print(f"Files in {folder}:")
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        for file in files:
            print(f"- {file}")
    else:
        print(f"Folder {folder} does not exist.")
```
- Output
```
Files in /path/to/folder1:
- file1.txt
- file2.docx

Files in /path/to/folder2:
- image1.png
- script.py

Folder /path/to/folder3 does not exist.
```
- Example
```
import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()
```
- Output
```
Enter a list of folder paths separated by spaces: /home/user/documents /home/user/restricted /home/user/nonexistent
Files in /home/user/documents:
- report.pdf
- meeting_notes.txt
- project_plan.docx

Error in /home/user/restricted: Permission denied

Error in /home/user/nonexistent: Folder not found
```