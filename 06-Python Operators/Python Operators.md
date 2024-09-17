# Python Operators

## 1.Introduction to Operators in Python
Operators in Python are special symbols or keywords that are used to perform operations on variables and values. Python 
supports a wide range of operators, categorized into several types. These operators allow you to perform tasks such as arithmetic calculations, assign values to variables, compare values, perform logical operations, and more.

**Here are the main types of operators in Python**

1. **Arithmetic Operators:** These operators are used for performing basic mathematical operations such as addition, 
subtraction, multiplication, division, and more.

2. **Assignment Operators:** Assignment operators are used to assign values to variables. They include the equal sign
(=) and various compound assignment operators.

3. **Relational Operators:** Relational operators are used to compare values and determine the relationship between them.
They return a Boolean result (True or False).

4. **Logical Operators:** Logical operators are used to combine and manipulate Boolean values. They include "and," "or,"
and "not."

5. **Identity Operators:** Identity operators are used to check if two variables point to the same object in memory. The
identity operators in Python are "is" and "is not."

6. **Membership Operators:** Membership operators are used to check if a value is present in a sequence or collection, 
such as a list, tuple, or string. The membership operators in Python are "in" and "not in."

7. **Bitwise Operators:** Bitwise operators are used to perform operations on individual bits of binary numbers. They 
include bitwise AND, OR, XOR, and more.

8. **Precedence of Operations:** Operators in Python have different levels of precedence, which determine the order in 
which operations are performed in an expression.

## 2.Arithmetic Operations in Python
Arithmetic operators in Python allow you to perform basic mathematical calculations on numeric values. These operators 
include addition, subtraction, multiplication, division, and more.

