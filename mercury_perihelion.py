import numpy as np
from scipy.integrate import odeint
import matplotlib.pylab as plt


L = 9.11*10**38     #L = angular momentum
m = 3.28*10**23     #m = mass of mercury
M = 1.99*10**30     #M = mass of sun
G = 6.674*10**-11   #G = Gravitationl constant
c = 3*10**8
h = L/m   
j = 3*G**2*M**2
k = h**2*c**2

def fx(z,t):
    x , xdiv = z
    dzdt =[xdiv,(1 + j*x**2*300000/k) - x] #300000 #90000 #300000
    return dzdt

n = 100000
x0 = [2,0] #2 #2 #2.03
phi = np.linspace(0,84*np.pi,n) #84 #288 #84
y = odeint(fx,x0,phi)
r = 1/y[:,0]

x = np.zeros([n])
y = np.zeros([n])

for i in range(0,n):
    x[i] = r[i]*np.cos(phi[i])

for i in range(0,n):
    y[i] = r[i]*np.sin(phi[i])

print('r =',r)
print('x =',x)
print('y =',y)
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
