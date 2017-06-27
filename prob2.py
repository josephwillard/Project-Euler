sum_evens = 2

def fibonacci(a1, a2):
    
    global sum_evens
    
    if a1 + a2 > 4000000:
        pass

    else:
        if (a1+a2) % 2 == 0:
            sum_evens = sum_evens + a1 + a2
        fibonacci(a2, a2+a1)
        
    
