liste1 = ["ahmet", "mehmet", "özlem"]
liste2 = liste1[:]#dilimleme yöntemini kullanırsak ilk liste değişse bile ikinci liste aynı kalıyor.
liste1[0] = "veli"
print(liste1)
print(liste2)
print("-"*30)
liste3 = ["ahmet", "mehmet", "özlem"]
liste4 = list(liste3)#list fonk. yöntemini kullanırsak ikinci liste değişse bile ilk liste aynı kalıyor.
liste4[0] = "veli"
print(liste3)
print(liste4)