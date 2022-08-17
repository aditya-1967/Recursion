def count(number):
    if number == 3:
        return
    print(number)
    count(number + 1)

count(0)