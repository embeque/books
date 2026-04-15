largestodd = 0;
i = 0
while (i < 10):
    num = int(input("Enter a number: "))
    if num % 2 != 0 and num > largestodd:
        largestodd = num

    i += 1

if largestodd == 0:
    print("No Odd Number is Entered.")
else:
    print(f"The largest odd number entered is {largestodd}.")
