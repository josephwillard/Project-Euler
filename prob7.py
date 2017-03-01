import math as m

x = 0
i = 1
def prime(x):
 a = m.ceil(m.sqrt(x))
 b = 0
 if x == 2:
     return True
 elif x == 1:
     return False
 else:
    for i in range(1,a+1):
        if x%(i) == 0:
            b += 1
    if b > 1:
        return False
    else:
        return True

while x < 10001:
    if prime(i) == True:
        x += 1
        i += 1
    else:
        i += 1
print(i - 1)
