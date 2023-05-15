<h1>Data Structure and algorithm</h1>
<table>
    <tr>
        <th>Sr. No</th>
        <th>Chapter</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Introduction of data structure and algorithm</td>
    </tr>
    <tr>
        <td>2</td>
        <td>In-buit data structure in python</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Arrays</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Stack</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Queue</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Linked List</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Binary Tree</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Binary Search Tree</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Graph</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Hashing</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Algoritm Analysis</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Linear and Binary search</td>
    </tr>
    <tr>
        <td>13</td>
        <td>Sorting</td>
    </tr>
    <tr>
        <td>14</td>
        <td>Divide approach to programing</td>
    </tr>
    <tr>
        <td>15</td>
        <td>Greedy approach to programming</td>
    </tr>
    <tr>
        <td>16</td>
        <td>Dynamic Programming</td>
    </tr>
</table>

<h4>Introduction of Data Structure</h4>
<h5>What is a data structure ??</h5>
==> 
An extremely important part of the programming language.<br />
1) Data Structure are always of storing data in a efficient manner and accessing them as and when required.<br />
row text:-

    DS --> storing data --> in --> efficient manner and accessing--> when --> required.<br />

2) Lots of variables of data structures across programming language.<br />
3) Data Storage, Organization, accessibility and efficiency are at play all the time.<br />

    Data Storage --> data organisation --> access data --> efficiency == Data Structure

<h5>Types of data structure</h5>
<h6>There are 2 main Types:-</h6>
<table>
    <tr>
        <th>1</th>
        <th>Built-in data structure</th>
    </tr>
    <tr>
        <th>2</th>
        <th>User-define data structure</th>
    </tr>
</table>

<table>
    <tr>
        <th>Sr. No</th>
        <th>Built-in data structure</th>
        <th>User-define data structure</th>
    </tr>
    <tr>
        <td>1</td>
        <td>List</td>
        <td>Stack</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Dictionary</td>
        <td>Queue</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Tuple</td>
        <td>Tree</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Set</td>
        <td>Graph</td>
    </tr>
</table>

<h5>1) Builti-in Data Structures :</h5>
<h6>1) List:-</h6>
1. List are used to store data in a sequential manner.<br />
2. Negative indexing and positive indexing supported.<br />
3. Lists are supported indexing and slicing structure.<br />
4. List is an ordered collection of element enclosed within [].<br />
5. List are mutable.(change is supported, add, remove, and update)<br />
    
ex.

    L1 = [1, "a", False, "b", True]
    
o/p:

        [1, 'a', False, 'b', True]

<h6>2) Dictionary:-</h6>
1. Dictionary are one important data type in python.<br />
2. Data is stored in key:value pairs in the case of dictionaries.<br />
3. Pairs can be added, accessed and deleted as needed.<br />
4. Dictionary is an unordered collection of key-value pairs enclosed with {}.<br />
5. Dictionary are mutable.<br />

ex.
    
    dict_item = {'first':'apple', 'second':'Ball'}

o/p:

    {'first':'apple','second':'ball'}

ex.

    d1 = {"mango": 45, "apple": 30, "orange": 77, "guava": 125}

o/p:

    {"mango": 45, "apple": 30, "orange": 77, "guava": 125}

ex.

    d1.keys()

o/p:

    dict_keys(['mango', 'apple', 'orange', 'guava'])

<h6>3)Tuple :-</h6>
1. Tuples are most used data structure in python.<br />
2. works similar to that of list but this is immutable.<br />
3. so, data one entered into a tuple connot be changed.<br />
4. Tuple is an ordered collection of element enclosed within().<br />
5. Tuple are immutable.<br />
6. Heterogeneous collection of Data(Various type of data we can store in Tuple).<br />

ex.
    
    sample_tuple = (1, 3, 2)

o/p:

    (1, 3, 2)

ex.
    
    tup1 = (1, "a", True, "b", 23.0)

o/p:

    (1, "a", True, "b", 23.0)

<h6>4)Set :-</h6>
1. Sets are collection of unordered unique element.<br />
2. Every data element in set must be unique.<br />
3. The operations are similar to the sets you might.<br />
4. enclosed with {}.<br />


<h2>Array Data Structure :-</h2>


<h6>What is array??</h6>
1. Linear Data structure<br />
2. Contiguous memory locations<br />
3. Access elements randomly<br />
4. Homogeneous elements i.e. similar elements.<br />

