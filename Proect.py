import math
import random
from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
def sin(x):
    '''
    ----------
    x : float (Угол в радианах)

    Returns : float (Синус угла в радианах)
    -------
    '''
    return math.sin(x)
def cos(x):
    '''
    ----------
    x : float (Угол в радианах)
    
    Return : float (Косинус угла в радианах)
    -------
    '''
    return math.cos(x)
def tg(x):
    '''
    ----------
    x : float (Угол в радианах)
    
    Return : float (Тангенс угла в радианах)
    -------
    '''
    return math.tg(x)
def ctg(x):
    '''
    ----------
    x : float (Угол в радианах)
    
    Return : float (Косинус угла в радианах)
    -------
    '''
    return math.ctg(x)
def x(x):
    return x
def step2(x):
    return x ** 2
def step3(x):
    return x ** 3
def integ(f, a, b):
    v, err = integrate.quad(f, a, b)
    return v
def method_rectangles():
    return 0
def method_trapecia():
    return 0
def method_Sipmson(f, a, b):
    ans1=(b-a)/6*(f(a)+4*f((a+b)/2)+f(b))
    ans2=0
    for i in range(100000):
        if i%2==1:
            ans2+=4*f(a+(b-a)*i/2/100000)
        else:
            ans2+=2*f(a+(b-a)*i/2/100000)
    return ans2*(b-a)/6/100000,ans1
        
    return ans1
def method_Ghaus(f, a, b):
    Ai = [0.11846344, 0.23931433, 0.28444444, 0.23931433, 0.11846344]
    mxi = [0.04691008, 0.23076534, 0.5, 0.76923466, 0.95308992]
    bxi = []
    integ = 0
    for i in range(len(mxi)):
        bxi.append(a + (b - a) * mxi[i])
    for i in range(len(mxi)):
        integ += Ai[i] * f(bxi[i])
    return (b - a) * integ
def method_Monte_Karlo(f, a, b):
    s = []
    x = 0
    y = 0
    n1 = 0
    m1 = 0
    n2 = 0
    m2 = 0
    for i in range(a, b):
        s += [f(i)]
    for i in range(((b - a) * math.ceil(max(s)))**3):
        x = random.uniform(a, b)
        y = random.uniform(0, math.ceil(max(s)))
        m1 += 1
        if f(x) >= y:
            n1 += 1
    for i in range(((b - a) * abs(math.floor(min(s))))**3):
        x = random.uniform(a, b)
        y = random.uniform(math.floor(min(s)), 0)
        m2 += 1
        if f(x) <= y:
            n2 += 1
    if (m1 != 0) and (m2 != 0):
        itog = ((n1 / m1) * (b - a) * math.ceil(max(s))) + ((n2 / m2) * (b - a) * math.floor(min(s)))
    else:
        if m1 != 0:
            itog = ((n1 / m1) * (b - a) * math.ceil(max(s)))
        else:
            if m2 != 0:
                itog = ((n2 / m2) * (b - a) * math.floor(min(s)))
            else:
                itog = 0
    return itog
def grafik_Monte_Karlo(f):
    t = []
    y1 = []
    for i in range(1, 101):
        t.append(i)
    for i in range(0, 100):
        y1.append(method_Monte_Karlo(f, 0, t[i]) - integ(f, 0, t[i]))
    plt.title('График погрешностей')
    plt.axis([0, 110, -2, 2])
    plt.plot(t, y1, 'r')
    plt.show()
def grafik_Ghaus(f):
    t = []
    y1 = []
    for i in range(1, 101):
        t.append(i)
    for i in range(0, 100):
        y1.append(method_Ghaus(f, 0, t[i]) - integ(f, 0, t[i]))
    plt.title('График погрешностей')
    plt.plot(t, y1, 'r')
    plt.show()
