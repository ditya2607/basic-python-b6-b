nilai = [1,2,3,4,5]
print(nilai)
data = int(input("Tambahkan nilai : "))
#menyisipkan data
nilai.append(10)
nilai.append(12)
nilai.append(14)
nilai.append(data)
print(nilai)

#print berdasarkan indeks
print(nilai[2])
print(nilai[4])
print(nilai[6])

#panjang isi
print(len(nilai))

#ganti data
nilai[1] = 20
print(nilai)

tambah = input("Masukkan data : ")
nilai.append(tambah)
print(nilai)
nilai[3] = tambah
print(nilai)