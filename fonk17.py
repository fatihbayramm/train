s = dict(a=1 , b=2 , c=3)
print(s)

#callable() Bu fonksiyon, bir nesnenin ‘çağrılabilir’ olup olmadığını denetler.
#Mesela fonksiyonlar çağrılabilir nesnelerdir. Değişkenler ise çağrılabilir nesneler değildir.

a = callable(open)
print(a)
b = callable(print)
print(b)

import sys
c = callable(sys.version)#sys modülü içindeki version adlı araç bir fonksiyon değil, değişkendir.
print(c)                 #bu yüzden false geliyor .
print("-"*30)
#ord()Bu fonksiyon, bir karakterin karşılık geldiği ondalık sayıyı verir.
print(ord("a"))
#oct() Bu fonksiyon, bir sayıyı sekizli düzendeki karşılığına çevirmemizi sağlar:
print(oct(2))
#Bu fonksiyon, bir sayıyı onaltılı düzendeki karşılığına çevirmemizi sağlar:
print(hex(305))
#Yalnız hem oct() hem de hex() fonksiyonlarında dikkat etmemiz gereken şey,
#bu fonksiyonların parametre olarak bir sayı alıp, çıktı olarak bir karakter dizisi veriyor olmasıdır.