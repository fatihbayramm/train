import sys
sys.version
major = sys.version_info[0]
minor = sys.version_info[1]
micro = sys.version_info[2]
print(major , minor , micro , sep=".")
if sys.version_info[0] < 3:
    print("Kullandığınız python sürümü eski !") 