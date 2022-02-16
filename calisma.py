import sys
_2x_metni = """Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırabilmek için sisteminizde Python'ın
3.x sürümlerinden biri kurulu olmalı."""
_3x_metni = "Programa Hoşgeldiniz ! "
if sys.version_info.major < 3 and sys.version_info.mınor <2:
    print(_2x_metni)
else:
    print(_3x_metni)     