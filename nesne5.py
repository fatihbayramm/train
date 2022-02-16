class Sinif():
    def __new__(cls , *args , **kwargs):
        print("Yeni sınıf inşa edilirken lütfen bekleyiniz ...")
        return object.__new__(cls , *args , **kwargs)
    def __init__(self):
        print("Merhaba sınıf")    

a = Sinif()
a        