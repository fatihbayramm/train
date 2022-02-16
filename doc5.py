f = open("../yeni.txt" , "r+")
with open("../yeni.txt" , "r+") as f :
    veri = f.readlines()
    veri.insert(3 , "Gül Bayram\t: 0552 252 15 45\n")#burda ise dosyanın istediğimiz bir yerine ekleme yaptık .
    f.seek(0)
    f.writelines(veri)