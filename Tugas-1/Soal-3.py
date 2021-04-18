Ujian_teori = float(input("Nilai ujian teori kamu : "))
Ujian_praktik = float(input("Nilai ujian praktik kamu : "))

if Ujian_teori >= 70 and Ujian_praktik >= 70:
    print ("Selamat, anda lulus!")
elif Ujian_teori >= 70 and Ujian_praktik <70:
    print("Anda harus mengulang ujian praktik.")
elif Ujian_teori <70 and Ujian_praktik >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktik.") 