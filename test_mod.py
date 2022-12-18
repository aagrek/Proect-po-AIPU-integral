from main_Project import *
import unittest
global e 
e=0.001

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
class TestMonteKarlo(unittest.TestCase):
    def test_1(self):
        a=podshet('loga4',2,9,method_Monte_Karlo)
        b=8.2152298
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
        a=podshet('sin',1,63,method_Monte_Karlo)
        b=0.83244
        assert (min(a,b)/max(a,b)*100>90 or abs(a-b)<e)==1
  
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

if __name__ ==  '__main__':
    unittest.main()
    
 
