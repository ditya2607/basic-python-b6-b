print("Selamat datang!")
menu = ["--Menu--","1. Daftar kontak", "2. Tambah kontak", "3. Keluar"]
print(menu[0])
print(menu[1])
print(menu[2])
print(menu[3])

daftar_kontak = {
    "Nama :" : "Ditya",
    "No telepon :" : "081327518596",
}

kontak_in_list = [daftar_kontak]
pilih_menu = int(input("Pilih menu : "))


if pilih_menu == 1:
    print("Daftar kontak")
    for x,y in daftar_kontak.items():
        print(x,y)
elif pilih_menu == 2:
    tambah_nama = input("Nama : ")
    tambah_nomor = input("No Telepon : ")
    data = {
        "Nama :" : tambah_nama,
        "No telepon :" : tambah_nomor,
    }
    kontak_in_list.append(data)
    for i in kontak_in_list:
        print("Nama : ",i["Nama :"])
        print("No telepon :",i["No telepon :"])
    print("Nomor berhasil ditambahkan")
elif pilih_menu == 3:
    print("Porgram selesai, sampai jumpa!")
else:
    print("Menu tidak tersedia")