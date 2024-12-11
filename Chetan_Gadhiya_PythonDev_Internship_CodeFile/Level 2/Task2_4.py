def fibonacci(terms):
    if terms <= 0:
        print("Error : please Enter terms >= 0.")
        return
    
    fibonacci_seq = []
    a,b = 0,1
    for _ in range(terms):
        fibonacci_seq.append(a)
        a,b = b, a+b
    return fibonacci_seq
    
terms = int(input("Enter number of terms you need in Fibonacci sequence : "))
fibonacci_seq = fibonacci(terms)
print(fibonacci_seq)
