# Count all subsequences with sum k

arr = [1,2,1,3,5,1,2,3,4,1,2,1,2]
k = 6
temp = []
global count
count = 0
def func(index, total):
    global count
    if index == len(arr):
        if total == k:
            count += 1
        return count
    temp.append(arr[index])
    total += arr[index]
    func(index+1, total)
    temp.pop()
    total -= arr[index]
    func(index+1, total)

func(0, 0)
print(count)