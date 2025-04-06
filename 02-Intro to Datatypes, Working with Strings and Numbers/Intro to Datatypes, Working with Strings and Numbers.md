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

## 3.Numeric Data Type

**Numeric Data Types in Python (int, float):**

- Python supports two primary numeric data types: `int` for integers and `float` for floating-point numbers.
- Integers are whole numbers, and floats can represent both whole and fractional numbers.
- You can perform arithmetic operations on these types, including addition, subtraction, multiplication, division, and more.
- Be aware of potential issues with floating-point precision, which can lead to small inaccuracies in calculations.
- Python also provides built-in functions for mathematical operations, such as `abs()`, `round()`, and `math` module for advanced functions.

### 1.Numeric Float

#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano float.py
```
#### 2.In the editor, type the following Python code
```
# Float variables
num1 = 5.0
num2 = 2.5

# Basic Arithmetic
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

# Rounding
result5 = round(3.14159265359, 2)  # Rounds to 2 decimal places
print("Rounded:", result5)
```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (float.py).

#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 float.py
Addition: 7.5
Subtraction: 2.5
Multiplication: 12.5
Division: 2.0
Rounded: 3.14
```

### 2.Numeric Int

#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano int.py
```
#### 2.In the editor, type the following Python code
```
# Integer variables
num1 = 10
num2 = 5

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)
```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (int.py).

#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 int.py
Integer Division: 2
Modulus (Remainder): 0
Absolute Value: 7
```

## 4.Regex

**Regular Expressions for Text Processing:**

- Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
- The `re` module in Python is used for working with regular expressions.
- Common metacharacters: `.` (any character), `*` (zero or more), `+` (one or more), `?` (zero or one), `[]` (character class), `|` (OR), `^` (start of a line), `$` (end of a line), etc.
- Examples of regex usage: matching emails, phone numbers, or extracting data from text.
- `re` module functions include `re.match()`, `re.search()`, `re.findall()`, and `re.sub()` for pattern matching and replacement.

### 1.Regex Findall

#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano regex-findall.py
```
#### 2.In the editor, type the following Python code
```
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (regex-findall.py).

#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 regex-findall.py
Pattern found: brown
```

### 2.Regex Match

#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano regex-match.py
```
#### 2.In the editor, type the following Python code
```
import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (regex-match.py).

#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 regex-match.py
No match
```

### 3.Regex Replace

#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano regex-replace.py
```
#### 2.In the editor, type the following Python code
```
import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)
```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (regex-replace.py).

#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 regex-replace.py
Modified text: The quick red fox jumps over the lazy red dog
```

### 4.Regex Search

#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano regex-search.py
```
#### 2.In the editor, type the following Python code
```
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (regex-search.py).

#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 regex-search.py
Pattern found: brown
```

### 5.Regex Split

#### 1.Create a Python Script using nano editor
```
ubuntu@balasenapathi:~$ nano regex-split.py
```
#### 2.In the editor, type the following Python code
```
import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)
```
#### 3.Save and Exit
**After typing the code, save the file:**
- Press Ctrl + X to exit.
- Press Y to confirm saving changes.
- Press Enter to confirm the file name (regex-split.py).

#### 4.Run the Python Script
- To run your Python script, use the following command in the terminal:
```
ubuntu@balasenapathi:~$ python3 regex-split.py
Split result: ['apple', 'banana', 'orange', 'grape']
```