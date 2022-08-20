# Combination Sum II
# Leetcode 40

arr = [10, 1, 2, 7, 6, 1, 5]
target = 8

res, temp = [], []
arr.sort()
def combination_sum_2(index, target):
    if target == 0:
        res.append(temp.copy())
        return
    for i in range(index, len(arr)):
        if i > index and arr[i] == arr[i-1]:
            continue
        if arr[i] > target:
            break
        temp.append(arr[i])
        combination_sum_2(i+1, target - arr[i])
        temp.pop()
combination_sum_2(0, target)
print(res)