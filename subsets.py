# Subsets II
# Leetcode 90

arr = [1,2,3]
res, temp = [], []
def subset(index):
    res.append(temp.copy())
    for i in range(index, len(arr)):
        if i != index and arr[i] == arr[i-1]:
            continue
        temp.append(arr[i])
        subset(i+1)
        temp.pop()

arr.sort()
subset(0)
res.sort(key = len)
print(res)