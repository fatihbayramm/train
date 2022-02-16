kardiz = "python"
print(kardiz.index("y"))#index metodu harfin hangi sırada oldugunu soyler.
#Bu metodun özelliği, sorguladığımız karakterin, karakter dizisi içinde geçtiği ilk konumu vermesidir.
c = "adana"
print(c.index("a" , 0))

print(c.index("a" , 1))#burada aramaya 1.sıradaki harften basladıgı için 0. sıradaki a yı es geçti ve 
                        #bize 2.sıradaki a harfinin sırasını verdi.
print(c.index("a" , 3))       #aynı şekilde.

print(c.index("a" , 1 , 3))#burada ise tıpkı count metondaki gibi aramaya 1.sıradan başladı ve 
                            #3. sırada bitirdi bu yüzden 2. sıradaki a harfinin sırasını verdi.
print("-"*30)                            
a = "karaman"

print(a.index("a", 0))
print(a.index("a", 1))
print(a.index("a", 2))
print(a.index("a", 3))
print(a.index("a", 4))

print("-"*30)

degisken = "adana"
for i in range(len(degisken)):
    print(degisken.index("a" , i))

print("-"*30)

veri = input("Metin girin :")
ara = input("Arayacağınız harf :")
for i in range(len(veri)):
    if i == veri.index(ara , i):
        print(i)

        
#bu metod ise karakter dizilerini sağdan sola doğru okur.
kardiz = "adana"
print(kardiz.rindex("a"))