liste = ["elma", "armut", "çilek"]
liste.insert(0 , "portakal")
print(liste)

a = ["Ahmet Özkoparan",
"Mehmet Veli",
"Serdar Güzel",
"Zeynep Güz"]
print(a)
a.insert(1 , "Fatih Bayram")
print(a)

b = ["elma" , "armut" , "kiraz"]
b.remove("elma")
print(b)

meyveler = ["elma", "armut", "çilek", "kiraz"]
print(reversed(meyveler))
print(*reversed(meyveler))

for i in reversed(meyveler) :
    print(i)

   
   
   
liste2 = ["elma", "armut", "çilek"]
liste2.reverse()
print(liste2)