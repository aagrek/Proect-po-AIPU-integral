from CRAZY_Project import *
import unittest
global e 
e=0.001
class ExpFunction(unittest.TestCase):
    def test_1(self):
        assert(exp(4,2) == 16)
    def test_2(self):
        assert(exp(25,16) == 23283064365386962890625)
    def test_3(self):
        assert(exp(-2,8) == 256)
    def test_4(self):
        assert(exp(0.25,2) == 0.0625)
    def test_5(self):
        assert(exp(0,15) == 0)
    def test_6(self):
        assert(exp(25,-1) == 0.04)
    def test_7(self):
        assert(exp(-10,-10) == 0.0000000001)
class LogharifmFunction(unittest.TestCase):
    def test_1(self):
        assert(loga(4,2) == 2)
    def test_2(self):
        assert(loga(16,4) == 2)
    def test_3(self):
        assert(loga(25,5) == 2)
    def test_4(self):
        assert(loga(1,2) == 0)
    def test_5(self):
        assert((loga(52.25,9.3) - 1.7739 )< e)
    def test_6(self):
        assert(loga(2,4) == 0.5)   
    def test_7(self):
        assert(loga(5,625) == 0.25) 
    def test_8(self):
        assert((loga(12.5,325.15) -0.43665)<e)
    def test_8(self):
        assert((loga(32,0.5) == -5)) 
    def test_8(self):
        assert((loga(256,0.25) ==-4))     
class StepFunction(unittest.TestCase):
    def test_1(self):
        assert(step(2,4) == 16)
    def test_2(self):
        assert(step(25,16) == 23283064365386962890625)
    def test_3(self):
        assert(step(-2,8) == 256)
    def test_4(self):
        assert(step(0.25,2) == 0.0625)
    def test_5(self):
        assert(step(0,15) == 0)
    def test_6(self):
        assert(step(25,-1) == 0.04)
    def test_7(self):
        assert(step(-10,-10) == 0.0000000001)
class Cotangens(unittest.TestCase):
    def test_1(self):
        assert((ctg(2) - (-0.457))<e)
    def test_2(self):
        assert((ctg(1) - (0.642))<e)
    def test_3(self):
        assert((ctg(15.2) - (-1.796))<e)
    def test_4(self):
        assert((ctg(-30) - (0.156))<e)  
class TestGhaus(unittest.TestCase):
    def test_1(self):
        a=podshet('loga4',2,9,method_Ghaus )
        b=8.2152298
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e) ==1
    def test_2(self):
        a=podshet('cos',1,2,method_Ghaus )
        b=0.067826
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e)==1
    def test_3(self):
        a=podshet('sin+cos-loga12+exp0.25',1,10,method_Ghaus )
        b=-5.4702
        assert (min(a,b)/max(a,b)*100 > 96) or (abs(a-b) < e)==1
    def test_4(self):
        a=podshet('loga2+exp5-tan',1,12,method_Ghaus)
        b=151693123.746
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e)==1
    def test_5(self):
        a=podshet('x - log2',0.5,13.25,method_Ghaus)
        b=56.1556
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e)==1
class TestRectangles(unittest.TestCase):
     
    def test_1(self):
        a=podshet('loga4',2,9,method_rectangles)
        b=8.2152298
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e)==1
    def test_2(self):
        a=podshet('cos',1,2,method_rectangles )
        b=0.067826
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e) ==1
    def test_3(self):
        a=podshet('sin+cos-loga12+exp0.25',1,10,method_rectangles )
        b=-5.4702
        assert (min(a,b)/max(a,b)*100 > 96) or (abs(a-b) < e) ==1
    def test_4(self):
        a=podshet('loga2+exp5-tan',1,12,method_rectangles )
        b=151693123.746
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e) ==1
    def test_5(self):
        a=podshet('x - log2',0.5,13.25,method_rectangles)
        b=56.1556
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e)==1    
class TestMonteKarlo(unittest.TestCase):
    def test_1(self):
        a=podshet('loga4',2,7,method_Monte_Karlo)
        b=5.2190
        assert (min(a,b)/max(a,b)*100 > 83 or abs(a-b)<e*100) ==1
    def test_2(self):
        a=podshet('cos',1,2,method_Monte_Karlo )
        b=0.067826
        assert (min(a,b)/max(a,b)*100 > 83 or abs(a-b)<e*100) ==1
    def test_3(self):
        a=podshet('sin+cos-loga12+exp0.25',1,10,method_Monte_Karlo )
        b=-5.4702
        assert (min(a,b)/max(a,b)*100 > 83) or (abs(a-b) < e*100) ==1
    def test_4(self):
        a=podshet('loga2+x-tan',1,12,method_Monte_Karlo )
        b=99.0957
        assert (min(a,b)/max(a,b)*100 > 83 or abs(a-b)<e*100 )== 1
    def test_5(self):
        a=podshet('exp2',-5,5,method_Monte_Karlo)
        b=46.1211
        assert (min(a,b)/max(a,b)*100>83 or abs(a-b)<e*100)==1
    def test_6(self):
        a=podshet('x - log2',1.5,6.25,method_Monte_Karlo)
        b=9.6123
        assert (min(a,b)/max(a,b)*100 > 83 or abs(a-b)<e*100)==1    
class TestSimson(unittest.TestCase):
   
    def test_1(self):
        a=podshet('loga4',2,9,method_Simson)
        b=8.2152298
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e) == 1
    def test_2(self):
        a=podshet('cos',1,2,method_Simson )
        b=0.067826
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e) == 1
    def test_3(self):
        a=podshet('sin+cos-loga12+exp0.25',1,10,method_Simson )
        b=-5.4702
        assert (min(a,b)/max(a,b)*100 > 96) or (abs(a-b) < e) ==1
    def test_4(self):
        a=podshet('loga2+exp5-tan',1,12,method_Simson )
        b=151693123.746
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e) == 1
    def test_5(self):
        a=podshet('x - log2',0.5,13.25,method_Simson)
        b=56.1556
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e)==1  
class TestTrapecia(unittest.TestCase):
      
    def test_1(self):
        a=podshet('loga4',2,9,method_trapecia) 
        b=8.2152298
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e) ==1
    def test_2(self):
        a=podshet('cos',1,2,method_trapecia )
        b=0.067826
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e) ==1
    def test_3(self):
        a=podshet('sin+cos-loga12+exp0.25',1,10,method_trapecia )
        b=-5.4702
        assert (min(a,b)/max(a,b)*100 > 96) or (abs(a-b) < e) ==1
    def test_4(self):
        a=podshet('loga2+exp5-tan',1,12,method_trapecia )
        b=151693123.746
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e)  ==1
    def test_5(self):
        a=podshet('x - log2',0.5,13.25,method_trapecia)
        b=56.1556
        assert (min(a,b)/max(a,b)*100 > 96 or abs(a-b)<e)==1    
if __name__ ==  '__main__':
    unittest.main()
    
 
