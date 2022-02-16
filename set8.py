k1 = set([1, 2, 3, 4])
k2 = set([1, 3, 5, 7])
a = k1.intersection(k2)
print(a)
#ikisi de kesişim anlamına gelir .
b = k1 & k2
print(b)

tr = "şçöğüıŞÇÖĞÜİ"

parola = input("Sisteme giriş için bir parola belirleyin: ")
if set(tr) & set(parola) :
    print("Lütfen parolanızda Türkçe karakter kullanmayın !")
else:
    print("Parolanız kabul edildi !")    

k3 = set([1, 2, 3, 4])
k4 = set([1, 3, 5, 7])
k3.intersection_update(k4)
print(k3)   
print(k4) 

