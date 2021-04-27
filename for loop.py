buah = ["apple", "banana", "watermelon","melon","lemon","guava"]

#bentuk 1 for loop
for x in buah:
    print (x)

print("\n")

buah.append("Jeruk")
#bentuk 2
for x in range(len(buah)):
    print(buah[x])

daftar_kontak = {
    "Nama :" : "Ditya",
    "No telepon :" : +6281327518596,
}

for i in daftar_kontak:
    print(daftar_kontak[i])

for x,y in daftar_kontak.items():
    print(x,y)
