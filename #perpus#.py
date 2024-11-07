import pandas as pd 
from time import sleep
from tabulate import tabulate
import os
import datetime as dt

def login(): 
    print('='*100)
    print("||                     //        SELAMAT DATANG DI PUSTAKA KITA         \\\\                        ||")
    print("||                    |||             Program Perpustakaan               |||                      || ")
    print("||                      \\\\                                              //                        || ")
    print('='*100)
    sleep(1)
    print("\nApakah anda sudah membuat akun?")
    while True : 
        jawab = input("ya/tidak : ")
        if jawab == "ya":
            signin()
            break
        elif jawab == "tidak":
            signup()
            break
        else :
            print('masukkan jawaban yang benar!')
            continue


def signin():
    os.system('cls')
    df = pd.read_csv('datauser.csv')
    while True:
        id = input("Masukkan Username : ")
        pas = int(input("Masukkan Password : "))
        if id in df['Username'].values and pas in df['Password'].values :
            menu()
            break
        else :
            print('masukkan username atau password yang benar!')
            continue

def signup():  #fungsi bernama signup
    os.system('cls')    #untuk membersihkan tampilan sebelumnya
    print('-------------------- sign up --------------------')
    nama = input("Masukkan Nama : ")    #mengambil masukan nama pengguna berupa string 
    id = input("Masukkan Username yang ingin digunakan (huruf) : ") #mengambil masukan username pengguna berupa string
    pas = int(input("Masukkan Password yang ingin digunakan (angka) : "))   #mengambil masukan password pengguna berupa integer

    df = None #mengosongkan variabel
    try:  #untuk menguji blok kode untuk kesalahan    
        df = pd.read_csv('datauser.csv')    #membaca file csv bernama datauser

        if df.empty:    #jika file yang ada di variabel df kosong
            df = pd.DataFrame(columns=('Nama', 'Username', 'Password')) #buat data frame dengan kolom nama, username, dan pasword
    except FileNotFoundError:   #jika file yang ada di variabel df tidak kosong
        df = pd.DataFrame(columns=('Nama', 'Username', 'Password')) #buat data frame dengan kolom nama, username, dan pasword
    df.loc[1] = (nama, id, pas) # memasukkan nilai yang didapat dari masukan pengguna ke data frame yang telah dibuat
    df.to_csv('datauser.csv', index=False)  #memasukkan data frame ke file csv bernama datauser dengan index bernilai false
       
    while True: #loop dengan kondisi true yang artinya loop akan berjalan terus menerus
        verif = int(input("Masukkan kembali Password yang ingin digunakan : ")) #meminta masukan password pengguna berupa integer
        if pas == verif:    #jika nilai di variabel pas sama dengan nilai di variabel verif
            print("Data anda sedang diproses.....")     #mencetak string "data anda sedang diproses...."
            sleep(2)    #untuk menjeda layar selama 2 detik
            print('-'*57)
            print('-------- anda berhasil mendaftar! silahkan login --------')  #mencetak string "anda berhasil mendaftar! silahkan login"
            print('-'*57)
            sleep(4)    #jeda layar selama 4 detik
            signin()    #masuk ke fungsi signin
            break   #untuk menghentikan eksekusi loop
        elif pas != verif:  #jika nilai di variabel pas tidak sama dengan nilai di variabel verif
            print("\nPassword anda salah, silahkan masukkan kembali password anda!")    #cetak string "Password anda salah, silahkan masukkan kembali password anda!"
            continue    #untuk melanjutkan ke iterasi selanjutnya

