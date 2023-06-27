import ramamath as rm

print("========= Modul by Arya Mwehehe =========\n")

def show_menu():
    print ("\n")
    print("----------------- MENU -----------------")
    print("[1]  Volume Kubus")
    print("[2]  Keliling Kubus")
    print("[3]  Luas Kubus")
    print("[4]  Luas Lingkaran")
    print("[5]  Diameter Lingkaran")
    print("[6]  Luas Persegi Panjang")
    print("[7]  Keliling Persegi Panjang")
    print("[8]  Pertambahan")
    print("[9]  Pengurangan")
    print("[10] Perkalian")
    print("[11] Pembagian")
    print("[12] Luas Trapesium")
    print("[13] Luas Layang-Layang")

show_menu()
print("\n")

back = "y"
while back == "y":
    choose = int(input("Masukkan Menu     : "))
    print("\n---------------- OPERASI ---------------")

    if choose == 1 :
        angka = int(input("Masukkan Angka Volume              :  "))
        hasil_volume = rm.VolKubus(angka)
        print("Volume Kubus Adalah                : ", hasil_volume)

    if choose == 2:
        angka = int(input("Masukkan Angka Keliling            :  "))
        hasil_keliling = rm.KelKubus(angka)
        print("Keliling Kubus Adalah              : ", hasil_keliling)

    if choose == 3:
        angka = int(input("Masukkan Angka Luas                :  "))
        hasil_luas = rm.LuasKubus(angka)
        print("Luas Kubus Adalah                  : ", hasil_luas)

    if choose == 4:
        angka = int(input("Masukkan Angka Luas Lingkaran      :  "))
        hasil_LuasLingkaran = rm.LuasLingkaran(angka)
        print("Luas Lingkaran Adalah              : ", hasil_LuasLingkaran)

    if choose == 5:
        angka = int(input("Masukkan Angka Diameter Lingkaran  :  "))
        hasil_DiameterLingkaran = rm.DiameterLingkaran(angka)
        print("Diameter Lingkaran Adalah          : ", hasil_DiameterLingkaran)

    if choose == 6:
        panjang = int(input("Masukkan Panjang Persegi           :  "))
        lebar   = int(input("Masukkan Lebar Persegi             :  "))
        hasil_LuasPersegiPanjang = rm.LuasPersegiPanjang(panjang,lebar)
        print("Luas Persegi Panjang Adalah        : ", hasil_LuasPersegiPanjang)

    if choose == 7:
        panjang = int(input("Masukkan Panjang Persegi           :  "))
        lebar   = int(input("Masukkan Lebar Persegi             :  "))
        hasil_KelPersegiPanjang = rm.KelPersegiPanjang(panjang,lebar)
        print("Keliling Persegi Panjang Adalah    : ", hasil_KelPersegiPanjang)

    if choose == 8:
        num1 = int(input("Masukkan Angka Pertama     :  "))
        num2 = int(input("Masukkan Angka Kedua       :  "))
        hasil_pertambahan = rm.Pertambahan(num1,num2)
        print("Hasil Pertambahan Adalah   : ", hasil_pertambahan)

    if choose == 9:
        num1 = int(input("Masukkan Angka Pertama     :  "))
        num2 = int(input("Masukkan Angka Kedua       :  "))
        hasil_pengurangan = rm.Pengurangan(num1,num2)
        print("Hasil Pengurangan Adalah   : ", hasil_pengurangan)

    if choose == 10:
        num1 = int(input("Masukkan Angka Pertama     :  "))
        num2 = int(input("Masukkan Angka Kedua       :  "))
        hasil_perkalian = rm.Perkalian(num1,num2)
        print("Hasil Perkalian Adalah     : ", hasil_perkalian)

    if choose == 11:
        num1 = int(input("Masukkan Angka Pertama     :  "))
        num2 = int(input("Masukkan Angka Kedua       :  "))
        hasil_pembagian = rm.Pembagian(num1,num2)
        print("Hasil Pembagian Adalah     : ", hasil_pembagian)

    if choose == 12:
        a = int(input("Masukkan Alas Trapesium   : "))
        b = int(input("Masukkan Sisi Trapesium   : "))
        t = int(input("Masukkan Tinggi Trapesium : "))
        hasil_trapesium = rm.LuasTrapesium(a,b,t)
        print("Hasil Luas Trapesium Adalah : ", hasil_trapesium)

    if choose == 13:
        d1 = int(input("Masukkan Diagonal Pertama : "))
        d2 = int(input("Masukkan Diagonal Kedua   : "))
        hasil_layang = rm.LuasLayang(d1,d2)
        print("Hasil Luas Layang-Layang Adalah : ", hasil_layang)

    print("\n----------------- DONE ----------------")

    back = input("Apakah Anda Ingin Mengoperasikan Kembali ?? (y/n) : ")

    if back == 'y':
        show_menu()
    else:
        exit 
        print("\nAnda Telah Keluar Dari Program\n")