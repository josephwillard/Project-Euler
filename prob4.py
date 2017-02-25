import math 

#x = range(100,1000)

def palindrome(x):
    n = len(str(x))
    
    if n % 2 == 0:
        m = int(n / 2)
    elif n % 2 != 0:
        m = math.floor(n/2)

    l = [str(x)[i] for i in range(m)]
    p = [str(x)[n - 1 - i] for i in range(m)]

    if l == p:
        return True
    else:
        return False

    
        
def palindrome_list(x):
    pal = []
    for j in range(100, 1000):
        l = [j*x[i] for i in range(len(x))]
    
    
        for i in range(len(l)):
            if palindrome(l[i]) == True:
                pal.append(l[i])
            else:
                pass
        
    return max(pal)
