# Define the original array
arr = [10, 22, 38, 27, 11]

# Initialize a variable to use for swapping array elements
temp = 0

# Displaying elements of original array
print("Elements of original array : ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

# sort the array in ascending order
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            # Swap the elements using the temporary variable
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print()

# Displaying elements of the array after sorting
print("Elements of array sorted in ascending order : ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")