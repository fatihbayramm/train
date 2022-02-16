demet = ("mehmet" , "ahmet" , 12 , 13 )
print(demet)
print(type(demet))

demet2 ="mehmet" , 12 , 23
print(demet2)
print(type(demet2))                #demetler de karakter dizileri gibi değiştirilemez (immutable) veri tipidir.

a = tuple("fagahdfhjsgfj")
print(a)
b = tuple('sadasldşasd')
print(b)

c = tuple(["ahmet" , "mehmet" , 12 , 13])
print(c)

#tek öğeli demet oluşturma :
demet3 = ("ahmet" , ) #ya da :
print(type(demet3))
demet4 = "mehmet" , #virgül konulmazsa bir karakter dizisi olur.
print(type(demet4))