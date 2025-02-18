import random
from collections import Counter

def jalankan_permainan():
    nama_permainan = "The Great Bimshot"
    rentang_goa = 50
    BIMS_position = random.randint(1, rentang_goa)
    max_attempts = 5
    riwayat_tebakan = []
    posisi_terakhir = None
    pilihAcak = True;  #inisialisasi 
    
    print(f"Selamat datang di {nama_permainan}")#pesan selamat datang baru

    nama_user = input("masukan nama anda, dan siap untuk menangkap bims:")#diubah

    # Tampilkan goa-goa
    print(f"Ayo {nama_user}! Coba intai lokasi persembunyian Bims!:")#dirubah
    print("Goa:", " ".join(str(i) for i in range(1, rentang_goa + 1)))

    for percobaan in range(max_attempts):
        # Analisis Data dan Prediksi Tebakan
        if len(riwayat_tebakan) > 3: # Kurangi syarat minimal
            frekuensi_tebakan = Counter(riwayat_tebakan)
            tebakan_terbanyak = frekuensi_tebakan.most_common(1)[0][0]
            goa_aman = [i for i in range(1, rentang_goa + 1) if i != tebakan_terbanyak and i != posisi_terakhir]

            if goa_aman:
                BIMS_position = random.choice(goa_aman)
            else:
                BIMS_position = random.randint(1, rentang_goa)
        else:
            BIMS_position = random.randint(1, rentang_goa)

        try:
            pilihan_user = int(input(f"Tebak di goa nomor berapa bims bersembunyi? [1 - {rentang_goa}]: ")) #Di ubah
            if 1 <= pilihan_user <= rentang_goa:
                riwayat_tebakan.append(pilihan_user)
                posisi_terakhir = pilihan_user
                konfirmasi = input(f"Yakin mau menembak goa itu (yes/no)?: ").lower()#dirubah
                if konfirmasi == "yes":
                    if pilihan_user == BIMS_position:
                        print(f"\tKena! {nama_user} berhasil menembak Bims di goa {BIMS_position}!")#dirubah
                        break
                    else:
                        print("Meleset! Bims berhasil kabur. Coba lagi!")#Dirubah
                elif konfirmasi == "no":
                    continue
                else:
                    print("Mohon masukkan 'yes' atau 'no'.")
            else:
                print(f"Mohon masukkan angka antara 1 sampai {rentang_goa}.")
        except ValueError:
            print("Input tidak valid. Mohon masukkan angka.")

    print("\tSampai jumpa di perburuan Bims berikutnya!") # dirubah

if __name__ == "__main__":
    jalankan_permainan()
    