import numpy as np
import matplotlib.pyplot as plt
def f(t, y):
    y1, y2, y3 = y
    return [y2, y3, 6*y2**2 + 9*y1]

def runge_kutta4(t0, y0, h, x0,xn):
    t = np.zeros((int((xn-x0)/h)))
    t[0]=t0
    y=np.zeros((int((xn-x0)/h),3))
    y[0,:]=y0

    for x in range(1,int((xn-x0)/h)):
        k1 = np.array(f(t[x-1], y[x-1,:]))
        k2 = np.array(f(t[x-1] + h/2, y[x-1,:] + 1/2 * k1))
        k3 = np.array(f(t[x-1] + h/2, y[x-1,:] + 1/2 * k2))
        k4 = np.array(f(t[x-1] + h, y[x-1,:] + k3))

        y[x][:] = y[x-1,:] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        t[x] = t[x-1] + h

    return t, y

t0 = 0
y0 = [1, 0, 2]
h = 0.01
x0=0
xn=0.7

t, y = runge_kutta4(t0, y0, h, x0,xn)
x=np.linspace(x0,xn,int((xn-x0)/h))
f1, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(t, y[:,0])
ax1.set_title('y(t)')
ax2.scatter(t, y[:,1])
ax2.set_title("y'(t)")
'''ax3.plot(t,y[:,2])
ax3.set_title('y"(t)')'''

plt.show()
print(f"t = {t}")
print(f"y(t) = {y[:,0]}")
print(f"dy/dt(t) = {y[:,1]}")
print(f"d^2y/dt^2(t) = {y[:,2]}")