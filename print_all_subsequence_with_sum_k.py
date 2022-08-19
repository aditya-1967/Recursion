# Print all subsequences with sum k

arr = [1,2,1]
k = 2
res, temp = [], []
def func(index, total):
    if index == len(arr):
        if total == k:
            res.append(temp.copy())
        return res
    temp.append(arr[index])
    total += arr[index]
    func(index+1, total)
    temp.pop()
    total -= arr[index]
    func(index+1, total)

func(0, 0)
print(res)