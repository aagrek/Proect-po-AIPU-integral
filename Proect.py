import math
import random
import re
from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
def sin(x):
    if type(x) == type(sin):
        return math.sin(x)
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
    return math.tan(x)
def ctg(x):
    '''
    ----------
    x : float (Угол в радианах)
    
    Return : float (Косинус угла в радианах)
    -------
    '''
    return math.ctg(x)
def x(x):
    return

def step(x,a):
    return x ** a
def integ(f, a, b):
    v, err = integrate.quad(f, a, b)
    return v
def method_rectangles(f, a, b):
    ans=0
    n=10000
    shag=(b-a)/n
    for i in range (1,n+1):
        ans=ans + f(a+shag*(i-1) + (b-a)/2/n)
    return ans * shag
def method_trapecia(f, a, b):
    ans=(f(a)+f(b))/2
    n=10000
    shag=(b-a)/n
    for i in range(1,n):
        ans+=f(a+shag*i)
    return ans * shag
def method_Simson(f, a, b):
    ans2=f(a)+f(b)
    for i in range(1,10000):
        if i%2==1:
            ans2+=4*f(a+(b-a)*i/10000)
        else:
            ans2+=2*f(a+(b-a)*i/10000)
    return ans2*(b-a)/3/10000
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
    for i in range(math.floor(a), math.ceil(b)):
        s += [f(i)]
    for i in range(((math.ceil(b) - math.floor(a)) * math.ceil(max(s)))**3):
        x = random.uniform(math.floor(a), math.ceil(b))
        y = random.uniform(0, math.ceil(max(s)))
        m1 += 1
        if f(x) >= y:
            n1 += 1
    for i in range(((math.ceil(b) - math.floor(a)) * abs(math.floor(min(s))))**3):
        x = random.uniform(math.floor(a), math.ceil(b))
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
def clever_grafik(f,method):
    t = []
    y1 = []
    t = np.arange(1, 101, 0.1)
    for i in range(0, 1000):
        y1.append(method(f, 0, t[i]) - integ(f, 0, t[i]))
    plt.title('График погрешностей')
    plt.plot(t, y1, 'r')
    plt.show()
st=('sin+cos-tg').split('+')
f=method_rectangles
a=-10
b=312
ans=0
for i in st:
    k=i.split('-')
    print(k)
    if len(k)==1:
        ans=ans + f(eval(i), a, b)
    else:
        for j in range(len(k)):
            if j == 0:
                ans= ans+ f(eval(k[j]),a,b)
            else:
                ans= ans - f(eval(k[j]),a,b)
print(ans)
print(f(sin,a,b)+f(cos,a,b)-f(tg,a,b))
