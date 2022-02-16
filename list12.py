li1 = [1, 3, 4]
li2 = [10, 11, 12]
li1.extend(li2)#bu şekilde append() metoduna yapsaydık li2 yi li1 in içine bir liste olarak ekleyecekti yani 
print(li1)      #[1,3,4,[10,11,12,]] olacaktı .

isletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
platformlar = ["IPhone", "Android", "S60"]
isletim_sistemleri.extend(platformlar)
print(isletim_sistemleri)