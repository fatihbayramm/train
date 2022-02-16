import modul6

import importlib
importlib.reload(modul6)
sozluk = {"kitap"      : "book",
          "bilgisayar" : "computer",
          "programlama": "programming"}

def ara(sozcuk):
    hata = "{} kelimesi sözlükte yok !"
    return sozluk.get(sozcuk , hata.format(sozcuk))       

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

