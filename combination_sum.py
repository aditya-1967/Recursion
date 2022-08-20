# Combination Sum I
# Leetcode 39.

arr = [2,3,6,7]
target = 7

res, temp = [], []

def combination_sum(index, target):
    if index == len(arr):
        if target == 0:
            res.append(temp.copy())
        return
    if arr[index] <= target:
        temp.append(arr[index])
        combination_sum(index, target - arr[index])
        temp.pop()
    combination_sum(index + 1, target)

combination_sum(0, target)
print(res)