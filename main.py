from abc import ABC, abstractmethod

class Empty(Exception):
    pass

class PriorityVal(ABC):

    class _Item:
        def __init__(self, key, value):
            self.key, self.value = key, value

        def __lt__(self, other):
            return self.key < other.key

        def __repr__(self):
            return str((self.key, self.value))

    @abstractmethod
    def add(self, key, value):
        '''pridá dvojicu (key, value)'''
        pass

    @abstractmethod
    def max(self):
        '''vráti dvojicu (key, value) s najmenším kľúčom'''
        pass
    
    @abstractmethod
    def min(self):
        '''vráti dvojicu (key, value) s najmenším kľúčom'''
        pass

    @abstractmethod
    def remove_min(self):
        '''vráti a odstráni dvojicu (key, value) s najmenším kľúčom'''
        pass

    
class Test(PriorityVal):
    def __init__(self):
        self._data= []
    def add(self, key, value):
        self._data.append(self._Item(key,  value))
    def max(self):
        index = self.najdi_max()
        item = self._data[index]
        return item.key, item.value
    def najdi_max(self):
        index = 0
        for i in range (1,len(self._data)):
            if self._data[index]<self._data[i]:
                index= i
        return index
    def _find_min(self):
        index = 0
        for i in range(1, len(self._data)):
            if self._data[i] < self._data[index]:
                index = i
        return index
    def min(self):
        '''vráti dvojicu (key, value) s najmenším kľúčom'''
        index = self._find_min()
        item = self._data[index]
        return item.key, item.value

#    def remove_min(self):
#        index = self._find_min()
#        while index == 0:
#            item = self._data.pop(index)
#        return item.key, item.value

    
#    def zoradit(self):
#       if len(self._data) == 1:
#           print (self._data)
#       elif len (self._data) ==2:
#           zorad()
#           print (self._data)
#       elif len(self._data) ==3:
#           print (self._data)
#       else:
#           print ("zle")



test = str(input("nazov testu"))
test = Test()

dzadane= int(input("zadaj d"))
if dzadane<=0:
    dh= 0
elif 0<dzadane<=4:
    dh=60
elif 4<dzadane<=7:
    dh=70
elif 7<dzadane<=12:
    dh=80
elif 12<dzadane<=15:
    dh=90
else :
    dh=100
test.add(dh,"d")

izadane= int(input("zadaj i"))
if izadane<=-1:
    ih= 0
elif -1<izadane<=1:
    ih=60
elif 1<izadane<=3:
    ih=70
elif izadane ==4:
    ih= 75
elif 4<izadane<=6:
    ih=80
elif izadane ==7:
    ih= 85
elif 7<izadane<=9:
    ih=90
else :
    dh=100
test.add(ih,"i")


szadane= int(input("zadaj s"))
if szadane<=-2:
    sh= 0
elif -2<szadane<=0:
    sh=60
elif 0<szadane<=3:
    sh=70
elif 4<szadane<=7:
    sh=80
elif szadane ==8:
    sh= 85
elif 8<szadane<=10:
    sh=90
else :
    sh=100
test.add(sh,"s")


kzadane= int(input("zadaj k"))
if kzadane<=-3:
    kh= 0
elif -3<kzadane<=1:
    kh=60
elif -1<kzadane<=1:
    kh=70
elif 1<kzadane<=4:
    kh=80
elif 4<kzadane<=7:
    kh=90
else :
    kh=100
test.add(kh,"k")

nzadane= int(input("zadaj n"))
nh= 0
test.add(nh,"n")


print (dzadane,izadane,szadane,kzadane,nzadane,)
print ("test", test._data)
print('max=', test.max())
#print('vymaz=', test.remove_min(), "ukaz",test._data)
