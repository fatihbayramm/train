#repr() fonksiyonu ise ASCII olmayan karakterlerle karşılaşsa bile,
#bize çıktı olarak bunların da karakter karşılıklarını gösterir:
print(repr("şeker"))

#bin() Bu fonksiyon, bir sayının ikili düzendeki karşılığını verir:
print(bin(1))

#bytes() fonksiyon bytes türünde nesneler oluşturmak için kullanılır.
print(bytes(10))
a = bytes(12)
print(a)
print(a[0])
print(a[1])
c = bytes("ışık" , encoding = "utf-8")
print(c)
d = bytes("ışık" , "cp1254")
print(d)
e = bytes("ışık" , "cp857")
print(e)
print("-"*30)
f = bytes('ışık', encoding='ascii', errors='replace')#ş ve ı ascii de tanımlı değildir bu yüzden hata verir biz de errors
#adlı parametreyle hata yerine tanımsız olan karakterler yerine ? basıyoruz .
print(f)

g = bytes('€', encoding='cp857', errors='ignore')
print(g)
