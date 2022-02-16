def selamla():
    print("Selam Zalim Dünya !")

selamla()   

def sistem_bilgisi():
    import sys 
    print("\nSistemde kurulu Python'ın ;")
    print("\tAna sürüm numarası :" , sys.version_info.major)
    print("\tAlt sürüm numarası :" , sys.version_info.minor)
    print("\tMinik sürüm numarası :" , sys.version_info.micro)

    print("\nKullanılan işletim sisteminin ;")
    print("\tAdı :" , sys.platform)
sistem_bilgisi()

    