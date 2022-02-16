alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
harf_listesi = list(alfabe)
print(harf_listesi)

li = list()
print(li)

a = list(range(10))
print(a)
print(type(a))

meyveler = ["elma" , "armut" , "kiraz" , "portakal"]
for oge_sirasi in range(len(meyveler)):
    print("{}.{}".format(oge_sirasi , meyveler[oge_sirasi]))

print("-"*30)

meyveler = ["elma" , "armut" , "kiraz" , "portakal"]
for sira , oge in enumerate(meyveler , 1):
    print("{}.{}".format(sira , oge))    
print("-"*30)

print(meyveler[-1])
#Karakter dizileri konusunu işlerken öğrendiğimiz dilimleme yöntemi listeler için de aynen geçerlidir. 

    

