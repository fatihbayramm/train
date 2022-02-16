def bas(*args , start = "" , **kwargs):
    for oge in args:
        print(start+oge , **kwargs)
f = open("../te.txt" , "w")

bas("oge1" , "oge2" , "oge3" , "oge4" , start = ".#" , end ="" , file = f)

#"*args"  : Rastgele Sayıda İsimsiz Parametre Belirleme
#"**kwargs"  : Rastgele Sayıda İsimli Parametre Belirleme