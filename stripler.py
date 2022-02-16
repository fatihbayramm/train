kardiz = " istihza "
print(kardiz)

print(kardiz.strip())

a = "FatihBayram"
print(a.strip("y"))#strip sadece baştaki ve sondaki karakterleri kırpabilir.
print("-" * 100)
metin = """
> Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından
> 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin Python
> olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını düşünür.
> Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından gelmez.
> Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz komedi
> grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır.
> Ancak her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
> bir yılan figürü ile temsil edilmesi neredeyse birgelenek halini almıştır diyebiliriz.
"""
for i in metin.split():
    print(i.strip("> ") , end=" ")

print("-"*100)
#lstrip sadece sol tarafta bulunan gereksiz karakterleri kırpar.
#rstrip ise sağdaki.
a = "kazak"
print(a.lstrip("k"))
b = "kaydırak"
print(b.rstrip("k"))


