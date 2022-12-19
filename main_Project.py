from math import *
import random
from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
def ctg(x):
    """Возвращает котангенс угла x
       Вход: x- угол
    """
    return 1/tan(x)
def step(x,a):
    """Возвращает x в степени а
       Вход: x - возводимое число
             a - степень
    """
    return x ** a
def exp(a,x):
    """Возвращает а в степени x
           Вход: a - возводимое число
                 x - степень
        """
    return a**x
def loga(x,a):
    """Возвращает логарифм числа x по основанию а
               Вход: x - логарифмируемое число >0
                     а - основание логарифма   >0
            """
    return log(x,a)
def x(x):
    """Возвращает x
               Вход: x - число
            """
    return x
def integ(f, a, b):
    """Возвращает интеграл от функции f в границах от a до b
               Вход: a - нижняя граница  -> str
                     b - верхняя граница -> str
                     f - выражения для подсчёта интеграла -> str
               локальные переменные:
                     v - значнгие игтеграла
                     err - погрешность
            """
    v, err = integrate.quad(f, a, b)
    return v
def method_rectangles(f, a, b,*arg):
    """Подщет интеграла методом прямоугольников
            Вход: 
                a - нижняя граница  -> str
                b - верхняя граница -> str
                f - выражения для подсчёта интеграла -> str
            Локальные переменные:
                ans - сумма значений функции
                n - кол-во значений функций
                shag - на сколько изменяется переменная прикаждом измерении
            Выход: 
                ans * shag - площадь под функцией f
                     """
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
    """Подщет интеграла методом трапеций
            Вход: a - нижняя граница  -> float
                b - верхняя граница -> float
                f - выражения для подсчёта интеграла -> str
            Локальные переменные:
                result - сумма значений функции
                n - кол-во значений функций
                shag - на сколько изменяется переменная прикаждом измерении
            Выход: 
                result * shag - площадь под функцией f
                         """
    result=0
    if str(f)[10:14]=='step':
        result+= (f(a,arg[0])+f(b,arg[0]))/2
    elif str(f)[10:14]=='loga':
        result+= (f(a,arg[0])+f(b,arg[0]))/2
    elif str(f)[10:13]=='exp':
        result+=(f(arg[0],a)+f(arg[0],b))/2
    else:
        result=(f(a)+f(b))/2
    n=10000
    shag=(b-a)/n
    for i in range(1,n):
        if str(f)[10:14]=='step':
            result=result + f(a+shag*i,arg[0])
        elif str(f)[10:14]=='loga':
            result=result + f(a+shag*i,arg[0])
        elif str(f)[10:13]=='exp':
            result=result + f(arg[0],a+shag*i)
        else:
            result+=f(a+shag*i)
    return result * shag
def method_Simson(f, a, b,*arg):
    """Подщет интеграла методом Симпсона
            Вход: a - нижняя граница  -> float
                b - верхняя граница -> float
                f - выражения для подсчёта интеграла -> str
            Локальные переменные:
                ans2 - сумма значений функции изменяемых таким образом, чтобы получилась приблизительная форма пораболы
            Выход: 
                ans2*(b-a)/3/10000 - площадь под функцией f в приближенни параболы
                             """
    if str(f)[10:14]=='step':
        ans2=f(a,arg[0])+f(b,arg[0])
    elif str(f)[10:14]=='loga':
        ans2=f(a,arg[0])+f(b,arg[0])
    elif str(f)[10:13]=='exp':
        ans2=f(arg[0],a)+f(arg[0],b)
    else:
        ans2=f(a)+f(b)
    
    if str(f)[10:14]=='step':
        for i in range(1,10000):
            if i%2==1:
                ans2+=4*f(a+(b-a)*i/10000,arg[0])
            else:
                ans2+=2*f(a+(b-a)*i/10000,arg[0])
    elif str(f)[10:14]=='loga':
        for i in range(1,10000):
            if i%2==1:
                ans2+=4*f(a+(b-a)*i/10000,arg[0])
            else:
                ans2+=2*f(a+(b-a)*i/10000,arg[0])
    elif str(f)[10:13]=='exp':
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
    """Подщет интеграла методом Симпсона
            Вход: a - нижняя граница  -> float
                b - верхняя граница -> float
                f - выражения для подсчёта интеграла -> str
            Локальные переменные:
                Ai - список специальных точек специально распределенных для уточненного вычисления
                mxi - список точек полученных преобразованием точек из списка Ai, от которых будет браться функция
                integ - сумма вычисляющаяся по специальной формуле
            Выход: (b - a) * integ - площадь под функцией f вычисленная по квадратурной формуле -> float
                                 """
    Ai = [0.11846344, 0.23931433, 0.28444444, 0.23931433, 0.11846344]
    mxi = [0.04691008, 0.23076534, 0.5, 0.76923466, 0.95308992]
    bxi = []
    integ = 0
    for i in range(len(mxi)):
        bxi.append(a + (b - a) * mxi[i])
    for i in range(len(mxi)):
        if str(f)[10:14] == 'step':
            integ += Ai[i] * f(bxi[i], arg[0])
        elif str(f)[10:14] == 'loga':
            integ += Ai[i] * f(bxi[i], arg[0])
        elif str(f)[10:13] == 'exp':
            integ += Ai[i] * f(arg[0], bxi[i])
        else:
            integ += Ai[i] * f(bxi[i])
    return (b - a) * integ
