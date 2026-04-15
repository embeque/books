sum = 2
for i in range(3,999,2):
    isprime = True
    for j in range(2,i):
        if i % j == 0:
            isprime = False

    if isprime == True:
        print(f"{i} is a prime number...check it.")
        sum += i

print(sum)
