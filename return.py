def luas_kotak(p,l):
    return p*l

def kel_kotak(p,l):
    keliling = p+p+l+l
    text = "kelilingnya adalah {}".format(keliling)
    return text

def luas_kotak_string(p,l):
    luas = p*l
    print(luas)

print(luas_kotak(5,10))
print(kel_kotak(5,10))
print(luas_kotak_string(5,10))