km = set("adana")
for i in km :
    print(i)

km.clear()
print(km)    

km2 = set("kahramanmaraş")
yedek = km2.copy()
print(yedek)
print(km2)

print("-"*60)

kume = set(["elma", "armut", "kebap"])
kume.add("çilek")
print(kume)

yeni = [1 , 2 , 3]
for i in yeni:
    kume.add(i)
print(kume)    