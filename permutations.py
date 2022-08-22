# Print all permutations of given array
# leetcode 46
# Method 1

arr = [1,2,3]

ans, temp = [], []
freq = {i: False for i in range(len(arr))}

def permutations():
    if len(temp) == len(arr):
        ans.append(temp.copy())
        return
    for i in range(len(arr)):
        if freq[i] == False:
            freq[i] = True
            temp.append(arr[i])
            permutations()
            temp.pop()
            freq[i] = False
permutations()
print(ans)
            
