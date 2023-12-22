#y(x)−∫10ssinxy(s)ds=x,x∈[0,1]
import matplotlib.pyplot as plt
import numpy as np
h=0.1
xi=np.arange(0,1,h)
sj=np.arange(0,1,h)
#print(xi.size)
y=np.zeros(xi.size)
g=y
l=1
a=np.ones(xi.size)

a[:]=h
a[-1]=h/2
a[0]=a[-1]
def ys(y,i):
    g[:]=0
    for j in range(i):
        g[i]=g[i]+y[j-1]

    return g[i]



def trap(y,i,h):
    s=0
    for j in range(1,i):

        s=s+((j*h*np.sin(xi[i])*y[j]+(j-1)*h*np.sin(xi[i-1])*y[j-1])/2)*h
    return s


for i in range(xi.size):
    y[i] = 2 * xi[i] / (2 - h * xi[i] * 2 * np.sin((i) * h))
for i in range(0,xi.size):

    y[i]=trap(y,i,h)+xi[i]
print(y)
plt.plot(xi,y)
plt.show()

'''
def trapezoidal_rule_integration(f, a, b, n):
    h = (b - a) / n # шаг
    result=0
    x = np.linspace(a, b, n+1) # точки разбиения
    y = f(x) # значения функции на точках разбиения
    for i in range(x.size):
        result=result+(x[i]-x[i-1])*(y[i]+y[i-1])/2
    #result = h * (np.sum(y) - 0.5 * (y[0] + y[-1]))

    return result

def y_function(x):
    return x + trapezoidal_rule_integration(lambda s: s * np.sin(x*s), 0, 1, 10)

# решение уравнения на заданном отрезке
x_values = np.linspace(0, 1, 11) # значения x
y_values = [y_function(x) for x in x_values] # соответствующие значения y

for x, y in zip(x_values, y_values):
    print(f"y({x}) = {y}")

plt.plot(x_values,y_values)
plt.show()

'''