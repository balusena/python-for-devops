# Intro to Data Types, Working with Strings and Numbers

## 1.Data Types
In programming, a data type is a classification or categorization that specifies which type of value a variable can hold.
Data types are essential because they determine how data is stored in memory and what operations can be performed on that
data. Python, like many programming languages, supports several built-in data types. Here are some of the common data types
in Python:

1. **Numeric Data Types:**
   - **int**: Represents integers (whole numbers). Example: `x = 5`
   - **float**: Represents floating-point numbers (numbers with decimal points). Example: `y = 3.14`
   - **complex**: Represents complex numbers. Example: `z = 2 + 3j`

2. **Sequence Types:**
   - **str**: Represents strings (sequences of characters). Example: `text = "Hello, World"`
   - **list**: Represents lists (ordered, mutable sequences). Example: `my_list = [1, 2, 3]`
   - **tuple**: Represents tuples (ordered, immutable sequences). Example: `my_tuple = (1, 2, 3)`

3. **Mapping Type:**
   - **dict**: Represents dictionaries (key-value pairs). Example: `my_dict = {'name': 'John', 'age': 30}`

4. **Set Types:**
   - **set**: Represents sets (unordered collections of unique elements). Example: `my_set = {1, 2, 3}`
   - **frozenset**: Represents immutable sets. Example: `my_frozenset = frozenset([1, 2, 3])`

5. **Boolean Type:**
   - **bool**: Represents Boolean values (`True` or `False`). Example: `is_valid = True`

6. **Binary Types:**
   - **bytes**: Represents immutable sequences of bytes. Example: `data = b'Hello'`
   - **bytearray**: Represents mutable sequences of bytes. Example: `data = bytearray(b'Hello')`

7. **None Type:**
   - **NoneType**: Represents the `None` object, which is used to indicate the absence of a value or a null value.

8. **Custom Data Types:**
   - You can also define custom data types using classes and objects.

## 2.Strings

**1. String Data Type in Python:**

- In Python, a string is a sequence of characters, enclosed within single (' '), double (" "), or triple (''' ''' or """ """) quotes.
- Strings are immutable, meaning you cannot change the characters within a string directly. Instead, you create new strings.
- You can access individual characters in a string using indexing, e.g., `my_string[0]` will give you the first character.
- Strings support various built-in methods, such as `len()`, `upper()`, `lower()`, `strip()`, `replace()`, and more, for manipulation.

**2. String Manipulation and Formatting:**

- Concatenation: You can combine strings using the `+` operator.
- Substrings: Use slicing to extract portions of a string, e.g., `my_string[2:5]` will extract characters from the 2nd to the 4th position.
- String interpolation: Python supports various ways to format strings, including f-strings (f"...{variable}..."), %-formatting ("%s %d" % ("string", 42)), and `str.format()`.
- Escape sequences: Special characters like newline (\n), tab (\t), and others are represented using escape sequences.
- String methods: Python provides many built-in methods for string manipulation, such as `split()`, `join()`, and `startswith()`.

### 1.String Concatenation

#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano string-concat.py
```
#### 2.In the editor, type the following Python code
```
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)
```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (string-concat.py).

#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 string-concat.py
Hello, World!
```
### 2.String Length

#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano string-len.py
```
#### 2.In the editor, type the following Python code
```
text = "Python is awesome"
length = len(text)
print("Length of the string:", length)
```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (string-len.py).

#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 string-len.py
Length of the string: 16
```

### 3.String Uppercase Lowercase
   
#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano string-case.py
```
#### 2.In the editor, type the following Python code
```
text = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
 ```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (string-case.py).
   
#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 string-case.py
Uppercase: PYTHON IS AWESOME
Lowercase: python is awesome
```

### 4.String Replace

#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano string-replace.py
```
#### 2.In the editor, type the following Python code
```
text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)
```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (string-replace.py).

#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 string-replace.py
Modified text: Python is great
```

### 5.String Split

#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano string-split.py
```
#### 2.In the editor, type the following Python code
```
text = "Python is awesome"
words = text.split()
print("Words:", words)
```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (string-split.py).

#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 string-split.py
Words: ['Python', 'is', 'awesome']
```

### 6.String Strip

#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano string-strip.py
```
#### 2.In the editor, type the following Python code
```
text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)
```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (string-strip.py).

#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 string-strip.py
Stripped text: Some spaces around
```

### 7.String Substring

#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano string-substring.py
```
#### 2.In the editor, type the following Python code
```
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")
```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (string-substring.py).

#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 string-substring.py
is found in the text
```
