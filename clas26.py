class Program():
    def __init__(self):
        pass 
    @property    
    def versiyon(self):
        return "0.1" 

program = Program()
print(program.versiyon)       
#versiyon() fonksiyonunu, @property bezeyicisi yardımıyla bir niteliğe dönüştürdüğümüz için,
#artık bu fonksiyonu parantezsiz kullandığımıza dikkat edin.   

class Yazilim():
    def __init__(self):
        self.veri = 0
    @property
    def data(self):
        return self.veri

p = Yazilim()

print(p.data)
print(p.veri)

p.veri = 5
print(p.data)
print(p.veri)