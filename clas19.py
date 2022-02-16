class Kitaplar():
    def __init__(self , deger = None , sira = None):
        self.liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
                      ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
                      ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem') ]
        if not deger and not sira :
            l = self.liste
        else:
            l = [li for li in self.liste if deger == li[sira]]
        for i in l:
            print(*i , sep = ", ")
    @classmethod
    def isbnden(cls , isbn):
        cls(isbn , 0)
    @classmethod    
    def yazardan(cls , yazar):
        cls(yazar , 1)
    @classmethod    
    def eserden(cls , eser):
        cls(eser , 2)
    @classmethod    
    def yayinevi(cls , yayinevi):
        cls(yayinevi , 3)            

Kitaplar.isbnden("9789753424080")
Kitaplar.yazardan("Nietzsche")
Kitaplar.eserden("Postmodern Bir Kız Sevdim")
Kitaplar.yayinevi("Cem")
print("-"*30)
print(Kitaplar())
print("-"*30)

