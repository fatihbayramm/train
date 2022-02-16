def dosyadaki_karakter_sayisi(dosya , karakter):

    def karakter_sayisi(karakter_dizisi):
        sayac = 0
        for i in karakter_dizisi:
            if i == karakter:
                sayac += 1
        return sayac

    if type(dosya) == str:
        with open(dosya , "r") as f :
            return karakter_sayisi(f.read()) 
    else:
        return karakter_sayisi(dosya.read())

dosyadaki_karakter_sayisi("../final_takvimi.txt" , "a")                           

    
    