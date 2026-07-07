# Function to greet a user by name, defaulting to "Guest" if no name is provided
def greet_user(name="Guest") :
    if name == "Guest":
      print("Hello, Guest!")
    else:
       print(f"Hello, {name}!")

greet_user("Baby")
greet_user()
#Function to add two numbers
def add_numbers(a, b):
    return a + b
a = add_numbers(5, 3)
print(a)
# #Function to check if a number is even
def is_even(num):
    return num % 2 == 0 
print(is_even(4))  # True
print(is_even(3))  # False