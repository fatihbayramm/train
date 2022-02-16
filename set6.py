kume = set()
kume.add((1 , 2 , 3))
kume.add("Fatih")
kume.add(45)
print(kume)
#Yukarıdakiler, değiştirilemeyen veri tipleri olduğu için kümelere eklenebilir.
#(tuple) , str , int
#kümelere ; küme , liste , sözlük ekleyemeyiz . Çünkü bunlar değiştirilebilir veri tipleridir.

print("-" * 60)

k1 = set([1, 2, 3, 5])
k2 = set([3, 4, 2, 10])
a = k1.difference(k2)#bu metot iki kümenin farkını almamızı sağlar .
print(a)
b = k2.difference(k1)
print(b)
c = k1 - k2
print(c)
#eksi ile de aynı işlevi gerçekleştirebiliriz .
d = k2 - k1
print(d)