### 1.List of Arithmetic Operators
1. **Addition (+):** Adds two numbers.
2. **Subtraction (-):** Subtracts the right operand from the left operand.
3. **Multiplication (*):** Multiplies two numbers.
4. **Division (/):** Divides the left operand by the right operand (results in a floating-point number).
5. **Floor Division (//):** Divides the left operand by the right operand and rounds down to the nearest whole number.
6. **Modulus (%):** Returns the remainder of the division of the left operand by the right operand.
7. **Exponentiation (**):** Raises the left operand to the power of the right operand.

### 2.Examples

#### 1.Addition
```
a = 5
b = 3
result = a + b
print(result)  # Output: 8
```
#### 2.Subtraction
```
x = 10
y = 7
result = x - y
print(result)  # Output: 3
```

## 3.Assignment Operations in Python
Assignment operators in Python are used to assign values to variables. They include the basic assignment operator (=) and
various compound assignment operators that perform an operation on the variable while assigning a value.

### 1.List of Assignment Operators
1. **Basic Assignment (=):** Assigns a value to a variable.

2. **Addition Assignment (+=):** Adds the right operand to the left operand and assigns the result to the left operand.

3. **Subtraction Assignment (-=):** Subtracts the right operand from the left operand and assigns the result to the left operand.

4. **Multiplication Assignment (*=):** Multiplies the left operand by the right operand and assigns the result to the left operand.

5. **Division Assignment (/=):** Divides the left operand by the right operand and assigns the result to the left operand.

6. **Floor Division Assignment (//=):** Performs floor division on the left operand and assigns the result to the left operand.

7. **Modulus Assignment (%=):** Calculates the modulus of the left operand and assigns the result to the left operand.

8. **Exponentiation Assignment (**=):** Raises the left operand to the power of the right operand and assigns the result to
the left operand.

### 2.Examples

#### 1.Basic Assignment
```
x = 5
```
#### 2.Addition Assignment
```
y = 10
y += 3  # Equivalent to y = y + 3
```

## 4.Bitwise Operations in Python
Bitwise operators in Python are used to perform operations on individual bits of binary numbers. These operators include
bitwise AND, OR, XOR, and more.

### 1.List of Bitwise Operators
1. **Bitwise AND (&):** Performs a bitwise AND operation on the binary representations of the operands.
2. **Bitwise OR (|):** Performs a bitwise OR operation.
3. **Bitwise XOR (^):** Performs a bitwise XOR operation.
4. **Bitwise NOT (~):** Flips the bits of the operand, changing 0 to 1 and 1 to 0.
5. **Left Shift (<<):** Shifts the bits to the left by a specified number of positions.
6. **Right Shift (>>):** Shifts the bits to the right.

### 2.Examples

#### 1.Bitwise AND
```
a = 5  # Binary: 0101
b = 3  # Binary: 0011
result = a & b  # Result: 0001 (Decimal: 1)
```
#### 2.Bitwise OR
```
x = 10  # Binary: 1010
y = 7   # Binary: 0111
result = x | y  # Result: 1111 (Decimal: 15)
```

## 5.Identity Operations in Python
Identity operators in Python are used to compare the memory locations of two objects to determine if they are the same 
object or not. The two identity operators are "is" and "is not."

### 1.List of Identity Operators
1. **is:** Returns `True` if both operands refer to the same object.
2. **is not:** Returns `True` if both operands refer to different objects.

### 2.Examples

#### 1.is Operator
```
x = [1, 2, 3]
y = x  # y now refers to the same object as x
result = x is y
# result will be True
```
#### 2.is not Operator
```
a = "hello"
b = "world"
result = a is not b
# result will be True
```

## 6.Logical Operations in Python
Logical operators in Python are used to manipulate and combine Boolean values. These operators allow you to perform 
logical operations such as AND, OR, and NOT.

### 1.List of Logical Operators
1. **AND (and):** Returns `True` if both operands are `True`.
2. **OR (or):** Returns `True` if at least one of the operands is `True`.
3. **NOT (not):** Returns the opposite Boolean value of the operand.

### 1.Examples

#### 1.AND Operator
```
x = True
y = False
result = x and y
# result will be False
```
#### 2.OR Operator
```
a = True
b = False
result = a or b
# result will be True
```
#### 3.NOT Operator
```
x = True
result = not x
# result will be False
```

## 7.Membership Operations in Python
Membership operators in Python are used to check whether a value is present in a sequence or collection, such as a list,
tuple, or string. The membership operators are "in" and "not in."

### 1.List of Membership Operators
1. **in:** Returns `True` if the left operand is found in the sequence on the right.
2. **not in:** Returns `True` if the left operand is not found in the sequence on the right.

### 2.Examples

#### 1.in Operator
```
fruits = ["apple", "banana", "cherry"]
result = "banana" in fruits
# result will be True
```
#### 2.not in Operator
```
colors = ["red", "green", "blue"]
result = "yellow" not in colors
# result will be True
```

## 8.Precedence of Operations in Python
Precedence of operations in Python defines the order in which different types of operators are evaluated in an expression.
Operators with higher precedence are evaluated first.

### 1.Examples

#### 1.Arithmetic Precedence
```
result = 5 + 3 * 2
# Multiplication has higher precedence, so result is 11, not 16
```

## 9.Relational Operations in Python
Relational operators in Python are used to compare two values and determine the relationship between them. These operators
return a Boolean result, which is either `True` or `False`.

### 1.List of Relational Operators
1. **Equal to (==):** Checks if two values are equal.

2. **Not equal to (!=):** Checks if two values are not equal.

3. **Greater than (>):** Checks if the left operand is greater than the right operand.

4. **Less than (<):** Checks if the left operand is less than the right operand.

5. **Greater than or equal to (>=):** Checks if the left operand is greater than or equal to the right operand.

6. **Less than or equal to (<=):** Checks if the left operand is less than or equal to the right operand.

### 2.Examples

#### 1.Equal to
```
a = 5
b = 5
result = a == b
# result will be True
```
#### 2.Not equal to
```
x = 10
y = 7
result = x != y
# result will be True
```
#### 3.Greater than
```
x = 15
y = 10
result = x > y
# result will be True
```
#### 4.Less than
```
x = 8
y = 12
result = x < y
# result will be True
```
#### 5.Greater than or equal to
```
x = 7
y = 7
result = x >= y
# result will be True
```
#### 6.Less than or equal to
```
x = 9
y = 14
result = x <= y
# result will be True
```

# Python Operators Assignment

In this assignment, you will explore various Python operators and their usage. Please complete the following tasks.

## Task 1: Arithmetic Operators

1. Create two variables `a` and `b` with numeric values.
2. Calculate the sum, difference, product, and quotient of `a` and `b`.
3. Print the results.

- Code:
```
a = 10
b = 5

sum_result = a + b
difference_result = a - b
product_result = a * b
quotient_result = a / b

print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
```
- Output:
```
Sum: 15
Difference: 5
Product: 50
Quotient: 2.0
```
## Task 2: Comparison Operators

1. Compare the values of `a` and `b` using the following comparison operators: `<`, `>`, `<=`, `>=`, `==`, and `!=`.
2. Print the results of each comparison.

- Code:
```
a = 10
b = 5

less_than = a < b
greater_than = a > b
less_than_or_equal = a <= b
greater_than_or_equal = a >= b
equal = a == b
not_equal = a != b

print("a < b:", less_than)
print("a > b:", greater_than)
print("a <= b:", less_than_or_equal)
print("a >= b:", greater_than_or_equal)
print("a == b:", equal)
print("a != b:", not_equal)
```
- Output:
```
a < b: False
a > b: True
a <= b: False
a >= b: True
a == b: False
a != b: True
```

## Task 3: Logical Operators

1. Create two boolean variables, `x` and `y`.
2. Use logical operators (`and`, `or`, `not`) to perform various logical operations on `x` and `y`.
3. Print the results.

- Code:
```
x = True
y = False

and_result = x and y
or_result = x or y
not_result_x = not x
not_result_y = not y

print("x and y:", and_result)
print("x or y:", or_result)
print("not x:", not_result_x)
print("not y:", not_result_y)
```
- Output:
```
x and y: False
x or y: True
not x: False
not y: True
```

## Task 4: Assignment Operators

1. Create a variable `total` and initialize it to 10.
2. Use assignment operators (`+=`, `-=`, `*=`, `/=`) to update the value of `total`.
3. Print the final value of `total`.

- Code:
```
total = 10

total += 5
total -= 3
total *= 2
total /= 4

print("Final total:", total)
```
- Output:
```
Final total: 6.0
```
## Task 5: Bitwise Operators
1. If you are comfortable with bitwise operators, perform some bitwise operations on integer values and print the results.
If not, you can skip this task.

- Code:
```
# Define two integers
a = 6  # 110 in binary
b = 3  # 011 in binary

# Performing all bitwise operations

# Bitwise AND
result_and = a & b
# Bitwise OR
result_or = a | b
# Bitwise XOR
result_xor = a ^ b
# Bitwise NOT
result_not_a = ~a
result_not_b = ~b
# Left Shift
result_left_shift_a = a << 2
result_left_shift_b = b << 2
# Right Shift
result_right_shift_a = a >> 2
result_right_shift_b = b >> 1

# Print all results
print(f"Bitwise AND of {a} & {b}: {result_and}")       
print(f"Bitwise OR of {a} | {b}: {result_or}")        
print(f"Bitwise XOR of {a} ^ {b}: {result_xor}")       
print(f"Bitwise NOT of {a}: {result_not_a}")           
print(f"Bitwise NOT of {b}: {result_not_b}")          
print(f"{a} << 2 (Left Shift): {result_left_shift_a}") 
print(f"{b} << 2 (Left Shift): {result_left_shift_b}") 
print(f"{a} >> 2 (Right Shift): {result_right_shift_a}") 
print(f"{b} >> 1 (Right Shift): {result_right_shift_b}") 
```
- Output:
```
Bitwise AND of 6 & 3: 2
Bitwise OR of 6 | 3: 7
Bitwise XOR of 6 ^ 3: 5
Bitwise NOT of 6: -7
Bitwise NOT of 3: -4
6 << 2 (Left Shift): 24
3 << 2 (Left Shift): 12
6 >> 2 (Right Shift): 1
3 >> 1 (Right Shift): 1
```
## Task 6: Identity and Membership Operators

1. Create a list `my_list` containing a few elements.
2. Use identity operators (`is` and `is not`) to check if two variables are the same object.
3. Use membership operators (`in` and `not in`) to check if an element is present in `my_list`.
4. Print the results.

- Code:
```
my_list = [1, 2, 3, 4, 5]

# Identity operators
a = my_list
b = [1, 2, 3, 4, 5]

is_same_object = a is my_list
is_not_same_object = b is not my_list

# Membership operators
element_in_list = 3 in my_list
element_not_in_list = 6 not in my_list

print("a is my_list:", is_same_object)
print("b is not my_list:", is_not_same_object)
print("3 in my_list:", element_in_list)
print("6 not in my_list:", element_not_in_list)
```
- Output:
```
a is my_list: True
b is not my_list: True
3 in my_list: True
6 not in my_list: True
```


