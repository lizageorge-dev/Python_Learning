numbers=[64, 25, 12, 22, 11]
# Traverse through all array elements
for i in range(len(numbers)):
    # Find the minimum element in remaining unsorted array
    min_idx = i
    for j in range(i+1, len(numbers)):
        if numbers[min_idx] > numbers[j]:
            min_idx = j
    # Swap the found minimum element with the first element
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
print("The sorted numbers are: ", numbers)
