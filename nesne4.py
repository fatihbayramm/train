#class Sinif(taban_sinifi1 , taban_sinifi2):#çoklu miras alma
    #pass


class c1:
    sn1 = 'sn1'

    def __init__(self):
        self.ön1 = 'ön1'
        print(self.ön1)

    def örn_metot1(self):
        self.öm1 = 'öm1'
        return self.öm1

    def ortak_metot(self):
        self.om = 'ortak metot_c1'
        return self.om    

class c2:
    sn2 = 'sn2'

    def __init__(self):
        self.ön2 = 'ön2'
        print(self.ön2)

    def örn_metot2(self):
        self.öm2 = 'öm2'
        return self.öm2

    def ortak_metot(self):
        self.om = 'ortak metot_c2'
        return self.om    
    
        

class c3:
    sn3 = 'sn3'

    def __init__(self):
        self.ön3 = 'ön3'
        print(self.ön3)

    def örn_metot3(self):
        self.öm3 = 'öm3'
        return self.öm3

    def ortak_metot(self):
        self.om = 'ortak metot_c3'
        return self.om    

class c4(c1 , c2 , c3):
    def __init__(self):
        super().__init__()

s = c4()
print(s.ortak_metot())        

