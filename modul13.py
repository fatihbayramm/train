import os , sys , random , subprocess

set_os = set(dir(os))
set_sys = set(dir(sys))
set_random = set(dir(random))
set_sp = set(dir(subprocess))

print(set_os & set_sys & set_random & set_sp)

moduller = ["os" , "sys" ,"random" , "subprocess"]

def kesisim_bul(moduller):
    kumeler = [set(dir(__import__(modul))) for modul in moduller]
    return set.intersection(*kumeler)

print(kesisim_bul(moduller))    