#Eğer deyim mi yoksa ifade mi olduğundan emin olamadığınız bir şeyi eval() fonksiyonuna parametre 
#olarak verdiğinizde hata almıyorsanız o parametre bir ifadedir. Eğer hata alıyorsanız o parametre bir deyimdir.


b = eval("5+25")
print(b)

c = exec("a = 5")
print(a)

d = 20
exec("d = 43")
print(d)


x = 10


globals()["f"] = 5
print(globals())
print("-"*60)

def fonksiyon(param1 , param2):
    x = 10
    print(locals())
fonksiyon(10 , 20)    