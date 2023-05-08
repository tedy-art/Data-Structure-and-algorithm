"""
1 . Create a 1-D integer array and insert numbers to the maximum size provided until end
    of the array. Access the numbers inserted and then display the same as output.
"""

print("How many elements to store inside the array :", end="")
num = input()
arr = []
print("\n Enter ",num, "element :", end="")
num = int(num)
for i in range(num):
    element = input()
    arr.append(element)
print("\nThe array elements are")
for i in range(num):
    print(arr[i], end=" ")