#dictionary created
pelanggan = {
    "nama" : "tyo",
    "umur" : 18,
}

#list created
pelanggan_list = []


#akses dictionary
print(pelanggan["nama"])
print(pelanggan["umur"])

#input data dictionary
for i in range(len(pelanggan)):
    nama = input("Masukkan nama anda : ")
    umur = input("Masukkan umur anda : ")
    data = {
    "nama" : nama,
    "umur" : umur,
    }
    pelanggan_list.append(data)

#print(pelanggan_list[0])

for i in pelanggan_list:
    print("Nama pelanggan : ",i["nama"])
    print("Umur pelanggan : ",i['umur'])

#data = pelanggan_list[0]
#print("Nama pelanggan : ",data['nama'])
#print("Umur pelanggan : ",data['umur'])
#mengubah
#pelanggan['nama'] = 'slebew'