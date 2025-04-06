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