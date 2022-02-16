import modul6

def ekle(sozcuk , anlam):
    mesaj = "{} kelimesi sözlüğe eklendi !"
    sozluk[sozcuk] = anlam
    print(mesaj.format(sozcuk))


print(dir(modul6))

print("-"*30)
import importlib
importlib.reload(modul6)  

print(dir(modul6))