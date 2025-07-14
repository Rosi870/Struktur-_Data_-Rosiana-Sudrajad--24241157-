# ================== Final Project UAS ==================
# Nama Kelompok :
# Afrizan Hidayat  (24241188)
# Rosiana Sudrajad (24241157)
# =======================================================

def meet1():
    print("\n== Meet1: Perbandingan Nilai Boolean ==")
    print("# a = 2 digit NIM pertama")
    print("# b = 2 digit NIM terakhir")

    a = 24
    b = 88

    print(f"\na = {a}")
    print(f"b = {b}")

    print("\nHasil perbandingan:")
    print(f"{a} < {b}  = {a < b}")
    print(f"{a} > {b}  = {a > b}")
    print(f"{a} >= {b} = {a >= b}")
    print(f"{a} <= {b} = {a <= b}")
    print(f"{a} != {b} = {a != b}")
    print(f"not a     = {not a}")
    print(f"not b     = {not b}")

def meet2():
    print("\n== Meet2: Operasi Logika ==")

    # NOT
    print("\n--- Operasi NOT ---")
    x = True
    z = not x
    print(f"not {x} = {z}")

    # AND
    print("\n--- Operasi AND ---")
    nilai = [True, False]
    for x in nilai:
        for y in nilai:
            z = x and y
            print(f"{x} AND {y} = {z}")

    # OR
    print("\n--- Operasi OR ---")
    for x in nilai:
        for y in nilai:
            z = x or y
            print(f"{x} OR {y} = {z}")

    # XOR (menggunakan != untuk boolean XOR)
    print("\n--- Operasi XOR ---")
    for x in nilai:
        for y in nilai:
            z = x != y
            print(f"{x} XOR {y} = {z}")

def meet3_4():
    print("\n== Meet3-4: Perhitungan Luas Persegi dan Segitiga ==")

    pilihan = input("Apakah Anda ingin menghitung 'persegi' atau 'segitiga'? ").lower()

    if pilihan == "persegi":
        try:
            panjang = int(input("Masukkan panjang: "))
            lebar = int(input("Masukkan lebar: "))
            luas = panjang * lebar
            print(f"Luas persegi = {luas}")
        except ValueError:
            print("Input harus berupa angka.")
    
    elif pilihan == "segitiga":
        try:
            alas = int(input("Masukkan alas: "))
            tinggi = int(input("Masukkan tinggi: "))
            luas = 0.5 * alas * tinggi
            print(f"Luas segitiga = {luas}")
        except ValueError:
            print("Input harus berupa angka.")
    
    else:
        print("Pilihan tidak dikenal. Silakan pilih 'persegi' atau 'segitiga'.")

def meet5():
    print("\n== Meet5: Kalkulator Sederhana ==")

    operasi = input("Anda ingin mengoperasikan apa? (+, -, x, :) ").strip()

    try:
        bil1 = float(input("Masukkan bilangan pertama: "))
        bil2 = float(input("Masukkan bilangan kedua: "))

        if operasi == "+":
            hasil = bil1 + bil2
            print(f"Hasil: {bil1} + {bil2} = {hasil}")
        elif operasi == "-":
            hasil = bil1 - bil2
            print(f"Hasil: {bil1} - {bil2} = {hasil}")
        elif operasi == "x":
            hasil = bil1 * bil2
            print(f"Hasil: {bil1} x {bil2} = {hasil}")
        elif operasi == ":":
            if bil2 != 0:
                hasil = bil1 / bil2
                print(f"Hasil: {bil1} : {bil2} = {hasil}")
            else:
                print("Error: Tidak bisa dibagi dengan nol.")
        else:
            print("Operasi tidak dikenali. Gunakan hanya +, -, x, atau :")
    except ValueError:
        print("Input harus berupa angka.")

def meet6():
    print("\n== Meet6: Kondisional Satu Baris (x if kondisi else y) ==")

    angka = 9
    umur = 19

    print(f"Angka {angka} adalah", "positif" if angka > 0 else "negatif")
    print(f"Angka {angka} adalah", "genap" if angka % 2 == 0 else "ganjil")

    klasifikasi_umur = "dewasa" if umur >= 18 else "anak-anak"
    print(f"Umur {umur} tergolong:", klasifikasi_umur)

    akses = input("Masukkan hak akses Anda: ").lower()
    print("Full akses" if akses == "admin" else "Akses ditolak")

def meet7():
    print("\n== Meet7: Pengecekan Password ==")

    password = input("Masukkan password: ")

    if len(password) < 8:
        print("Karakter kurang (minimal 8 karakter)")
    else:
        print("Karakter cukup")

def meet8():
    print("\n== Meet8: Manipulasi String - Menampilkan Karakter Tertentu ==")

    number = "1234567890"
    print(f"String number = {number}")

    print("Data terakhir      :", number[-1])
    print("Data pertama       :", number[0])
    print("Data ke-3 sampai 6 :", number[2:6])

def meet9_10():
    print("\n== Meet9-10: Memproses Input Nama Domain ==")

    domain = input("Masukkan nama domain Anda (contoh: google.com): ")

    try:
        nama, ekstensi = domain.split(".")
        print("Nama domain Anda adalah =", nama)
        print("Ekstensi yang Anda gunakan adalah =", ekstensi)
    except ValueError:
        print("Format domain tidak valid. Gunakan format seperti: nama.ekstensi (contoh: google.com)")

def menu():
    print("\n========== Final Project UAS ==========")
    print("##### Nama Kelompok : #####")
    print("Afrizan Hidayat  (24241188)")
    print("Rosiana Sudrajad (24241157)")
    print("########################")
    print("\nDaftar Program:")
    print("1. Meet1 (Perbandingan Nilai Boolean)")
    print("2. Meet2 (Operasi Logika)")
    print("3. Meet3-4 (Perhitungan Luas Persegi / Segitiga)")
    print("5. Meet5 (Kalkulator Sederhana)")
    print("6. Meet6 (Conditional Statement Satu Baris)")
    print("7. Meet7 (Pengecekan Password)")
    print("8. Meet8 (String Indexing & Slicing)")
    print("9. Meet9-10 (Memproses Nama Domain)")
    print("0. Keluar")

def main():
    while True:
        menu()
        try:
            pilihan = int(input("\nMasukkan nomor program yang ingin dijalankan: "))
            if pilihan == 1:
                meet1()
            elif pilihan == 2:
                meet2()
            elif pilihan == 3:
                meet3_4()
            elif pilihan == 5:
                meet5()
            elif pilihan == 6:
                meet6()
            elif pilihan == 7:
                meet7()
            elif pilihan == 8:
                meet8()
            elif pilihan == 9:
                meet9_10()
            elif pilihan == 0:
                print("Terima kasih! Program selesai.")
                break
            else:
                print("Pilihan tidak tersedia. Silakan coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()