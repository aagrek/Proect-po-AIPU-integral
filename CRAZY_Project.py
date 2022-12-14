from math import sin,cos,tan,log
import random
import re
import math
from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
def ctg(x):
    return 1/tan(x)
def step(x,a):
    return x ** a
def exp(a,x):
    return a**x
def loga(x,a):
    return log(x,a)

def integ(f, a, b):
    v, err = integrate.quad(f, a, b)
    return v
def method_rectangles(f, a, b,*arg):
    ans=0
    n=10000
    shag=(b-a)/n
    for i in range (1,n+1):
        if str(f)[10:14]=='step':
            ans=ans + f((a+shag*(i-1) + (b-a)/2/n),arg[0])
        elif str(f)[10:14]=='loga':
            ans=ans + f((a+shag*(i-1) + (b-a)/2/n),arg[0])
        elif str(f)[10:13]=='exp':
            ans=ans + f(arg[0],a+shag*(i-1) + (b-a)/2/n)
        else:
            ans=ans + f(a+shag*(i-1) + (b-a)/2/n)
    return ans * shag
def method_trapecia(f, a, b,*arg):
    result=0
    if str(f)=='step':
        result+= (f(a,arg[0])+f(b,arg[0]))/2
    if str(f)=='loga':
        result+= (f(a,arg[0])+f(b,arg[0]))/2
    elif str(f)=='exp':
        result+=(f(arg[0],a)+f(arg[0],b))/2
    else:
        result=(f(a)+f(b))/2
    n=10000
    shag=(b-a)/n
    for i in range(1,n):
        if str(f)=='step':
            result=result + f(a+shag*i,arg[0])
        elif str(f)=='loga':
            result=result + f(a+shag*i,arg[0])
        elif str(f)=='exp':
            result=result + f(arg[0],a+shag*i)
        result+=f(a+shag*i)
    return result * shag
def method_Simson(f, a, b,*arg):
    if arg=='step':
        ans2=f(a,arg[0])+f(b,arg[0])
    elif arg=='loga':
        ans2=f(a,arg[0])+f(b,arg[0])
    elif str(f)=='exp':
        ans2=f(arg[0],a)+f(arg[0],b)
    else:
        ans2=f(a)+f(b)
    
    if str(f)=='step':
        for i in range(1,10000):
            if i%2==1:
                ans2+=4*f(a+(b-a)*i/10000,arg[0])
            else:
                ans2+=2*f(a+(b-a)*i/10000,arg[0])
    elif str(f)=='loga':
        for i in range(1,10000):
            if i%2==1:
                ans2+=4*f(a+(b-a)*i/10000,arg[0])
            else:
                ans2+=2*f(a+(b-a)*i/10000,arg[0])
    elif str(f)=='exp':
        for i in range(1,10000):
            if i%2==1:
                ans2+=4*f(arg[0],a+(b-a)*i/10000)
            else:
                ans2+=2*f(arg[0],a+(b-a)*i/10000)
    else:
        for i in range(1,10000):
            if i%2==1:
                ans2+=4*f(a+(b-a)*i/10000)
            else:
                ans2+=2*f(a+(b-a)*i/10000)
    return ans2*(b-a)/3/10000
def method_Ghaus(f, a, b, *arg):
    Ai = [0.11846344, 0.23931433, 0.28444444, 0.23931433, 0.11846344]
    mxi = [0.04691008, 0.23076534, 0.5, 0.76923466, 0.95308992]
    bxi = []
    integ = 0
    for i in range(len(mxi)):
        bxi.append(a + (b - a) * mxi[i])
    for i in range(len(mxi)):
        if str(f) == 'step':
            integ += Ai[i] * f(bxi[i], arg[0])
        elif str(f) == 'loga':
            integ += Ai[i] * f(bxi[i], arg[0])
        elif str(f) == 'exp':
            integ += Ai[i] * f(arg[0], bxi[i])
        else:
            integ += Ai[i] * f(bxi[i])
    return (b - a) * integ
def method_Monte_Karlo(f, a, b, *arg):
    s = []
    x = 0
    y = 0
    n1 = 0
    m1 = 0
    n2 = 0
    m2 = 0
    for i in range(math.floor(a), math.ceil(b)):
        s += [f(i)]
    for i in range(((math.ceil(b) - math.floor(a)) * math.ceil(max(s))) ** 3):
        x = random.uniform(math.floor(a), math.ceil(b))
        y = random.uniform(0, math.ceil(max(s)))
        m1 += 1
        if str(f) == 'step':
            if f(x, arg[0]) >= y:
                n1 += 1
        elif str(f) == 'loga':
            if f(x, arg[0]) >= y:
                n1 += 1
        elif str(f) == 'exp':
            if f(arg[0], x) >= y:
                n1 += 1
        else:
            if f(x) >= y:
                n1 += 1
    for i in range(((math.ceil(b) - math.floor(a)) * abs(math.floor(min(s)))) ** 3):
        x = random.uniform(math.floor(a), math.ceil(b))
        y = random.uniform(math.floor(min(s)), 0)
        m2 += 1
        if str(f) == 'step':
            if f(x, arg[0]) <= y:
                n2 += 1
        elif str(f) == 'loga':
            if f(x, arg[0]) <= y:
                n2 += 1
        elif str(f) == 'exp':
            if f(arg[0], x) <= y:
                n2 += 1
        else:
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
    plt.title('График погрешностей' )
    plt.plot(t, y1, 'r')
    plt.show()
    
stroka='sin-step5+exp0.5+loga5'
fun=method_rectangles
a=10
b=20
def podshet(st,a,b,f):
    st=st.split('+')
    ans=0   
    for i in st:
        k=i.split('-')
        if len(k)==1:
            if k[0][:4]=='step':
                ans+=f(step,  a,b,float(k[0][4:]))
            elif k[0][:3]=='exp':
                ans+=f(exp,a,b,float(k[0][3:]))
            elif k[0][:4]=='loga':
                ans+=f(loga,  a,b,float(k[0][4:]))
            else:ans=ans + f(eval(i), a, b)
        else:
            for j in range(len(k)):
                if j == 0:
                    if k[j][:4]=='step':
                        ans=ans+f(step,  a,b,float(k[j][4:]))
                    elif k[j][:4]=='loga':
                        ans=ans+f(loga,  a,b,float(k[j][4:]))
                    elif k[j][:3]=='exp':
                        ans+=f(exp,a,b,float(k[j][3:]))
                    else:
                        ans= ans + f(eval(k[j]),a,b)
                else:
                    if k[j][:4]=='step':
                        ans-=f(step,  a,b,float(k[j][4:]))
                    elif k[j][:4]=='loga':
                        ans-=f(loga,  a,b,float(k[j][4:]))
                    elif k[j][:3]=='exp':
                        ans-=f(exp,a,b,float(k[j][3:]))
                    else:
                        ans-= f(eval(k[j]),a,b)
    return ans
print(podshet(stroka,a,b,fun))
