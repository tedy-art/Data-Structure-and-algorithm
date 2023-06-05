"""
Write a Python program to get the length in bytes of one array item in the internal representation.
Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Length in bytes of one array item: 4
"""

from array import *

array_ele = array('i',[1, 3, 5, 7, 9])
print("original array : ", str(array_ele))
print(f"length of an array is : {str(array_ele.itemsize)}")
