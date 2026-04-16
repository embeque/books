# Edit the code to find the largest divisor

# Test if an int > 2 is prime. If not, print smallest divisor
x = int(input("Enter an integer greater than 2: "))
largest_divisor = None 
for guess in range(2, x):
    if x % guess == 0:
        largest_divisor = guess
        #break
if largest_divisor != None:
    print(f"Largest divisor of {x} is {largest_divisor}")
else:
    print(f"{x} is a prime number")

# Not used hint,
# if i should have used hint it should be like this
# uncomment the break statement on line 9

smallest_divisor = int(x / largest_divisor)
print(f"and the smallest divisor of {x} is {smallest_divisor}")
