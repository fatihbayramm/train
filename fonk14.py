#ascii() Bu fonksiyon, bir nesnenin ekrana basılabilir halini verir bize.
#Ayrıca bu fonksiyon, karakter dizileri içindeki Türkçe karakterlerin de UNICODE temsillerini döndürür.
a  = "istihza"
print(ascii(a))
b = "\n"
print(ascii(b))
print("burada tırnak yok ")

c = "ışık"#türkçe karakter var .
print(ascii(c))
for i in c:
    print(ascii(i))

liste = ['elma', 'armut', 'erik']
temsil = ascii(liste)
print(temsil)
    