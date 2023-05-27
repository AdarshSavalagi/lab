def function(n):
    if n < 0:
        print('Invalid input')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return function(n-1) + function(n-2)


num = int(input('Enter value of n: '))
print(function(num))
