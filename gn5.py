uretec = (i for i in range(0,10))
print(type(uretec))


a = list(uretec)
print(a)

def uretec_fonk():
    for i in range(10):
        yield i

uretec2 = uretec_fonk()


uretec3 = (i for i in range(5))
for i in uretec3:
    print(i)


for i in uretec3:
    print(i)    #burada tekrar basılmıyor çünkü bu tip üreteçler tek kullanımlıktır.

print("-"*30)
uretec4 = (i for i in range(3))

print(next(uretec4))
print(next(uretec4))
print(next(uretec4))


print("-"*30)
def uretec_fonksiyonu():
    for i in range(3):
        yield i

uretec5 = uretec_fonksiyonu()
print(next(uretec5))
print(next(uretec5))
print(next(uretec5))
#bidahaki print de stopiteration vereceğinden bu üreteci başka bir değişkene atayarak tekrar kullanabiliriz.

print("-"*50)

uretec6 = uretec_fonksiyonu()
print(next(uretec6))
print(next(uretec6))
print(next(uretec6))

liste = uretec_fonksiyonu()
listem = list(liste)
print(listem)


