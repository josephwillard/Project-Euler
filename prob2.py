def sum_evens():
    a1 = 1
    a2 = 2
    sum = 0

    while True:
        if fibonacci(a1, a2) < 4000000:
            if a2 % 2 == 0:
                sum = sum + a2

            # elif a2 % 2 == 0:
            #     sum =  sum + a2
        else:
            break
            
        a3 = a1 + a2
        a1 = a2
        a2 = a3
    return sum

print(sum_evens())
            
