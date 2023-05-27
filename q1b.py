def is_palindrome(number):
    temp = number
    c = 0
    while int(temp) > 0:
        c *= 10
        c += temp % 10
        temp = temp // 10
    if c == number:
        return True
    else:
        return False


def counter(number):
    str_num = str(number)
    checker = []
    print('Number : count')
    for i in str_num:
        if i not in checker:
            checker.append(i)
            print(i + ' : ' + str(str_num.count(i)))


# program starts here

num = int(input('Enter a number'))
if is_palindrome(num):
    print(f'{num} is palindrome')
else:
    print(f'{num} is not a palindrome')

counter(num)
