num = int(input("Enter an integer: "))
run = True
for root in range(1, num):
    for pwr in range(2, 6):     # powers will be in between 2 and 5
        if root**pwr == num:
            run = False
            break
    if run == False:
        break

if run == False:
    print(f"Root: {root}, Power: {pwr}")
else:
    print(f"There don't exist a pair of root and power for x value: {num}")
