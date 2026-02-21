#q.no.2-Given an array of insteger perform the following operation: 
# reverse the array find the main and min elements andcalorate the sum 
# and average of the elments. Impleent function to paform each operation and 
#ensure the time complimity is optional.

def reverse_array(arr):
    left=0
    right=len(arr)-1
    
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

def find_max(arr):
    max_val=arr[0]
    for i in arr:
        if i>max_val:
            max_val=i 

        return max_val

def find_min(arr):
    min_val=arr[0]
    for i in arr:
        if i in arr:
            min_val=i
    return min_val