print('Enter your marks')
mark = []

try:
    for i in range(3):
        ele = int(input(f'Test: {(i + 1)}: '))
        mark.append(ele)
except Exception as e:
    print('Exception: ' + str(e))

mark.sort()
print(f'The best of 2 out 3 tests are :{mark[1]} & {mark[2]}')
ave = (mark[1] + mark[2]) / 2
print('Average: ' + str(ave))
