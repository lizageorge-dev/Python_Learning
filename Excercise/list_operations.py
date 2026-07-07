# This program demonstrates list operations in Python. It takes a comma-separated string of numbers from the user, splits it into a list, and then converts the list of strings into a list of integers.
input_number = input("Enter 5 comma-separated numbers : ")
numbers = input_number.split(",")
print("The numbers you entered are: ", numbers)
# Convert the list of strings to a list of integers
numbers = [int(num) for num in numbers]
print("The numbers in integer format are: ", numbers)
# Now we will sort the list of numbers using both the sorted() function and the sort() method.
sorted_numbers = sorted(numbers)
print("The sorted numbers are: ", sorted_numbers)
# Alternatively, we can use the sort() method to sort the list in place.
numbers.sort()
print("The numbers in sorted order are: ", numbers)
# We can also sort the numbers in reverse order using the sorted() function with the reverse parameter set to True.
reverse_sorted_numbers = sorted(numbers, reverse=True)
print("The numbers in reverse sorted order are: ", reverse_sorted_numbers)
# Finally, we will demonstrate how to append a new number to the list and then print the updated list.
numbers.append(10)
print("After appending 10 to the list: ", numbers)
numbers.remove(10)
print("After removing 10 from the list: ", numbers)