Ex.<br />

    cars_arr = ["ford", "volvo", "BMW"]

indexing -  "ford" = 0
            "Volvo" = 1
            "BMW" = 2

access element :<br />

    x = cars_arr[1]
o/p:<br />
    
    'Volvo'

<h6>Applications of array : </h6><br />
1. Storing information - linear fashion.<br />
2. Suitable for applications that require frequent searching.<br />

<h6>Declaration an initialization of arrays : </h6>
1. Array declaration:<br />
    * Datatypes varname[size];<br />
2. Can also do declaration and initialization at once:<br />
    * Datatypes varname[] = {ele1, ele2, ele3};<br />
   
ex.<br />

<table>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
    <th>5</th>
</table>

* 0 to 4 indexing start from <br />
* 1 to 5 are storing data/element<br />

<table>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
    <th>5</th>
    <tr>
        <td>100</td>
        <td>104</td>
        <td>108</td>
        <td>112</td>
        <td>116</td>
    </tr>
</table>

* 100 to 116 are address of element which are store in arrays<br />

<h6>2- Dimensional Array -</h6><br />
1. 2D can be related to a table or matrix.<br />
2. Elements are stored one after another i.e. one 1D arrays inside other.<br />
3. Two subscripts or indices are used, one row and one colomn.<br />
4. Dimensions depends upn the number of subscripts used.<br />


