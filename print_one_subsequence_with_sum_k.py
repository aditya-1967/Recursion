# Print one subsequences with sum k

arr = [1,2,1]
k = 2
res, temp = [], []
def func(index, total):
    if index == len(arr):
        if total == k:
            res.append(temp.copy())
            return True
        return False
    temp.append(arr[index])
    total += arr[index]
    if func(index+1, total):
        return True
    temp.pop()
    total -= arr[index]
    if func(index+1, total):
        return True
    
    return False

func(0, 0)
print(res)