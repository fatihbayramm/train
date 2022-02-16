def kapsayici_fonk():
    non_local_degisken = 1

    def ic_fonk():
        nonlocal non_local_degisken#nonlocal ile kapsayici_fonkdaki non_local_degiskeni nin değerini değiştirdik.
        non_local_degisken += 1
        print(non_local_degisken)

    return ic_fonk

donus_fonk = kapsayici_fonk()
donus_fonk()       


def kapsayici_fonk():
    non_local_degisken = 1

    def ic_fonk():
        print(non_local_degisken)#değiştirmek istemezsek direkt böyle yazabilirdik .

    return ic_fonk   

a = kapsayici_fonk()
a()     

def yazici(mesaj):
    def yaz():
        nonlocal mesaj
        mesaj += " Dünya !"
        print(mesaj)
    return yaz

b = yazici("Merhaba")
b()
#Sonuç olarak kapsayıcı fonksiyona ait değişkenleri,
#iç fonksiyonumuzda değiştirebilmek için nonlocal ifadesine ihtiyacımız vardır.
        

    