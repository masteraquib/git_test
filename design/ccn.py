arr = [1, 2,4, 6, 7, 8]
n = len(arr)
is_sorted = False
for i in range(n-2,-1,-1):
    for j in range(0, i+1):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            is_sorted =  True
    
    if not is_sorted:
        break

