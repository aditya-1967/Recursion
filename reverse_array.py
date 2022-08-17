# Reverse an array

# Method 1 
arr = [1,2,3,4,5,6,7,8,9,10,11,12]
left, right = 0 , len(arr) - 1
def reverse(left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse(left+1, right-1)

print(arr)
reverse(left, right)
print(arr)

# Method 2

def reverse2(index):
    if index >= len(arr) / 2:
        return
    arr[index] = arr[len(arr) - index - 1]
    reverse2(index + 1)
reverse2(0)
print(arr)