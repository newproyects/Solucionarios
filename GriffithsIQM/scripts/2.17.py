import numpy as np
from numpy import pi,cos,exp
import matplotlib.pyplot as plt

w=1
m=1
h=1054571817e-34
h=1

def p0(x):
    return exp(-(x**2)*m*w/(2*h))*(m*w/(pi*h))**(1/4)

def p1(x):
    return exp(-(x**2)*m*w/(2*h))*((m*w/(pi*h))**(1/4))*(2*m*w/h)**(1/2)

def P(x,t):
    return 0.5*(p0(x)**2+p1(x)**2)+p0(x)*p1(x)*cos(w*t)

x=np.linspace(-2,2)

t=np.linspace(0,5,6)

for i in t:
    plt.plot(x,P(x,i*pi/w),label=f"{i}pi/w")

plt.legend()
plt.show()
