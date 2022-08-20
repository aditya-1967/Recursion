# Print all Subsequence

arr = [3,1,2,4]

res = []
temp = []
def func(index):
    if index == len(arr):
        res.append(temp.copy())
        return res
    temp.append(arr[index])
    func(index + 1)
    temp.pop()
    func(index + 1)

func(0)
print(res)
