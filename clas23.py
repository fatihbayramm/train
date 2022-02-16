import sys
sys.path.append(r"C:/Users/wante/AppData/Local/Programs/Python/Python39")

class Sinif():
    __gizli = "gizli"

    def ornek_metodu(self):
        print(self.__gizli)
        print("örnek metodu")

    @classmethod
    def sinif_metodu(cls):
        print("sınıf metodu")

    @staticmethod
    def statik_metot():
        print("statik metot")        

#Python’da baş tarafında yukarıdaki gibi iki adet alt çizgi olan, ancak uç tarafında alt çizgi bulunmayan
#(veya yalnızca tek bir alt çizgi bulunan) bütün öğeler birer gizli üyedir.
#Dışarıya kapalı olan bu gizli üyelere, normal yöntemleri kullanarak sınıf dışından erişemezsiniz.        