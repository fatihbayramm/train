sozluk = {"kitap"      : "book",
          "bilgisayar" : "computer",
          "programlama": "programming"}

def ara(sozcuk):
    hata = "{} kelimesi sözlükte yok !"
    print(sozluk.get(sozcuk , hata.format(sozcuk)))


def ekle(sozcuk , anlam):
    mesaj = "{} kelimesi sözlüğe eklendi !"
    sozluk[sozcuk] = anlam
    print(mesaj.format(sozcuk))

def sil(sozcuk):
    try:
        sozluk.pop(sozcuk)
    except KeyError as err:
        print(err , "kelimesi bulunamadı !")
    else:
        print("{} kelimesi sözlükten silindi !".format(sozcuk))     


print("1. Sözlükte kelime ara")
print("2. Sözlüğe kelime ekle")
print("3. Sözlükten kelime sil")

if __name__ == "__main__":


    no =  int(input("Yapmak istediğiniz işlemin numarasını giriniz : "))

    if no == 1 :
        sozcuk = input("Aradığınız sözcük : ")
        ara(sozcuk)
    elif no == 2:
        sozcuk = input("Ekleyeceğiniz sözcük : ")
        anlam = input("Eklediğiniz sözcüğün anlamı : ")
        ekle(sozcuk , anlam)
    elif no == 3:
        sozcuk = input("Sileceğiniz sözcük : ")
        sil(sozcuk)        
    else:
        print("Yanlış işlem !")    


print(__name__)#direkt yazdığım modülde olduğu için __name__ in değeri = __main__ oldu.