def peminjaman() :  #fungsi bernama peminjaman
    os.system('cls')    #untuk membersihkan layar sebelumnya
    nopeminjam = int(input('masukkan nomor peminjam (angka) : '))   #input masukan nomor peminjam berupa integer
    judulbuku = input('masukkan judul buku : ')  #input masukan judul buku berupa string
    nopanggilbk = input('masukkan nomor panggil buku : ')   #input masukan nomor panggil buku berupa string
    tanggalpinjam = input('masukkan tanggal pinjam buku (YYYY-MM-DD) : ')   #input masukan tanggal pinjam buku berupa string
    ubahdt = dt.datetime.strptime(tanggalpinjam, '%Y-%m-%d')   #mengubah tanggal pinjam yang awalnya string ke objek datetime 
    tgk = ubahdt + dt.timedelta(days=7) #menambahkan 7 hari ke tanggal pinjam buku sebelumnya 
    jatuhtempo = tgk.strftime('%Y-%m-%d')   #mengubah tanggal pinjam yang ditambah 7 hari menjadi string
    tanggalpinjam2 = ubahdt.strftime('%Y-%m-%d')    #mengubah tanggal pinjam menjadi string

    dp = pd.read_csv('datapeminjaman.csv')  #membaca file csv bernama data peminjaman
    try:    #untuk menguji blok kode untuk kesalahan             
        if dp.empty: #jika file di variabel dp kosong
            dp = pd.DataFrame(columns=('nomor peminjam', 'judul buku', 'nomor panggil', 'tanggal pinjam','tanggal jatuh tempo','tanggal kembali'))  #buat data frame dengan kolom tersebut
            
    except FileNotFoundError:   #jika file di variabel dp tidak kosong 
        dp = pd.DataFrame(columns=('nomor peminjam', 'judul buku', 'nomor panggil', 'tanggal pinjam','tanggal jatuh tempo','tanggal kembali'))   #buat data frame dengan kolom tersebut
      
    dp.loc[-1] = (nopeminjam, judulbuku, nopanggilbk, tanggalpinjam2, jatuhtempo,'belum kembali')   #memasukkan nilai dari masukan pengguna sebelumnya ke data frame yang telah dibuat
    dp.to_csv('datapeminjaman.csv', index=False)    #memasukkan data frame ke dalam file csv bernama data peminjaman

    print('=' * 66)     #mencetak sama dengan sebanyak 66 kali sebagai pembatas
    print(f'||             Tanggal jatuh tempo buku : {tgk.year}-{tgk.month}-{tgk.day}             ||')   # mencetak tanggal jatuh tempo buku dengan format tahun-bulan-hari
    print('=' * 66)
    sleep(1.5)  #jeda layar selama 1.5 detik
    print('\n------------------- data berhasil ditambahkan! -------------------')    #mencetak string "data anda berhasil ditambahkan!"
    sleep(2)    #jeda layar selama 2 detik
    tanyamenu = input('apakah ingin kembali ke menu? (ya/tidak) : ')    #meminta masukan pengguna apakah ingin kembali ke menu
    while True :  #loop dengan kondisi true yang artinya loop akan berjalan terus menerus 
        if tanyamenu == 'ya' :  #jika masukan pengguna berupa "ya" 
            menu()  #masuk ke fungsi menu
            break   #menghentikan eksekusi loop
        elif tanyamenu == 'tidak' : #jika masukan pengguna "tidak"
            break   #hentikan loop

def pengembalian() : #fungsi bernama pengembalian
    os.system('cls')    #untuk membersihkan layar sebelumnya
    dk = pd.read_csv('datapeminjaman.csv')  #membaca file csv bernama data peminjaman
    
    nopinjam = int(input('masukkan nomor peminjam : ')) #meminta masukan nomor peminjam berupa integer
    indeksnp = dk.loc[dk['nomor peminjam'] == nopinjam].index.tolist()  #untuk mendapatkan indeks nomor peminjam
    a = int(indeksnp[0])    #mengubah indeks menjadi integer karna sebelumnya berupa list
    tglpinjam = dk.loc[a, 'tanggal pinjam'] #mencari tanggal pinjam yang ada di file data peminjaman menggunakn indeks sebelumnya
    tglkembali = input('masukkan tanggal kembali buku (YYYY-MM-DD) :  ')    #meminta input tanggal kembali berupa string 
    ftglkembali = dt.datetime.strptime(tglkembali, '%Y-%m-%d')  #mengubah tanggal kembali menjadi datetime
    ftglpinjam = dt.datetime.strptime(tglpinjam, '%Y-%m-%d')    #mengubah tanggal pinjam menjadi datetime

    tarif = 500    #tarif denda senilai 500 rupiah
    selisih = ftglkembali - ftglpinjam  #menghitung jumlah hari keterlambatan pemgembalian
    denda = (selisih.days - 7) * tarif  #jumlah hari keterlambatan dikurangi 7 hari lalu dikalikan dengan tarif denda

    if denda > 0 :  #jika denda lebih dari 0 
        print('='*75)
        print(f'||                   denda yang dibayarkan : Rp {denda}                      ||')    #mencetak jumlah denda
        print('='*75)
    elif denda <= 0 :   #jika denda kurang dari sama dengan 0
        print('='*77)
        print('||                   tidak ada denda yang dibayarkan                       ||')  #mencetak kalimat tidak ada denda yang dibayarkan
        print('='*77)    

    dk.loc[a, 'tanggal kembali'] = tglkembali   #memasukkan tanggal kembali dengan indeks nomor peminjam ke data frame
    dk.to_csv('datapeminjaman.csv', index=False)    #memasukkan nilai ke file csv data peminjaman
    sleep(0.5)  #jeda 0.5 detik
    tanyamenu = input('\napakah ingin kembali ke menu? (ya/tidak) : ')  #meminta masukan pengguna apakah ingin kembali ke menu
    while True :     #loop dengan kondisi true yang artinya loop akan berjalan terus menerus
        if tanyamenu == 'ya' :  #jika masukan pengguna berupa "ya" 
            menu()  #masuk ke fungsi menu
            break   #menghentikan eksekusi loop
        elif tanyamenu == 'tidak' : #jika masukan pengguna "tidak"
            break   #hentikan loop

