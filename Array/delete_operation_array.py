# Delete Operation
print(end="Enter the size of array : ")
tot = int(input())
arr = []
print(end="Enter "+str(tot)+" elements: ")
for i in range(tot):
    arr.append(input())
print(arr)

print(end="\n Enter the value to delete : ")
val = input()
if val in arr:
    arr.remove(val)
    print("\n The new Array is : ")
    for i in range(tot - 1):
        print(end=arr[i] + " ")
else:
    print("\n Element doesn't exist in the array!")