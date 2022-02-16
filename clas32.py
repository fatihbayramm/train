import clas31

asker1 = clas31.Asker("Fatih" , "Er")
print(asker1.isim)
print(asker1.rutbe)
print(asker1.guc)
print(asker1.puan_kazan())
print(asker1.puan_kaybet())
print(asker1.memleket)

print("-"*30)

isci1 = clas31.İsci("İsmail" , "Usta")
print(isci1.isim , isci1.rutbe , sep=" --> ")

yonetici1 = clas31.Yonetici("Enes" , "Yönetici")
print(yonetici1.isim , yonetici1.rutbe , sep=" --> ")
yonetici1.puan_kaybet()
asker1.hareket_et()