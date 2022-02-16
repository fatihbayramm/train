def yazici():
    def yaz(mesaj):
        print(mesaj)
    return yaz

y = yazici()
y("Merhaba")

print("-"*60)

def kapsayici_fonk():
    non_local_degisken = 1
    def ic_fonk():
        non_local_degisken = 2
        print(non_local_degisken)
    return ic_fonk

donus_fonk = kapsayici_fonk()
donus_fonk()

a = 1
def func():
    global a
    a += 1
    print(a)
func()    
print(a)
