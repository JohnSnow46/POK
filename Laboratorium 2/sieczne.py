import math

# Defining Function

def f(x):
    #return  -(math.sin(x)*math.sin(x)) + x + math.log(x,10)
    return  -math.sin(x) + x*x + math.log(x,10)

# Implementing Secant Method

def secant(x0, x1, e, N):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print('Not Convergent!')
            break

        condition = abs(f(x2)) > e
    print('\n Required root is: %0.8f' % x2)


# Input Section
x0 = float(0.01)
x1 = float(0.94)
e = float(0.000001)
N = int(10)

# Starting Secant Method
secant(x0, x1, e, N)

