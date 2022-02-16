__all__ = ["fonk1" , "fonk2" , "fonk3"]#__all__ listesini kullanarak nelerin içe aktarılabileceğini belirleriz.
                                       # ama bu durum yıldızlı içe aktarmalarda geçerlidir(sonraki sayfa) 
def fonk1():
    print('fonk1')

def fonk2():
    print('fonk2')

def fonk3():
    print('fonk3')

def fonk4():
    print('fonk4')

def fonk5():
    print('fonk5')

def _fonk6():
    print('_fonk6')

def __fonk7():
    print('__fonk7')

def fonk8_():
    print('fonk8_')

import modul11
print(dir(modul11))    

modul11.fonk1()
modul11.fonk2()
modul11.fonk3()

print("-"*90)
from modul11 import*

print(dir(modul11))