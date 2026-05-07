k = 2400012348715369    # number of which we have to find the square root
# Newton-Raphson for square root
# Find x such that x**2 -24 is within epsilon of 0.01
nr_count = 0
epsilon = 0.01
guess = k/2
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    nr_count += 1
print(f'Square root of {k} is about {guess} with Newton-Raphson method with number of guesses {nr_count}')

 
# Exact copy paste of code from bisection search with some editing
x = k
# changed to find the cube root of the number

epsilon = 0.01
num_guesses, low = 0, min(x, 0)
high = max(1, x)
ans = (high + low) / 2
while abs(ans**2 - x) >= epsilon:
#    print(f'low = {low}, high = {high}, ans = {ans}')
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2

print(f'Square root of {x} is about {ans} with Bisection method with number of guesses {num_guesses}')
effi = (num_guesses - nr_count)*100 / num_guesses
print(f'Newton-Raphson method is {effi:.2f}% times more efficient then bisection method')
