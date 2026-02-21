'''def tower_of_hanoi(n,source="A",helper="B",destination="C"):
    if n==0:
        return
    tower_of_hanoi(n-1,source,destination,helper)
    print(f"move disk from{source}->{destination}")
    tower_of_hanoi(n-1,helper,source,destination)  
tower_of_hanoi(3) 

def binary_search(arr,low,high,x):
    if high>=low:
        mid=low+(high-low)//2
        if arr[mid]>x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return-1
arr=[1,2,3,4,5,6,7,9,10,44]
x=6
result=binary_search(arr,0,len(arr)-1,x)
print(result)''' 

def insert_start(arr, value):
    arr.insert(0, value)

def insert_middle(arr, value):
    middle = len(arr) // 2
    arr.insert(middle, value)

def insert_end(arr, value):
    arr.append(value)

def delete_start(arr):
    if len(arr) == 0:
        print("Array is empty")
        return
    arr.pop(0)

def delete_middle(arr):
    if len(arr) == 0:
        print("Array is empty")
        return
    middle = len(arr) // 2
    arr.pop(middle)

def delete_end(arr):
    if len(arr) == 0:
        print("Array is empty")
        return
    arr.pop()

# Testing
arr = [1, 2, 3, 4, 5]

insert_start(arr, 7)
print("After insert_start:", arr)

insert_middle(arr, 8)
print("After insert_middle:", arr)

insert_end(arr, 9)
print("After insert_end:", arr)

delete_start(arr)
print("After delete_start:", arr)

delete_middle(arr)
print("After delete_middle:", arr)

delete_end(arr)
print("After delete_end:", arr)
