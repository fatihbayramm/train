f = open("../tahsilat_dosyası.txt" , "a")
with open("../tahsilat_dosyası.txt" , "a") as f :
    f.write("\nFatih Bayram  : 0551 141 28 51")#bu şekilde dosyanın sonuna ekleme yaptık.

with open("../tahsilat_dosyası.txt" , "r+") as f :
    veri = f.read()#bu şekilde de dosyanın başına ekleme yaptık .
    f.seek(0)
    f.write("Sedat Köz\t: 0322 234 45 45\n"+veri)