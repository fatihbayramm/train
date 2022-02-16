liste = [1, 5, 3, 2, 9]
del liste[-1]
print(liste)
del liste

li1 = ["elma", "armut", "erik"]
li2 = li1
li1[0] = "karpuz"
print(li1)
print(li2)

liste1 = ["ahmet", "mehmet", "özlem"]
liste2 = liste1
print(id(liste1))
print(id(liste2))
print(id(liste1) == id(liste2))