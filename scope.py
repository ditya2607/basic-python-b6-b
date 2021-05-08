x = 20 #global scope
def coba(): #local scope
    global x #dari lokal menjadi global
    x = 10 
    print(x)
coba()
print(x)