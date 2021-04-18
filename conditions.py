x = int(input("Masukkan angka x : "))
y = int(input("Masukkan angka y : "))

if x > y:
    print("X lebih besar dari Y")
elif x < y:
    print("X kurang dari Y")
elif x == y:
    print("X sama dengan Y")
else:
    print("Salah input")

tanya = input("Mau makan? : ")

if tanya == 'ya' or tanya == 'YA' or tanya == 'Iya':
    print("Mau makan apa? ")
elif tanya == 'tidak':
    print("Mau mencoba cemilan?")
else:
    print("Oke")