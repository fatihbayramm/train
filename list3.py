liste = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6]
print(liste[2][0])
print(liste[2][2])
yeni_liste = liste[2]
print(yeni_liste)

renkler = ["kırmızı", "sarı", "mavi", "yeşil", "beyaz"]
print(renkler)
renkler[0] = "siyah"
print(renkler)

renkler[2] = "mor"
print(renkler)

degisken = [1 , 2 , 3]
degisken[0:len(degisken)] = 5 , 6 , 7
print(degisken)

a = [2 , 4 , 6 , 8]
a = a + [10] #Listelere + işareti ile ekleyeceğiniz öğelerin de bir liste olması gerekiyor. 
print(a)

derlenen_diller = ["C", "C++", "C#", "Java"]
yorumlanan_diller = ["Python", "Perl", "Ruby"]

programlama_dilleri = derlenen_diller + yorumlanan_diller
print(programlama_dilleri)