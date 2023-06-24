import ramamath as rm

print("========= Modul by Arya Mwehehe =========\n")

def show_menu():
    print ("\n")
    print("----------------- MENU -----------------")
    print("[1] Volume Kubus")
    print("[2] Keliling Kubus")
    print("[3] Luas Kubus")
    print("[4] Luas Lingkaran")
    print("[5] Diameter Lingkaran")
    print("[6] Keliling Persegi Panjang")

show_menu()
print("\n")


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
    hasil_KelPersegiPanjang = rm.KelPersegiPanjang(panjang,lebar)
    print("Keliling Persegi Panjang Adalah    : ", hasil_KelPersegiPanjang)

print("\n----------------- DONE ----------------")
back = input("Apakah Anda Ingin Mengoperasikan Kembali ?? (y/n) : ")

if back == 'y':
    show_menu()
else:
    exit 
    print("\nAnda Telah Keluar Dari Program\n")