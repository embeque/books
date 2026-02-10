x = 10
y = 13
z = 7
# Code starts from here

# Second try
res = min(x,y,z)
if(x%2!=0 and (x>y and x>z)):
    res = x
if(y%2!=0 and (y>x and y>z)):
    res = y
if(z%2!=0 and (z>x and z>y)):
    res = z


# First Try
#res = min(x,y,z)
#if(x%2!=0 and (x>y or x>z)):
#    res = x
#if(y%2!=0 and (y>x or y>z)):
#    res = y
#if(z%2!=0 and (z>x or z>y)):
#    res = z



# Code ends between here

print("Result:", res)

