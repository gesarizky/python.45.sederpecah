# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# function kpk dan fpb
def fpb(a,b):
    if a<b:
        smaller=a
    else:
        smaller=b
    for i in range (1,smaller+1):
        if a%i==0 and b%i==0:
            fpb=i
        # else:
        #     continue
    return fpb

def kpk(a,b):
    kpk=int(a*b/fpb(a,b))
    return kpk

# Menginput
print('Masukan Nilai dari a/b')
a = int(input("Tuliskan Nilai a : "))
b = int(input("Tuliskan Nilai b: "))

# Mengkonversi
a1 = int(a/fpb(a,b))
a2 = int(b/fpb(a,b))

# Menampilkan Hasil
print('==========================================================')
print('Maka Bentuk sederhana Dari Pecahan ',a,'/',b)
print('Dengan KPK Pecahan =',fpb(a,b))
print('Setelah disederhanakan menjadi = ',a1,' /',a2)
print('==========================================================')
