"""
 Write a Python program to append a new item to the end of the array.
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Append 11 at the end of the array:
New array: array('i', [1, 3, 5, 7, 9, 11])
"""

from array import array

Original_array = array('i', [1, 3, 5, 7, 9])
print(f"Original array: {Original_array}")
new_array = Original_array
new_array.append(11)
print(f"new array: {new_array}")
