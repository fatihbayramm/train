class Calısan:
    kabiliyet = []
    unvan = "işçi"
    maas = 1500
    memleket = ""
    dogum_tarihi = ""

ahmet = Calısan()
mehmet = Calısan()
ayse = Calısan()
selim = Calısan()

print(ahmet.kabiliyet)
print(ahmet.unvan)

print(mehmet.maas)
print(mehmet.memleket)

print(ayse.kabiliyet)
print(ayse.dogum_tarihi)

print("-"*60)

ahmet.kabiliyet.append("prezentabl")
print(ahmet.kabiliyet)

print(selim.kabiliyet)#burada selime prezentabl değerini eklemediğimiz halde selimin kabiliyetleri arasın gözüküyor
                      #Bunun nedeni listelerin değiştirilebilir veri tipi olmasındandır. Birini değiştirdiğimiz için
                      #Diğeri de değişti .
#Peki o halde biz değerinin her örnekte ortak değil de her örneğe özgü olmasını istediğimiz
#nitelikleri nasıl tanımlayacağız? Elbette sınıf nitelikleri yerine örnek nitelikleri denen
#başka bir kavramdan yararlanarak…                      