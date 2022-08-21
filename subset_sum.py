# Subset Sum I

arr = [3, 1, 2]
ans = []

def subset_sum(index, total):
    if index == len(arr):
        ans.append(total)
        return
    subset_sum(index + 1, total + arr[index])
    subset_sum(index + 1, total)

subset_sum(0, 0)
ans.sort()
print(ans)
    
