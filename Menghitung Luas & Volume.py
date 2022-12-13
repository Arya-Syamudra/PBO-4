class Luas():
    def start():
        print("="*50)
        print("=", "MENU".center(46), "=")
        print("=","Menghitung Luas".center(46, " "),"=")
        print("="*50)
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Lingkaran")
        print("4. Segitiga")
        print("5. kembali ke Menu")
        pilihan = input("Masukkan kode Menu :")
        if pilihan == "1":
            Luas.menu("Persegi")
        elif pilihan == "2":
            Luas.menu("Persegi Panjang")
        elif pilihan == "3":
            Luas.menu("Lingkaran")
        elif pilihan == "4":
            Luas.menu("Segitiga")
        elif pilihan == "5":
            pass
        else:
            print("Perintah tidak ditemukan")
            Luas.enter()
            Luas.start()
    def menu(namaBangun):
        print("="*50)
        print("=", "Menghitung Luas".center(46), "=")
        print("="*50)
        if namaBangun == "Persegi":
            sisi = float(input("Masukkan Panjang Sisi (cm) :"))
            Luas.persegi(sisi)
            Luas.enter()
            Luas.start()
        elif namaBangun == "Persegi Panjang":
            Panjang = float(input("Masukkan Panjang Sisi (cm) :"))
            Lebar = float(input("Masukkan Lebar Sisi (cm) :"))
            Luas.persegiPanjang(Panjang, Lebar)
            Luas.enter()
            Luas.start()
        elif namaBangun == "Segitiga":
            alas = float(input("Masukkan panjang Alas (cm) :")) 
            tinggi = float(input("Masukkan Tinggi (cm) :"))
            Luas.segitiga(alas, tinggi)
            Luas.enter()
            Luas.start()
        elif namaBangun == "Lingkaran":
            r = float(input("Masukkan Jari - Jari Lingkaran : (cm)"))
            Luas.lingkaran(r)
            Luas.enter()
            Luas.start()
        else:
            Luas.start() 
    def persegi (input_sisi):
        luas = input_sisi * input_sisi
        print("Luas Persegi adalah", luas, "Centimeter Persegi")
    def persegiPanjang(Panjang, Lebar):
        luas = Panjang * Lebar
        print("Luas Persegi Panjang adalah", luas, "Centimeter Persegi")
    def lingkaran (r):
        luas = 22/7 * (r**2)
        print("Luas Lingkaran adalah", luas, "Centimeter Persegi")
    def segitiga (alas, tinggi):
        luas = 1/2 * alas * tinggi
        print("Luas Segitiga adalah", luas , "Centimeter Persegi")
    def enter():
        enter = input("Tekan ENTER untuk lanjut")
        
class Volume():
    def start():
        print("="*50)
        print("=", "MENU".center(46),"=")
        print("=","Menghitung Volume".center(46),"=")
        print("="*50)
        print("1. Kubus")
        print("2. Balok")
        print("3. Tabung")
        print("4. Kerucut")
        print("5. kembali ke Menu")
        pilihan = input("Masukkan kode Menu : ")
        if pilihan == "1":
            Volume.menu("kubus")
        elif pilihan == "2":
            Volume.menu("balok")
        elif pilihan == "3":
            Volume.menu("tabung")
        elif pilihan == "4":
            Volume.menu("kerucut")
        elif pilihan == "5":
            pass
        else:
            print("Perintah tidak ditemukan")
            Volume.enter()
            Volume.start()
    def menu(namaBangunRuang):
        print("="*50)
        print("=","Menghitung Volume {namaBangunRuang}".center(46),"=")
        print("="*50)
        if namaBangunRuang == "kubus":
            rusuk = float(input("Masukkan Panjang Rusuk (cm) :"))
            Volume.kubus(rusuk)
            Volume.enter()
            Volume.start()
        elif namaBangunRuang == "balok":
            panjang = float(input("Masukkan Panjang Balok : "))
            lebar = float(input("Masukkan Lebar Balok : "))
            tinggi = float(input("Masukkan Tinggi Balok : "))
            Volume.balok(panjang, lebar, tinggi)
            Volume.enter()
            Volume.start()
        elif namaBangunRuang == "kerucut":
            r = float(input("Masukkan Jari-Jari Alas (cm) :"))
            t = float(input("Masukkan Tinggi Kerucut (cm) :"))
            Volume.kerucut(r, t)
            Volume.enter()
            Volume.start()
        elif namaBangunRuang == "tabung":
            r = float(input("Masukkan Jari - Jari (cm) :"))
            t = float(input("Masukkan Tinggi Tabung (cm) :"))
            Volume.tabung(r, t)
            Volume.enter()
            Volume.start()
        else:
            pass
    def kubus(sisi):
        volume = sisi **3
        print("Volume Kubus adalah", volume , "Centimeter Perkubik")
    def balok(panjang, lebar, tinggi):
        volume = panjang * lebar * tinggi
        print("Volume balok adalah", volume , "Centimeter Perkubik")
    def tabung(phi, r, t): 
        volume = 22/7 * ((r**2) * t)
        print("Volume dari Tabung adalah", volume, "Centimeter Perkubik")
    def kerucut(r, t):
        volume = 1/3 *(3.14 * (r**2) * t)
        print("Volume Kerucut adalah", volume, "Centimeter Perkubik")
    def enter():
        enter = input("Tekan ENTER untuk lanjut")

print("="*50)
print("=", "Nama: Arya Syamudra".center(46), "=")
print("=", "NIM : D0221357".center(46), "=")
while True :
    print("="*50)
    print("=","PROGRAM SEDERHANA".center(46),"=")
    print("=","Menghitung Luas dan Volume".center(46),"=")
    print("="*50)
    print("Menu : ")
    print("1. Menghitung Luas")
    print("2. Menghitung Volume")
    print("3. Exit Program")
    menu = input("Masukkan Kode Menu : ")
    if menu == "1":
        Luas.start()
    elif menu == "2":
        Volume.start()
    else :
        break
        
