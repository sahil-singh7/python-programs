# Print Fibonacci Series to n terms

def fibonacci(num):
    print("The terms are:")

    a = 0
    b = 1

    for i in range(num):
        print(a,  end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter the numbers of terms:"))
fibonacci(n)
