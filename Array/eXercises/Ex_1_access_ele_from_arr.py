"""
1. Write a Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.
    Sample Output:
    1
    3
    5
    7
    9
     Access the first three items individually
    1
    3
    5
"""
from array import array

# implementation of an array
array_num = array('i',[1, 3, 5, 7, 9])

for i in array_num:
    print(i)

print("Using simple method/ using square brackets []")
print(array_num[0])
print(array_num[1])
print(array_num[2])