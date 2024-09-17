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



