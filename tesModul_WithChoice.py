import ramamath as rm

print("=========== Modul by Arya Mwehehe ===========\n")

def show_menu():
    print ("\n")
    print("---------- MENU ----------")
    print("[1] Volume Kubus")
    print("[2] Keliling Kubus")
    print("[3] Luas Kubus")
    print("[4] Luas Lingkaran")
    print("[5] Diameter Lingkaran")

show_menu()
print("\n")

choose = int(input("Masukkan Menu     : "))

if choose == 1 :
    angka = int(input("\nMasukkan Angka Volume              :  "))
    hasil_volume = rm.VolKubus(angka)
    print("Volume Kubus Adalah                : ", hasil_volume)

if choose == 2:
    angka = int(input("\nMasukkan Angka Keliling            :  "))
    hasil_keliling = rm.KelKubus(angka)
    print("Keliling Kubus Adalah              : ", hasil_keliling)

if choose == 3:
    angka = int(input("\nMasukkan Angka Luas                :  "))
    hasil_luas = rm.LuasKubus(angka)
    print("Luas Kubus Adalah                  : ", hasil_luas)

if choose == 4:
    angka = int(input("\nMasukkan Angka Luas Lingkaran      :  "))
    hasil_LuasLingkaran = rm.LuasLingkaran(angka)
    print("Luas Lingkaran Adalah              : ", hasil_LuasLingkaran)

if choose == 5:
    angka = int(input("\nMasukkan Angka Diameter Lingkaran  :  "))
    hasil_DiameterLingkaran = rm.DiameterLingkaran(angka)
    print("Diameter Lingkaran Adalah          : ", hasil_DiameterLingkaran)

back = input("\nApakah Anda Ingin Mengoperasikan Kembali ?? (y/n) : ")

if back == 'y':
    show_menu()
else:
    exit 
    print("\nAnda Telah Keluar Dari Program\n")