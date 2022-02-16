import modul6

import importlib
importlib.reload(modul6)


modul6.ekle("araba" , "car")
a = modul6.ara("araba")
print(a)

import importlib
importlib.reload(modul6)

print(dir(modul6))

print("-"*100)

modul6.sil("kitap")
modul6.sil("araba")
modul6.ekle("kitap" , "book")