#all() fonksiyonunun görevi, bir dizi içinde bulunan bütün değerler True ise True değeri,
#eğer bu değerlerden herhangi biri False ise de False değeri döndürmektir.
liste = [1,2,3,4,5]
print(all(liste))
liste2 = [0,1,2,3,4,5]
print(all(liste2))
liste3 = ["ahmet" , "mehmet" , ""]
print(all(liste3))

a = 3
t1 = a == 3
t2 = a < 4
t3 = a % 2 == 1
print(all([t1 , t2 , t3]))
print("-"*60)

#any() fonksiyonunun görevi de, bir dizi içindeki bütün değerlerden en az biri True ise True çıktısı vermektir.
degisken = ["ahmet" , "sadi" , ""]
print(any(degisken))