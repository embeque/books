x = 10
y = 13
z = 7


answer = min(x,y,z)
if(x%2!=0):
    answer = x
if(y%2!=0 and y > answer):
    answer = y
if(z%2!=0 and z > answer):
    answer = z


print(answer)
