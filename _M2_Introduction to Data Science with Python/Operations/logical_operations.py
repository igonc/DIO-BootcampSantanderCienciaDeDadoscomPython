print("Logical Operations in Python")

# Logical Operations in Python with Different Variables and Pairs Evaluation

# Logical AND (and)
num1_and_true = True
num2_and_true = True
result_and_true_true = num1_and_true and num2_and_true  # True

num1_and_true = True
num2_and_false = False
result_and_true_false = num1_and_true and num2_and_false  # False

num1_and_false = False
num2_and_true = True
result_and_false_true = num1_and_false and num2_and_true  # False

num1_and_false = False
num2_and_false = False
result_and_false_false = num1_and_false and num2_and_false  # False

# Logical OR (or)
num1_or_true = True
num2_or_true = True
result_or_true_true = num1_or_true or num2_or_true  # True

num1_or_true = True
num2_or_false = False
result_or_true_false = num1_or_true or num2_or_false  # True

num1_or_false = False
num2_or_true = True
result_or_false_true = num1_or_false or num2_or_true  # True

num1_or_false = False
num2_or_false = False
result_or_false_false = num1_or_false or num2_or_false  # False

# Logical NOT (not)
result_not_and_true_true = not result_and_true_true  # False
result_not_and_true_false = not result_and_true_false  # True
result_not_and_false_true = not result_and_false_true  # True
result_not_and_false_false = not result_and_false_false  # True

result_not_or_true_true = not result_or_true_true  # False
result_not_or_true_false = not result_or_true_false  # False
result_not_or_false_true = not result_or_false_true  # False
result_not_or_false_false = not result_or_false_false  # True

# Printing the results
print("Logical AND (and) Results:")
print("True and True:", result_and_true_true)
print("True and False:", result_and_true_false)
print("False and True:", result_and_false_true)
print("False and False:", result_and_false_false)

print("\nLogical OR (or) Results:")
print("True or True:", result_or_true_true)
print("True or False:", result_or_true_false)
print("False or True:", result_or_false_true)
print("False or False:", result_or_false_false)

print("\nLogical NOT (not) Results for AND:")
print("not (True and True):", result_not_and_true_true)
print("not (True and False):", result_not_and_true_false)
print("not (False and True):", result_not_and_false_true)
print("not (False and False):", result_not_and_false_false)

print("\nLogical NOT (not) Results for OR:")
print("not (True or True):", result_not_or_true_true)
print("not (True or False):", result_not_or_true_false)
print("not (False or True):", result_not_or_false_true)
print("not (False or False):", result_not_or_false_false)
