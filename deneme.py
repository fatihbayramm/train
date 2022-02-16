kisi = input("Aradığınız kişinin adı ve soyadı  :")
kisi = kisi.lower()
if kisi == "ahmet öz":
    print("email: aoz@hmail.com")
    print("tel  : 02121231212")
    print("şehir: istanbul")
elif kisi == "mehmet söz":
    print("email: msoz@zmail.com")
    print("tel  : 03121231212")    
    print("şehir: ankara")
elif kisi == "mahmut göz":
    print("email: mgoz@jmail.com")   
    print("tel  : 02161231212") 
    print("şehir: istanbul")
else:
    print("Aradığınız kişi veritabanında yok ! ")    