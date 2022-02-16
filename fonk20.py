a = divmod(10 , 2)#bölünen ve bölen
print(a)#sonucunda ise sonuç ve bölümden kalan .
b = divmod(10 , 3)
print(b)
print("-" * 30)
c = enumerate("istihza")
print(list(c))

d = [i for i in enumerate("kardiz")]
print(d)

e = print(*enumerate("fatih"))

for i in enumerate("bayram"):
    print(i)

for sira , oge in enumerate("istihza" , 1):
    print("{}. {}".format(sira , oge)) 

exit()#çıkış
