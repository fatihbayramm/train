kardiz = "kahramanmaraş"
print("A sayısı :" , kardiz.count("a"))
print("Ş sayısı :" , kardiz.count("ş"))#count metodu karakter dizisindeki ögelerin kaç tane oldugunu sayar.

sehir = "adana"
print(sehir.count("a" , 0))#burda ise a harfini bulmak için kaçıncı sıradan başlaması gerektiğini yazıyoruz.
print(sehir.count("a" , 2))
print(sehir.count("a" , 3))

print("-"*100)

parola = input("Parolanız : ")
kontrol = True
for i in parola:
    if parola.count(i) > 1:
        kontrol = False

if parola == "" or " ":
    kontrol = False             
        
if kontrol:
    print("Parolanız onaylandı !")
else:
    print("Parolanızda aynı harfi bir defa kullanabilirsiniz.")   

print("-"*100)
kelime = input("Herhangi bir kelime giriniz : ")
for harf in kelime:
    print("{} harfi {} kelimesinde {} defa geçiyor !".format(harf , kelime , kelime.count(harf)))    


piton = "python programlama dili"
print(piton.count("a", 15 , 17 ))#burada ise 15. ve 17. ögeler arasındaki a harflerinin sayısını buluruz (15. dahil , 17. değil)
                                #yani count metodu 3 tane parametre alabiliyor.
                                
