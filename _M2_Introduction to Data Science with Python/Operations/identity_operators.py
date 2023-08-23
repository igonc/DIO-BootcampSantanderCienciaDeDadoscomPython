# Identity Operators in Python
print("Identity Operators in Python")
# Example 1: "is" operator
x = [1, 2, 3]
y = x  # y is assigned to the same object as x
z = [1, 2, 3]

print("Example 1:")
print("x is y:", x is y)  # True, because x and y refer to the same object
print("x is z:", x is z)  # False, because x and z refer to different objects

print("In Example 1, the is operator is used to check if variables x and y refer to the same object (which they do because y was assigned the same object as x), and it also checks if x and z refer to the same object (which they don't because they are separate instances).")

# Example 2: "is not" operator
a = 5
b = 10

print("\nExample 2:")
print("a is not b:", a is not b)  # True, because a and b refer to different objects

print("In Example 2, the is not operator is used to check if variables a and b do not refer to the same object (which is true because they are distinct variables).")

# Example 3: Identity with custom objects
class MyClass:
    def __init__(self, value):
        self.value = value

obj1 = MyClass(1)
obj2 = MyClass(1)
obj3 = obj1  # obj3 is assigned to the same object as obj1

print("\nExample 3:")
print("obj1 is obj2:", obj1 is obj2)  # False, because obj1 and obj2 are different instances
print("obj1 is obj3:", obj1 is obj3)  # True, because obj1 and obj3 refer to the same object

print("In Example 3, identity operators are used to check the identity of custom objects. obj1 and obj2 are different instances of MyClass, so obj1 is obj2 is False. However, obj1 and obj3 refer to the same object, so obj1 is obj3 is True.")
