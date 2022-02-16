import os
import sys
import subprocess#subprocess ismi uzun olduğundan bunu kısaltabiliriz şu şekilde :
import subprocess as sp 




print(os.getcwd())#bu komut ile hangi dizinde olduğumuzu öğrendik.

os.makedirs#bu komut ile dizin oluşturduk

print(sys.version)#python ın sürümünü verir.

subprocess.call("te.txt")
sp.call("te.txt")




