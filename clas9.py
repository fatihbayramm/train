class Calısan():
    kabiliyet = ["sınıf niteliği"]
   

    def __init__(self):
        self.kabiliyet = ["örnek niteliği"]
        print(self.kabiliyet)

Calısan()#örnek niteliklerinde sınıfımızın calısması için böyle cagırmamız lazım.

Calısan().kabiliyet#sınıf niteliklerinde parantezsiz erişebiliyorduk ama örnek niteliklerinde parantezsiz 
                   #erişemiyoruz.

print(Calısan.kabiliyet)#sınıf niteliğine erişmek için
#sınıf adını kullanıyoruz



ahmet = Calısan()

print(ahmet.kabiliyet)#örnek niteliğine erişmek için
#örnek adını kullanıyoruz

print(ahmet.kabiliyet)
