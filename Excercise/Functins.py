"""
# This function calculates the final price after applying a discount to the original price.
def calculate_price(original_price, discount=.10):
    final_price = original_price - (original_price * discount)
    return final_price
calculated_price = calculate_price(100)
print("The final price after discount is: ", calculated_price)

### This program demonstrates the use of functions in Python. It includes functions to convert pounds to kilograms, feet to meters, and to calculate the Body Mass Index (BMI) based on weight and height.
def lbs_to_kg(pounds):
    kilograms = pounds * 0.453592
    return kilograms
def feet_to_meters(feet):
    meters = feet * 0.3048
    return meters
def calculate_BMI(weight, height):
    bmi = weight / (height ** 2)
    return bmi
bmi = calculate_BMI(weight=lbs_to_kg(150), height=feet_to_meters(5.75))
print("The BMI is: ", bmi)
##### This function checks if three given sides can form a triangle based on the triangle inequality theorem.
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
triangle_sides = is_triangle(3, 4, 5)
if triangle_sides:
    print("The sides can form a triangle.") 
else:
    print("The sides cannot form a triangle.")

    #############tuple unpacking
destination=(34.0522, -118.2437)
lat, lon = destination
print("Latitude: ", lat)
lattitude=destination[0]
longitude=destination[1]
print("Latitude: ", lattitude)
print("Longitude: ", longitude)
#factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number=factorial(5)
print("The factorial of 5 is: ", number)

# Complete the code to correctly use the count() method to find the number of duplicates of 2 in the following tuple.
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
print(duplicates)    # outputs: 4

#Write a program that will "glue" the two dictionaries (d1 and d2) together and create a new one (d3).
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
 
for item in (d1, d2):
    d3.update(item)
 
print(d3)
#Write a program that will convert the my_list list to a tuple.
my_list = ["car", "Ford", "flower", "Tulip"]

t =  tuple(my_list)
print(t)
colors = (("green", "#008000"), ("blue", "#0000FF"))
 
# Write your code here.
colors_dictionary = dict(colors)
 
print(colors_dictionary)
###############################################
try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except:
    print('I do not know what to do.')
    #########################################
    alpha = [4, 8, 15, 16, 23, 42]
beta = alpha[:]
beta[2] = 99
print(alpha)  # outputs: [4, 8, 15, 16, 23, 42]
print(beta)   # outputs: [4, 8, 99, 16,

"""
for i in range(5):
    if i % 2 == 0:
        continue
    print(i, end=" ")










