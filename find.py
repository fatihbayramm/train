#find, rfind()
#find() ve rfind() metotları tamamen index() ve rindex() metotlarına benzer.
#find() ve rfind() metotlarının görevi de bir karakter dizisi içindeki bir karakterin konumunu sorgulamaktır:
#index() ve rindex() metotları karakter dizisi içindeki karakteri sorgularken,
#eğer o karakteri bulamazsa bir ValueError hatası verir:
#Ama find() ve rfind() metotları böyle bir durumda -1 çıktısı verir:

kardiz = "adana"
print(kardiz.find("a" , 1))
print(kardiz.find("z"))
print(kardiz.rfind("a" , 0))