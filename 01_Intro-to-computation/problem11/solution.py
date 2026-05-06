low = 0
high = 102
eggCount = 0
ans = high
#ans = (low + high) // 2
while ans > 0:
    eggCount += 1
    if True:
        high = ans
    else:
        low = ans
    print(f'egg broke at {ans} floor')
    ans = (low + high) // 2

print(f'total egg required to check this test is {eggCount}')
