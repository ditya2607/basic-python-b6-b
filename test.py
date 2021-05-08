nama_kon = []
no_kon = []
def input_data():
	brapa_data = int(input("Berapa banyak data yang ingin diinput: "))
	for i in range(brapa_data):
		print("+=========================+")
		input_nama = str(input("Nama Kontak: "))
		input_telp = input("No. Telp: ")
		nama_kon.append(input_nama)
		no_kon.append(input_telp)
		print("Kontak Berhasil Ditambahkan!")
def tunjuk_kontak():
	for i in range(len(nama_kon)):
		print(f"Nama: {nama_kon[i]}")
		print(f"No. Telp: {no_kon[i]}")
print("Selamat Datang!")
while True:
	print("----Menu----")
	print("1. Daftar Kontak ")
	print("2. Tambah Kontak")
	print("3. Keluar")
	print( )
	pilihan = int(input("Pilih Menu: "))
	if pilihan == 1:
		tunjuk_kontak()
	elif pilihan == 2:
		input_data()
	elif pilihan == 3:
		print("Program Selesai, Sampai Jumpa!")
		break
	else:
		print("Menu Tidak Ditemukan!")
		pass