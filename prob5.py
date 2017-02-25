import math as m
import itertools as ite


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




def prime_factorization(x):
    num = x
    fac = []
    i = 1
    while True:
        
        if (num%i == 0):
            if prime(i) == True:
                fac.append(i)
                num = num/i
            else:
                i += 1
        else:
            i += 1
        if num == 1:
            break
    return fac


def flatten_list(x):
    # Flatten List
    flat_list = []
    for i in range(len(x)):
        if type(x[i]) == int:
            flat_list.append(x[i])
        else:
            for j in range(len(x[i])):
                flat_list.append(x[i][j])
    return flat_list

def LCD(x):
    lcd = []
    prime_fact = []
    
    for i in range(x):
        if len(lcd) == 0:
            lcd.append(prime_factorization(i+1))
            lcd = flatten_list(lcd)
        else:
           prime_fact = prime_factorization(i+1)
           for j in range(len(lcd)):
               if lcd[j] in prime_fact:
                  prime_fact.remove(lcd[j])
           lcd.append(prime_fact)
           lcd = flatten_list(lcd)

    
    return lcd


#multiplying everything together
lcd = 1
factors = LCD(20)

for i in range(len(factors)):
    lcd = lcd*factors[i]

print(lcd)

