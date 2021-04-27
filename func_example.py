def luas_keliling(r):
    phi = 22/7
    luas = phi*r**2
    keliling = phi*2*r
    print("Luas lingkaran : ",luas)
    print("Keliling lingkaran : ",keliling)

r = int(input("Jari-jari lingkaran : "))
luas_keliling(r)

#perbedaan 
print("==========================")
def menghitung_lingkaran(r):
    phi = 22/7
    luas = phi*r**2
    keliling = phi*2*r
    return luas,keliling

r = int(input("Jari-jari lingkaran : "))
lingkaran = menghitung_lingkaran(r)
#print(lingkaran)
text = "Luas lingkaran adalah {:.2f} cm\u00b2 dan keliling {:.2f} cm".format(lingkaran[0],lingkaran[1])
print(text)