from crud.lihat import lihat
from crud.create import create_record
from crud.update import update_record
from crud.delete import delete_record

def main():
    while True:
        print("\nMODIFIKASI DATABASE")
        print("-----------------------------------------")
        print("1. CREATE")
        print("2. READ")
        print("3. UPDATE")
        print("4. DELETE")
        print("5. EXIT")
        print("-----------------------------------------")

        pil = int(input("MASUKKAN PILIHAN: "))

        if pil == 1:
            nis = int(input("Masukkan  nis : "))
            nama_siswa = input("masukan nama siswa : ")
            alamat = input("Masukkan alamat : ")
            create_record( nis, nama_siswa, alamat )
            print("Data berhasil ditambahkan.")
            lihat()
        elif pil == 2:
            lihat()
        elif pil == 3:
            nis = int(input("Masukkan nis : "))
            nama_siswa = input("Masukkan nama_siswa : ")
            alamat = input("Masukkan alamat : ")
            update_record(nis, nama_siswa, alamat)
            print("Data berhasil diupdate.")
            lihat()
        elif pil == 4:
            nis = int(input("Masukkan nis siswa yang mau dihapus: "))
            delete_record(nis)
            print("Data berhasil dihapus.")
            lihat()
        elif pil == 5:
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tnisak ada. Silakan coba lagi.")

if __name__ == "__main__":
    main()