def method_Monte_Karlo(f, a, b, *arg):
    """Подщет интеграла методом Монте-Карло
            Вход: a - нижняя граница  -> float
               b - верхняя граница -> float
               f - выражения для подсчёта интеграла -> str
            Локальные переменные:
                s - список значениий функции f в отрезке от a до b c шагом в один
                x - случайное чилсло по оси x (от a до b)
                y - случайное чилсло по оси y (от минимального и максимального значения функции на отрезке от a до b
                m1 - кол-во точек где значение функции больше нуля
                n1 - кол-во точекm, которые попадают под график, где функция положительна
                m2 - кол-во точек где значение функции меньше нуля
                n2 - кол-во точекm, которые попадают под график, где функция отрицательна
                itog - приблизительная площадь функции f на отрезке от a до b
            Выход: 
                itog - площадь под функцией f вычислення методом Монте-Карло -> float
                                     """
    s = []
    x = 0
    y = 0
    n1 = 0
    m1 = 0
    n2 = 0
    m2 = 0
    for i in range(floor(a), ceil(b)):
        if str(f)[10:14] == 'step':
            s += [f(i, arg[0])]
        elif str(f)[10:14] == 'loga':
            s += [f(i, arg[0])]
        elif str(f)[10:13] == 'exp':
            s += [f(arg[0], i)]
        else:
            s += [f(i)]
    for i in range(((ceil(b) - floor(a)) * ceil(max(s,default=0)))):
        x = random.uniform(floor(a), ceil(b))
        y = random.uniform(0, ceil(max(s,default=0)))
        m1 += 1
        if str(f)[10:14] == 'step':
            if f(x, arg[0]) >= y:
                n1 += 1
        elif str(f)[10:14] == 'loga':
            if f(x, arg[0]) >= y:
                n1 += 1
        elif str(f)[10:13] == 'exp':
            if f(arg[0], x) >= y:
                n1 += 1
        else:
            if f(x) >= y:
                n1 += 1
    for i in range(((ceil(b) - floor(a)) * abs(floor(min(s,default=0))))):
        x = random.uniform(floor(a), ceil(b))
        y = random.uniform(floor(min(s,default=0)), 0)
        m2 += 1
        if str(f)[10:14] == 'step':
            if f(x, arg[0]) <= y:
                n2 += 1
        elif str(f)[10:14] == 'loga':
            if f(x, arg[0]) <= y:
                n2 += 1
        elif str(f)[10:13] == 'exp':
            if f(arg[0], x) <= y:
                n2 += 1
        else:
            if f(x) <= y:
                n2 += 1
    if (m1 != 0) and (m2 != 0):
        itog = ((n1 / m1) * (b - a) * ceil(max(s,default=0))) + ((n2 / m2) * (b - a) * floor(min(s,default=0)))
    else:
        if m1 != 0:
            itog = ((n1 / m1) * (b - a) * ceil(max(s,default=0)))
        else:
            if m2 != 0:
                itog = ((n2 / m2) * (b - a) * floor(min(s,default=0)))
            else:
                itog = 0
    return itog
def grafik(f,method):
    """Построение графиков погрешностей для разных методов
            Вход: method - метод для которого будет выведен график погрешностей
                f - выражение, для которого считается интеграл (Принимает только функции: x, log2, log, log10, sin, cos, tan, ctg)
            Локальные переменные:
                t - массив чисел от 1 до 100 с шагом 0.1
                y - список разниц между методом от которого вызван график и функцией вычисления интеграла из питона
                         """
    t = []
    y1 = []
    t = np.arange(1, 101, 0.1)

    for i in range(0, 1000):
        y1.append(abs(podshet(f, 1,t[i], method) - podshet(f,1 ,t[i], integ)))
    plt.title('График погрешностей ' +str(f)+' ' + str(method)[10:str(method).find('at')])
    plt.plot(t, y1, 'r')
    plt.show()
def podshet(st,a,b,f):
    '''Разбивает выражение st с помощью метода split сначала по "+"
    затем по "-", считает интеграл от каждой функкции и считает в
    итоговую переменную ans с соответствующим знаком
             Вход: st - выражения для подсчёта интегралов -> str
                a  - нижняя граница интеграла  -> float
                b  - верхняя граница интеграла -> float
                f  - метод, с помощью которого считается интеграл -> function
            Локальные переменные:
                k - разбиение выражения st по минусам
            Выход:
                ans - итоговое значение интеграла
                         """
    '''
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
