import clas11

c1 = clas11.Calisan("Ahmet")
c2 = clas11.Calisan("Mehmet")

print(c1.isim)
print(c2.isim)

c1.isim = "Mahmut"
c1.personel[0] = "Mahmut"

print(c1.isim)
print(c1.personel)

c1.kabiliyet_ekle("prezantabl")
c1.kabiliyet_ekle("konuşkan")

c2.kabiliyet_ekle("girişken")


print(c1.kabiliyetleri_goruntule())
print(c2.kabiliyetleri_goruntule())