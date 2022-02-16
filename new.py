print("ß".lower())#oldugu gibi print ediyor

print("ß".casefold())#casefold ise değişik biçimlerde print edebiliyor.
print("-"*100)

kelime = input("Herhangi bir kelime giriniz : ")
sayac = ""
for harf in kelime:
    if harf not in sayac:
        sayac += harf

for harf in sayac:
    print("{} harfi {} kelimesinde {} defa geçiyor !".format(harf , kelime , kelime.count(harf)))

