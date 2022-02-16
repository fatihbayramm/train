bos_kume = set()
print(type(bos_kume))
kume = set(["elma" , "armut" , "kiraz"])
liste = ["elma" , "armut" , "kiraz"]
kume = set(liste)
demet = ("elma" , "armut" , "kebap")
kume = set(demet)
kardiz = "Python Programlama Dili için Türkçe Kaynak"
kume2 = set(kardiz)


#sayılardan kume olusturamayız . 

bilgi = {"işletim sistemi": "GNU", "sistem çekirdeği": "Linux",
"dağıtım": "Ubuntu GNU/Linux"}

kume4 = set(bilgi.items())
print(kume4)

print(bilgi)

kume5 = {'Python', 'C++', 'Ruby', 'PHP'}
print(type(kume5))
#kümelerde de sözlüklerde kullandığımız gibi süslü parantez kullanabiliriz
#kümelerin ayırt edici bir işareti yoktur .
print("-"*60)

bilgi = {"işletim sistemi": "GNU", "sistem çekirdeği": "Linux",
"dağıtım": "Ubuntu GNU/Linux"}
liste = [(anahtar , deger) for anahtar , deger in bilgi.items()]
kume = set(liste)
print(kume)