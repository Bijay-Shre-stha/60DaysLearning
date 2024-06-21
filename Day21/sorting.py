# implementing sorting without using the built-in sort function

def sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [3, 2, 1, 5, 4]
print(sort(arr))
alphabet = ['c', 'a', 'b', 'e', 'd']
print(sort(alphabet))