def pengunjung() : #fungsi bernama pengunjung
    os.system('cls') #menghapus tampilan layar sebelumnya
    nama = input('masukkan nama : ') #untuk meminta masukkan pengguna berupa nama
    noanggota = input('masukkan nomor anggota : ') #untuk meminta masukkan berupa nomor anggota
    tanggal = input('masukkan tanggal (YYY-MM-DD) : ')#meminta memasukkan tanggal pengunjungan
    alamat = input('masukkan alamat : ') #meminta masukkan alamat pengunjung

    df = pd.read_csv('datapengunjung.csv') #membaca file csv bernama datapengunjung.csv
    try:   #blok kode untuk menangani kesalahan              
        if df.empty: #jika variabel df kosong
            df = pd.DataFrame(columns=('nomor anggota', 'nama', 'tanggal', 'alamat')) #buat data frame berisi kolom nomor anggota,nama,tanggal,alamat
            
    except FileNotFoundError:   #jika variabel df tidak kosong maka ini akan dijalankan
        df = pd.DataFrame(columns=('nomor anggota', 'nama','tanggal', 'alamat')) #buat data frame berisi kolom nomor anggota,nama,tanggal,alamat
      
    df.loc[-1] = (noanggota, nama, tanggal, alamat) #memasukkan nilai ke data frame sesuai urutan kolom
    df.to_csv('datapengunjung.csv', index=False)    #memasukkan data frame ke file csv data pengunjung
    sleep(1.5) #jeda 1,5 detik
    print('\n------------ data berhasil ditambahkan! ------------')
    sleep(2)
    tanyamenu = input('\napakah ingin kembali ke menu? (ya/tidak) : ')  #meminta masukan pengguna apakah ingin kembali ke menu
    while True :    #loop dengan kondisi true yang artinya loop akan berjalan terus menerus
        if tanyamenu == 'ya' :  #jika masukan pengguna berupa "ya" 
            menu()  #masuk ke fungsi menu
            break   #menghentikan eksekusi loop
        elif tanyamenu == 'tidak' : #jika masukan pengguna "tidak"
            break   #hentikan loop
        

def riwayatbuku() : #fungsi bernama riwayat
    os.system('cls')    #untuk membersihkan layar sebelumnya
    df3 = pd.read_csv('datapeminjaman.csv') #membaca file csv data peminjaman

    print('+','-'*121,'+')
    print('|                                                     RIWAYAT PEMINJAMAN                                                    |')
    print('+','-'*121,'+')
    print(tabulate(df3, headers='keys', tablefmt="fancy_grid", showindex=False))    #untuk mencetak data peminjaman dalam format tabel
    sleep(0.5)  #jeda 0.5 detik

    tanyamenu = input('\napakah ingin kembali ke menu? (ya/tidak) : ')  #meminta masukan pengguna apakah ingin kembali ke menu
    while True :    #loop dengan kondisi true yang artinya loop akan berjalan terus menerus
        if tanyamenu == 'ya' :  #jika masukan pengguna berupa "ya"
            menu()  #masuk ke fungsi menu
            break   #menghentikan eksekusi loop
        elif tanyamenu == 'tidak' : #jika masukan pengguna "tidak"
            break   #hentikan loop

def riwayatpengunjung() :
    os.system('cls')
    var = pd.read_csv('datapengunjung.csv')
    
    print('+','-'*66,'+')
    print('|                       RIWAYAT PENGUNJUNG                           |')
    print('+','-'*66,'+')
    print(tabulate(var, headers='keys', tablefmt="rounded_grid", showindex=False))   #untuk mencetak data pengunjung dalam format tabel
    sleep(0.5)
    
    tanyamenu = input('\napakah ingin kembali ke menu? (ya/tidak) : ')
    while True:
        if tanyamenu == 'ya' :  #jika masukan pengguna berupa "ya"
            menu()  #masuk ke fungsi menu
            break   #menghentikan eksekusi loop
        elif tanyamenu == 'tidak' : #jika masukan pengguna "tidak"
            break   #hentikan loop
    
def keluar() :
    os.system('cls')
    tanya = input('apakah anda yakin ingin keluar dari program? (ya/tidak) : ')
    while True :
        if tanya == 'ya' :
            break
        elif tanya == 'tidak' :
            menu()
            break

def menu() :
    os.system('cls')
    print("""
=========================================================================
|                     _   _   _____   __  _   _   _                     |
|     ______         | \_/ | | ____| |  \| | | | | |         ______     |
|     ******         |  _  | | __|_  |  _  | | |_| |         ******     |
|                    |_| |_| |_____| |_| |_|  \___/                     |
|                                                                       |
=========================================================================

[1]. peminjaman buku
[2]. pengembalian buku  
[3]. daftar pengunjung
[4]. riwayat peminjaman
[5]. riwayat pengunjung          
[6]. keluar
""")
    
    while True :
        pilihan = input("pilih menu(1/2/3/4/5/6) : ")
        if pilihan == '1' :
            peminjaman()
            break
        elif pilihan == '2' :
            pengembalian()
            break
        elif pilihan == '3' :
            pengunjung()
            break
        elif pilihan == '4' :
            riwayatbuku()
            break
        elif pilihan == '5' :
            riwayatpengunjung()
            break
        elif pilihan == '6' :
            keluar()
            break

login()


