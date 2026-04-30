def find_root(x, power, epsilon):
    # Find interval containing answer
    if x < 0 and power%2 == 0:
        return None  # Negative number has no even powered roots
    low = min(-1, x)
    high = max(1, x)
    # Use bisection search
    ans = (high + low) / 2
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

epsilon = 0.001
sam = 0
roots = [ [25, 2], [-8, 3], [16, 4] ]
for value, power in roots:
    try:
        sam += find_root(value, power, epsilon)
    except TypeError:
        print(f'there don\'t exist a {power} root for {value}')
print(f'The sum of all the given roots is {sam}')
