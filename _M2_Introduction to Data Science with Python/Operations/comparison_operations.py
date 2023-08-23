# Comparison Operations in Python

print("Comparison Operations in Python")

# Equal to (==)
num1_eq = 5
num2_eq = 5
result_equal_12 = num1_eq == num2_eq  # True

num3_eq = 5
num4_eq = 10
result_equal_34 = num3_eq == num4_eq  # False

# Not equal to (!=)
num1_neq = 10
num2_neq = 5
result_not_equal_12 = num1_neq != num2_neq  # True

num3_neq = 10
num4_neq = 10
result_not_equal_34 = num3_neq != num4_neq  # False

# Greater than (>)
num1_gt = 7
num2_gt = 3
result_greater_than_12 = num1_gt > num2_gt  # True

num3_gt = 7
num4_gt = 10
result_greater_than_34 = num3_gt > num4_gt  # False

# Less than (<)
num1_lt = 5
num2_lt = 10
result_less_than_12 = num1_lt < num2_lt  # True

num3_lt = 10
num4_lt = 5
result_less_than_34 = num3_lt < num4_lt  # False

# Greater than or equal to (>=)
num1_ge = 5
num2_ge = 5
result_greater_equal_12 = num1_ge >= num2_ge  # True

num3_ge = 5
num4_ge = 10
result_greater_equal_34 = num3_ge >= num4_ge  # False

# Less than or equal to (<=)
num1_le = 10
num2_le = 15
result_less_equal_12 = num1_le <= num2_le  # True

num3_le = 10
num4_le = 5
result_less_equal_34 = num3_le <= num4_le  # False

# Printing the results
print("Equal to (==):")
print(f"{num1_eq} == {num2_eq}: {result_equal_12}")
print(f"{num3_eq} == {num4_eq}: {result_equal_34}")

print("\nNot equal to (!=):")
print(f"{num1_neq} != {num2_neq}: {result_not_equal_12}")
print(f"{num3_neq} != {num4_neq}: {result_not_equal_34}")

print("\nGreater than (>):")
print(f"{num1_gt} > {num2_gt}: {result_greater_than_12}")
print(f"{num3_gt} > {num4_gt}: {result_greater_than_34}")

print("\nLess than (<):")
print(f"{num1_lt} < {num2_lt}: {result_less_than_12}")
print(f"{num3_lt} < {num4_lt}: {result_less_than_34}")

print("\nGreater than or equal to (>=):")
print(f"{num1_ge} >= {num2_ge}: {result_greater_equal_12}")
print(f"{num3_ge} >= {num4_ge}: {result_greater_equal_34}")

print("\nLess than or equal to (<=):")
print(f"{num1_le} <= {num2_le}: {result_less_equal_12}")
print(f"{num3_le} <= {num4_le}: {result_less_equal_34}")
