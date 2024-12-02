class SistemPendataanHewan:
    def _init_(self):
        self.daftar_hewan = []

    def tambahkan_hewan(self):
        """Menambahkan hewan baru ke dalam daftar."""
        nama = input("Masukkan nama hewan: ")
        spesies = input("Masukkan spesies hewan: ")
        self.daftar_hewan.append({"nama": nama, "spesies": spesies})
        print(f"Hewan '{nama}' dengan spesies '{spesies}' berhasil ditambahkan.\n")

    def cek_daftar_hewan(self):
        """Menampilkan daftar hewan yang tercatat."""
        print("Daftar Hewan di Kebun Binatang:")
        if self.daftar_hewan:
            for indeks, hewan in enumerate(self.daftar_hewan, 1):
                print(f"{indeks}. {hewan['nama']} - {hewan['spesies']}")
        else:
            print("Belum ada hewan yang terdaftar.")
        print()

    def hapus_hewan(self):
        """Menghapus hewan berdasarkan nomor dalam daftar."""
        self.cek_daftar_hewan()
        if self.daftar_hewan:  # Cek apakah daftar hewan tidak kosong
            try:
                nomor = int(input("Masukkan nomor hewan yang ingin dihapus: "))
                if 1 <= nomor <= len(self.daftar_hewan):
                    hewan_dihapus = self.daftar_hewan.pop(nomor - 1)
                    print(f"Hewan '{hewan_dihapus['nama']}' dengan spesies '{hewan_dihapus['spesies']}' berhasil dihapus.\n")
                else:
                    print("Nomor tidak valid.\n")
            except ValueError:
                print("Input harus berupa angka.\n")

    def hitung_hewan(self):
        """Menghitung jumlah hewan yang tercatat."""
        jumlah = len(self.daftar_hewan)
        print(f"Jumlah hewan yang tercatat: {jumlah}\n")

    def menu(self):
        """Menampilkan menu utama sistem pendataan hewan."""
        while True:
            print("=" * 60)
            print("Selamat Datang di Sistem Pendataan Hewan Kebun Binatang")
            print("1. Tambahkan Hewan Baru")
            print("2. Cek Daftar Hewan")
            print("3. Hapus Hewan")
            print("4. Hitung Jumlah Hewan yang Tercatat")
            print("5. Keluar")
            print("=" * 60)

            pilihan = input("Masukkan pilihan menu (1-5): ")
            print()

            if pilihan == "1":
                self.tambahkan_hewan()
            elif pilihan == "2":
                self.cek_daftar_hewan()
            elif pilihan == "3":
                self.hapus_hewan()
            elif pilihan == "4":
                self.hitung_hewan()
            elif pilihan == "5":
                print("Terima kasih telah menggunakan sistem ini!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.\n")


# Memulai program
sistem = SistemPendataanHewan()
sistem.menu()
