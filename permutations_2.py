# Print all permuatations of given arr
# Leetcode 46
# Method 2

arr = [1,2,3]

ans = []

def permuatations(index):
    if index == len(arr):
        temp = []
        for i in range(len(arr)):
            temp.append(arr[i])
        ans.append(temp)
        return
    
    for i in range(index, len(arr)):
        arr[i], arr[index] = arr[index], arr[i]
        permuatations(index + 1)
        arr[i], arr[index] = arr[index], arr[i]

permuatations(0)    
print(ans)