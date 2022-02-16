kardiz = "python"
print(kardiz.swapcase())       #swapcase() büyük harfleri küçüğe ,
                               #küçük harfleri de büyüğe dönüştürür. 

a = "ELMA"
print(a.swapcase())

b = "ArMut"
print(b.swapcase())

kardiz = "istanbul"
for i in kardiz:
    if i == "İ":
        kardiz = kardiz.replace("İ" , "i")
    elif i == "i":
        kardiz = kardiz.replace("i" , "İ")
    else:
        kardiz = kardiz.replace(i , i.swapcase())
print(kardiz)                