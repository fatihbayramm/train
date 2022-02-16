sayilar = 0
notlar = []
for i in range(10):
    veri = int(input("{}.not ".format(i+1)))
    sayilar += veri
    notlar += [veri]

print("Girdiğiniz notlar : " , *notlar , sep=",")
print("Not ortalamanız : " , sayilar / 10)    