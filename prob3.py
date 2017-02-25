import math as m



def prime(x):
    i = 2
    t = 0
    test_num = m.ceil(m.sqrt(x))
    if x == 2 or x == 1:
        return True
    else:
        while i <= test_num:
            if x % i == 0:
                t += 1
            else:
                pass
            i += 1
        if t == 0:
            return True
        else:
            return False
    

            
def factorization(x):
    """
    This uses the square root test and tests every integer between 1 and the ceiling of the square root. During this process if it encounters a number that divides x it checks whether the number or its remainder from division is prime and appends it.
    """
    test_num = m.ceil(m.sqrt(x))
    factors = []
    i = 1
    while i <= test_num:
        if x%i == 0:
            if prime(i) == True:
                factors.append(i)
            if prime(x/i) == True:
                factors.append(int(x/i))
            else:
                pass
        else:
            pass
        i += 1
    return max(factors)

        

print(factorization(600851475143))

