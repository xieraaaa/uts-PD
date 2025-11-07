
#data awal 
obat = [
    ["OB001", "Paracetamol", 5000],
    ["OB002", "Amoxicillin", 12000],
    ["OB003", "Vitamin C", 8000],
    ["OB004", "OBH Combi", 10000]
]

layanan_kesehatan = [
    ["LK001", "Cek Tekanan Darah", 15000],
    ["LK002", "Cek Kolesterol", 25000],
    ["LK003", "Konsultasi Dokter", 30000]
]

vaksinasi = [
    ["V001", "Vaksin Influenza", 80000],
    ["V002", "Vaksin Covid-19", 120000],
    ["V003", "Vaksin Hepatitis", 100000]
]

konsultasi = [
    ["K001", "Konsultasi Obat Ringan", 10000],
    ["K002", "Konsultasi Obat Kronis", 20000],
    ["K003", "Konsultasi Anak", 15000]
]

transaksi = []

#bagian menunnya
menu = ""
while menu != "5":
    print("=" * 60)
    print("        SISTEM PELAYANAN APOTEK SEHAT SELALU")
    print("=" * 60)
    print("1. Konsultasi Obat")
    print("2. Penjualan Obat")
    print("3. Layanan Kesehatan & Pemeriksaan")
    print("4. Layanan Vaksinasi")
    print("5. Keluar")
    print("=" * 60)
    menu = input("Pilih menu: ")

    #konsultasi obat
    if menu == "1":
        print("\n=== LAYANAN KONSULTASI OBAT ===")
        print("Kode\tNama Layanan\t\tHarga")
        print("-" * 50)
        for k in konsultasi:
            print(k[0], "\t", k[1], "\t", k[2])
        kode = input("\nMasukkan kode konsultasi: ")

        ditemukan = 0
        for k in konsultasi:
            if k[0] == kode:
                nama = input("Nama Pasien: ")
                transaksi.append([nama, k[1], 1, k[2]])
                print("Pasien", nama, "melakukan", k[1], "- Total: Rp", k[2])
                ditemukan = 1
        if ditemukan == 0:
            print("Kode tidak ditemukan.")

    #penjualan obat
    elif menu == "2":
        print("\n=== PENJUALAN OBAT ===")
        print("Kode\tNama Obat\t\tHarga")
        print("-" * 50)
        for o in obat:
            print(o[0], "\t", o[1], "\t\t", o[2])
        kode = input("\nMasukkan kode obat: ")

        ditemukan = 0
        for o in obat:
            if o[0] == kode:
                nama = input("Nama Pembeli: ")
                jumlah = int(input("Jumlah beli: "))
                total = jumlah * o[2]
                transaksi.append([nama, o[1], jumlah, total])
                print("=" * 50)
                print("Pembelian", jumlah, o[1], " - Total: Rp", total)
                print("=" * 50)
                ditemukan = 1
        if ditemukan == 0:
            print("Kode obat tidak ditemukan.")

        print()

    #layanan kesehatan
    elif menu == "3":
        print("\n=== LAYANAN KESEHATAN & PEMERIKSAAN ===")
        print("Kode\tNama Pemeriksaan\t\tHarga")
        print("-" * 50)
        for l in layanan_kesehatan:
            print(l[0], "\t", l[1], "\t\t", l[2])
        kode = input("\nMasukkan kode layanan: ")

        ditemukan = 0
        for l in layanan_kesehatan:
            if l[0] == kode:
                nama = input("Nama Pasien: ")
                transaksi.append([nama, l[1], 1, l[2]])
                print("Pasien", nama, "melakukan", l[1], "- Biaya: Rp", l[2])
                ditemukan = 1
        if ditemukan == 0:
            print("Kode layanan tidak ditemukan.")

    #vaksinasi
    elif menu == "4":
        print("\n=== LAYANAN VAKSINASI ===")
        print("Kode\tJenis Vaksin\t\tHarga")
        print("-" * 50)
        for v in vaksinasi:
            print(v[0], "\t", v[1], "\t\t", v[2])
        kode = input("\nMasukkan kode vaksin: ")

        ditemukan = 0
        for v in vaksinasi:
            if v[0] == kode:
                nama = input("Nama Pasien: ")
                transaksi.append([nama, v[1], 1, v[2]])
                print("Pasien", nama, "melakukan vaksin", v[1], "- Biaya: Rp", v[2])
                ditemukan = 1
        if ditemukan == 0:
            print("Kode vaksin tidak ditemukan.")

    #keluar
    elif menu == "5":
        print("\n=== TERIMA KASIH ===\n")
        print("Daftar Transaksi Hari Ini:")
        print("-" * 60)
        print("Nama\t\tLayanan/Obat\t\tJumlah\tTotal")
        for t in transaksi:
            print(t[0], "\t", t[1], "\t", t[2], "\tRp", t[3])
        print("-" * 60)
        print("Sampai jumpa lagi!\n")

    else:
        print("Pilihan tidak valid, coba lagi!\n")
