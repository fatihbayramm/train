isim = "fatih"
soyad = "bayram"
print("Benim adım %s , soyadım %s"%(isim , soyad))

kardiz = "istihza"
for sira , karakter in enumerate(kardiz , 1):
    print("%s. karakter : '%s' " %(sira , karakter))

print("Karakter dizilerinin toplam %s metodu vardır ."%len(dir("")))    

for i in dir(str):
    print("%15s" %i)
