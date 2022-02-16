class Mat():
    @staticmethod
    def pi():
        return 22/7
    @staticmethod    
    def karekok(sayi):
        return sayi ** 0.5

m = Mat()

print(m.pi())#örnek niteliği üzerinden
print(m.karekok(4))#örnek niteliği üzerinden

print("-"*30)

print(Mat.pi())#Sınıf üzerinden
print(Mat.karekok(144))#Sınıf üzerinden
