import sys

sys.path.append(r"C:/Users/wante/AppData/Local/Programs/Python/Python39")

class Calisan():
    def __init__(self):
        self.kabiliyet = []




ahmet = Calisan() 
ahmet.kabiliyet.append("konuşkan")
print(ahmet.kabiliyet)

mehmet = Calisan()
print(mehmet.kabiliyet)#önceden mehmete konuşkan niteliğiin eklemediğimiz halde onun da kabiliyetleri arasındaydı 
                       #ama şimdi self ve __init__ kullanarak örnek niteliği şeklinde yazdığımız için sadece ahmet de var.
                       