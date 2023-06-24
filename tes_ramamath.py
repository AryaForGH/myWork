print("========== Modul by Arya Mwehehe ==========")

import ramamath as rm 

                                    # Function Untuk Mencari Volume Kubus
print("\n===== Volume Kubus =====")
angka = int(input("Masukkan Angka Volume         :  "))
hasil_volume = rm.VolKubus(angka)

print("Volume Kubus Adalah           : ", hasil_volume)


                                    # Function Untuk Mencari Keliling Kubus
print("\n===== Keliling Kubus =====")
angka = int(input("Masukkan Angka Keliling       :  "))
hasil_keliling = rm.KelKubus(angka)

print("Keliling Kubus Adalah         : ", hasil_keliling)


                                    # Function Untuk Mencari Luas Kubus
print("\n=====  Luas Kubus  =====")
angka = int(input("Masukkan Angka Luas           :  "))
hasil_luas = rm.LuasKubus(angka)

print("Luas Sisi Kubus Adalah        : ", hasil_luas)


                                    # Function Untuk Mencari Keliling Lingkaran
print("\n===== Luas Lingkaran =====")
angka = int(input("Masukkan Angka Luas Lingkaran :  "))
hasil_LuasLingkaran = rm.LuasLingkaran(angka)

print("Luas Lingkaran Adalah         : ", hasil_LuasLingkaran)


                                    # Function Untuk Mencari Diameter Lingkaran
print("\n===== Diameter Lingkaran =====")
angka = int(input("Masukkan Angka Luas Lingkaran :  "))
hasil_DiameterLingkaran = rm.DiameterLingkaran(angka)

print("Diameter Lingkaran           : ", hasil_DiameterLingkaran)