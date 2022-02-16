def ismin_ne():
    isim = input("İsmin ne ?")
    return isim

print("Merhaba {} ! Nasılsın ?".format(ismin_ne()))

ad = ismin_ne()
print("Naber lan {} şerefsizi ??".format(ad))

def fonk():
    print(2)
    return
    print(3)#Görüldüğü üzre returnden sonra gelen satır çalışmıyor .
fonk()    

def func(n):
    if n < 0:
        return "eksi değerli sayı olamaz !"
    else:
        return n
f = func(2)
print(f)            

