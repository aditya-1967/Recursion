string1 = 'abba'
string2 = 'abcd'

def checkPalindrome(string, index):
    if index >= len(string)/2:
        return True
    if string[index] != string[len(string) - index - 1]:
        return False
    return checkPalindrome(string, index + 1)

print(checkPalindrome(string1, 0))
print(checkPalindrome(string2, 0))