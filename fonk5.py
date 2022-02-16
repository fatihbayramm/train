def kur(kurulum_dizini = "/usr/bin"):
    cikti = "Program {} dizinine kuruldu !"
    print(cikti.format(kurulum_dizini))
kur()   #varsayılan parametreye göre çıktı verir
kur("C://desktop") #bizim belirlediğimiz parametreye göre çıktı verir .
print("-"*60)

def kurulum(kurulum_dizini =""):
    if not kurulum_dizini:
        print("Lütfen programı hangi dizine kurmak istediğinizi belirtin !")
    else:
        print("Programınız {} dizinine başarıyla kuruldu !".format(kurulum_dizini))
kurulum("c://desktop")       