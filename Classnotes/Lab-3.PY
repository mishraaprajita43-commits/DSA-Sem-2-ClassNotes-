#Q.9- 
def pushZeroTOEnd(arr):
    n = len(arr)
    temp = [0] * n   
    j = 0

    for i in range(n):
        if arr[i] != 0:     
            temp[j] = arr[i]
            j += 1

    for i in range(n):
        arr[i] = temp[i]   


if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5]
    pushZeroTOEnd(arr)
    print(arr)

#QNO.5 
def kthLargest (arr,k):
    arr.sort(reverse=True)
    return arr [k-1]
    print (kthLargest(arr,k))