![arrayDispalying](https://github.com/tedy-art/Data-structure-and-algorithm/blob/main/img.png) <br />

<h6>Array Implementation : </h6> 
1. Create a one-dimensional integer array and insert number to the maximum size provided until end of the array. Access the numbers inserted and then display the same as output???<br />


    print("How many elements to store inside the array", end="")
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

o/p:

    How many elements to store inside the array :3

    Enter  3 element :2
    5
    1

    The array elements are
    2 5 1 

2. Create a two-Dimentional integer array and insert numbers to the maximum size provided until the end of the array. Access the numbers inserted and then display the same as output.<br />
    

        r_num = int(input("Input number of rows : "))
        c_num = int(input("Input number of cols : "))
        twod_arr = [[0 for col in range(c_num)] for row in range(r_num)]

        for row in range(r_num):
            for col in range(c_num):
                twod_arr[row][col] = row * col
            print(twod_arr)

o/p:

        Input number of rows : 2
        Input number of cols : 3
        [[0, 0, 0], [0, 0, 0]]
        [[0, 0, 0], [0, 1, 2]]


3. Write a program that initialize a 2-D arrays of size m x n with the value 0,
and then sets the diagonal elements to the value 1


        m = 4
        n = 4
        arr = [[0 for j in range(n)] for i in range(m)]
        for i in range(min(m, n)):
            arr[i][i] = 1
        print(arr)


o/p:

        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

<h6>Delete Operation</h6>


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

<h6>Sort Operations -</h6>


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

o/p:

    Elements of original array : 
    10 22 38 27 11 
    Elements of array sorted in ascending order : 
    10 11 22 27 38

<h6>Search Array - </h6>
    
    # Search element in array
    
    import array
    
    arr = array.array('i', [1, 2, 3, 1, 2, 5])
    print("The new created array is :", end=" ")
    for i in range(0, 6):
        print(arr[i], end=" ")
    print("\r")
    print("The index 1st occurrence of 2 is : ", end=" ")
    print(arr.index(2))
    
    print("The index 1st occurrence of 1 is : ", end=" ")
    print(arr.index(1))

o/p:

    The new created array is : 1 2 3 1 2 5 
    The index 1st occurrence of 2 is :  1
    The index 1st occurrence of 1 is :  0

<h6>Advantages of Array : </h6>
1. Random access element.<br />
2. Easy sorting and iteration.<br />
3. Replacement of multiple variables.<br />

<h6>Disadvantages of Array : </h6>
1. Size is fixed.<br />
2. Difficult to insert and delete.<br />
3. If Capacity us more and occupancy less, most of the array get wasted.<br />
4. Needs contiguous memory.<br />

<h2>Stack Data Structure</h2>
<h5>Agenda : </h5>
<table>
    <tr>
        <th>Sr. no</th>
        <th>Topics</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Introduction of Stack</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Functions associated with Stack</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Implementation of stack</td>
    </tr>
</table>

<h5>Introduction of Stack : </h5>
1. Linear data structure.<br />
2. It follows Last in first out(LIFO) order.<br />
3. Insertion and removal of the element has done at one point.<br />
4. Push is used for inserting an element in a stack.<br />
5. pop is used to removal an element in a stack<br />

<table>
    <tr>
        <td>23</td>
        <td>45</td>
        <td>67</td>
        <td>89</td>
        <td>11</td>
        <td>15</td>
    </tr>
</table>
push()-->


<table>
    <tr>
        <td>15</td>
    </tr>
    <tr>
        <td>11</td>
    </tr>
    <tr>
        <td>89</td>
    </tr>
    <tr>
        <td>67</td>
    </tr>
    <tr>   
        <td>45</td>
    </tr>
    <tr>
        <td>23</td>
    </tr>
</table>


<h6>LIFO</h6> pop()--> 15 

push() = Inserting Element.<br />
pop() = Removing Element.<br />

<h5>Function associated with stack : </h5><br />
<h6>1.push(x) : </h6>
It is used insert the element 'x' at the end of a stack.<br />

<h6>2.pop() : </h6>
It is used to remove the top most / last element of a stack.<br />

<h6>3.size() : </h6>
Gives the size/ length of a stack.<br />

<h6>4.top() : </h6>
Give reference of last element present in stack.<br />

<h6>5.empty() : </h6>
returns true for an empty stack<br />

<h5>Several ways to implementation stack in python : </h5>
1. list<br />
2. collections.deque<br />
3. queue.LifeQueue<br />

<h5>Implementation using list : </h5>
1. List in python can be used as stack.<br />
2. append()- It is used to insert the element.<br />
3. pop()- It is used to remove the last element.<br />

<h6>logic :</h6>

    stack = []
    stack.append("abc")
    print(stack.pop())

<h6>Implementation using list :</h6>
    
    stack = []
    stack.append("Welcome")
    stack.append("to")
    stack.append("great learning")
    print(stack)
    print(stack.pop())
    
    print(stack)
    print(stack.pop())
    
    print(stack)

o/p:

    ['welcome', 'to', 'great learning']
    great learning
    ['welcome', 'to']
    to
    ['welcome']

<h5> Implementation using collection.deque :</h5>
1. Stack in python are crated by the collection module which provides deque class.<br />
2. append() and pop() operations are faster in deque as compare to list.<br />

<h6>Logic :</h6>

    from collections import deque
    stack = deque()
    stack.append("abc")
    print(stack.pop())

<h6>Implementation using deque :</h6>

    from collections import deque
    stack = deque()
    stack.append("x")
    print(stack)
    stack.append("y")
    stack.append("z")
    print(stack)
    print(stack.pop())
    print(stack)

o/p:

    deque(['x'])
    deque(['x', 'y', 'z'])
    z
    deque(['x', 'y'])


<h5> Implementation using queue :</h5>
1. Queue module contains the LIFO function.<br />
2. It is having some additional functions and work same as stack.<br />
3. put() function is used to insert the data in queue.<br />
4. get() function is used to remove the element.

<h6>Functions available in queue module :</h6>
<h6>1.get() : </h6>
It is used to remove the element from the queue.

<h6>2.maxsize() : </h6>
Used to put the maximum number of items allowed in queue.<br />

<h6>3.empty() : </h6>
It returns true, when queue is empty, else false.<br />

<h6>4.full() : </h6>
when queue is full returns True.<br />

<h6>5.put(x) : </h6>
It is used to insert x in queue.<br />

<h6>5.qsize() : </h6>
Gives the size of a queue.<br />

get() = insert element.<br />
put() = remove element.<br />

<h6> Implementation using queue :</h6>

    # Implementation using queue
    from queue import LifoQueue

    # assign LifoQueue() function to stack variable
    stack = LifoQueue(maxsize = 3) # maxsize of stack is 3
    stack.put(2) # insert 1st element
    stack.put(3) # insert 2st element
    stack.put(4) # insert 3st element
    print(stack.qsize()) # size of stack
    print(stack.full()) # True (stack is full)
    print(stack.get()) # remove
    print(stack.full()) # false (stack is not full)

o/p:

    3
    True
    4
    False


<h5>Advantages of Stack :</h5>
1. Maintains data in LIFO manner.<br />
2. The Last elements are ready for use.<br />
3. All operations are of O(1) complexity.<br />

<h5>Disadvantages of Stack :</h5>
1. Manipulation is restricted to the top of the stack.<br />
2. Not much flexible.<br />