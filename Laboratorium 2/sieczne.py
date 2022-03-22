import math

def f(x):

    y = x*x + math.log(x)
    return y

def metoda(a,b,delta,dokl):

    while delta > dokl:
        x1 = a - f(a) * ((b-a)/(f(b) - f(a)))
        if f(x1)*f(a) > 0:
            a = x1
        else:
            b = x1
        delta = abs(f(x1))
        print("x1={:.2f} a={:.2f} b={:.7f} c={:.7f} ".format(x1,a,b,delta))
        return [x1,a,b,delta]
x1_start = 0.4
x2_start = 5.0
delta_0 = 10000.0
dokl_fin = 0.00001
res = metoda(x1_start, x2_start, delta_0, dokl_fin)
print("\n \n \n final result: x1.{:.2} a={:.7f} b={:.7f} c={:.2f} ".format(res[0],res[1],res[2], res[3]))
