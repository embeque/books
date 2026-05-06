x = 28
# changed to find the cube root of the number

epsilon = 0.01
num_guesses, low = 0, min(x, 0)
high = max(1, x)
ans = (high + low) / 2
while abs(ans**3 - x) >= epsilon:
    print(f'low = {low}, high = {high}, ans = {ans}')
    num_guesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2

print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)
