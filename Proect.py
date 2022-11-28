import math
def method_rectangles():
    return 0
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
def method_trapecia():
    return 0
def method_Sipmson(f,a,b):
    ans1=(b-a)/6*(f(a)+4*f((a+b)/2)+f(b))
    ans2=f(a+(b-a)/2/100)+f(a+(b-a))
    c1=1
    for i in range(a*100+(b-1),b*100-(b-a),(b-a)):
        if c1%2==1:
            ans2+=2*f(a+(b-a)*c1/2/100)
        else:
            ans2+=4*f(a+(b-a)*c1/2/100)
        c1+=1
    return ans2*(b-a)/6/100,ans1
        
    return ans1
def method_Ghaus():
    return  0
def method_Monte_Karlo():
    return 0
print(method_Sipmson(cos,-9,5))