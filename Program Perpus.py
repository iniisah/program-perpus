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
    sleep(0.5)
    print("\nApakah anda sudah membuat akun?")
    while True : 
        jawab = input("ya/tidak : ").lower()
        if jawab == "ya":
            signin()
            break
        elif jawab == "tidak":
            signup()
            break
        else :
            print(' \n >>> Masukkan jawaban yang benar! <<< \n ')
            continue




def signin():
    os.system('cls')
    df = pd.read_csv('datauser.csv')
    print('-------------------- SIGN IN --------------------\n')

    while True:
        id  = input("Masukkan Username         : ")
        pas = int(input("Masukkan Password (angka) : "))
        indeks = (df['Username'] == id).idxmax()
        if id in df['Username'].values and pas in df['Password'].values :
            if df.loc[indeks, 'Password'] == pas :
                menu()
                break
            else :
                print('\n>>> password anda salah! <<<\n')
                continue
        else :
            print('\n>>> username tidak ditemukan <<<\n')
            continue

def signup():
    os.system('cls')
    df = pd.read_csv('datauser.csv')
    print('-------------------- SIGN UP --------------------\n')
    nama = input("Masukkan Nama                                          : ")
    while True :
        id = input("Masukkan Username yang ingin digunakan                 : ")
        if id in df['Username'].values :
            print('\n*** Username telah digunakan, masukkan username yang lain! ***\n')
            continue
        pas = int(input("Masukkan Password yang ingin digunakan (angka)         : "))
        df = None 
        try:
            df = pd.read_csv('datauser.csv')

            if df.empty :
                df = pd.DataFrame(columns=('Nama', 'Username', 'Password'))

        except FileNotFoundError:
            df = pd.DataFrame(columns=('Nama', 'Username', 'Password'))

        df.loc[-1] = (nama, id, pas)
        df.to_csv('datauser.csv', index=False)    

        while True:
            verif = int(input("Masukkan kembali Password yang ingin digunakan (angka) : "))
            if pas == verif :
                print("\nData anda sedang diproses.....")
                sleep(2)
                print('-'*57)
                print('         Anda berhasil mendaftar! silahkan login         ')
                print('-'*57)
                sleep(2.5)
                signin()
                break
            elif pas != verif:
                print("\n >>> Password anda salah, silahkan masukkan kembali password anda! <<< \n")
                continue

def peminjaman() :
    os.system('cls')
    dp = pd.read_csv('datapeminjaman.csv')

    nopeminjam    = int(input('Masukkan nomor peminjam                   : '))
    judulbuku     = input('Masukkan judul buku                       : ')
    nopanggilbk   = input('Masukkan nomor panggil buku               : ')
    tanggalpinjam = input('Masukkan tanggal pinjam buku (YYYY-MM-DD) : ')
    ubahdt = dt.datetime.strptime(tanggalpinjam, '%Y-%m-%d')
    tgk = ubahdt + dt.timedelta(days=7)
    jatuhtempo = tgk.strftime('%Y-%m-%d')
    tanggalpinjam2 = ubahdt.strftime('%Y-%m-%d')

    dp = pd.read_csv('datapeminjaman.csv')
    try:                 
        if dp.empty: 
            dp = pd.DataFrame(columns=('nomor peminjam', 'judul buku', 'nomor panggil', 'tanggal pinjam',
                                        'tanggal jatuh tempo','tanggal kembali'))
                
    except FileNotFoundError:
        dp = pd.DataFrame(columns=('nomor peminjam', 'judul buku', 'nomor panggil', 'tanggal pinjam',
                                    'tanggal jatuh tempo''tanggal kembali'))
        
    dp.loc[-1] = (nopeminjam, judulbuku, nopanggilbk, tanggalpinjam2, jatuhtempo,'belum kembali')
    dp.to_csv('datapeminjaman.csv', index=False)

    print('=' * 66)
    print(f'||             Tanggal jatuh tempo buku : {tgk.year}-{tgk.month}-{tgk.day}             ||')
    print('=' * 66)
    sleep(1.5)
    print('\n                    << Data berhasil ditambahkan! >>                    ')
    sleep(2)

    while True :
        tanyamenu = input('''\n
______________________
                            
[1]. Tambah data
[2]. Kembali ke menu
______________________                         
>> ''').lower()
            
        if tanyamenu == '1' :
            peminjaman()
            break
        elif tanyamenu == '2' :
            menu()
            break
        else :
            print(f' >>> {tanyamenu} tidak ada di pilihan <<< ')
            sleep(1)
            continue

def pengembalian() :
    os.system('cls')
    dk = pd.read_csv('datapeminjaman.csv')
    
    nopinjam   = int(input('Masukkan nomor peminjam                    : '))
    indeksnp = dk.loc[dk['nomor peminjam'] == nopinjam].index.tolist()
    a = int(indeksnp[0])
    tglpinjam = dk.loc[a, 'tanggal pinjam']
    tglkembali = input('Masukkan tanggal kembali buku (YYYY-MM-DD) : ')
    ftglkembali = dt.datetime.strptime(tglkembali, '%Y-%m-%d') 
    ftglpinjam = dt.datetime.strptime(tglpinjam, '%Y-%m-%d')

    tarif = 500
    selisih = ftglkembali - ftglpinjam
    denda = (selisih.days - 7) * tarif

    if denda > 0 :
        print('='*75)
        print(f'||                   Denda yang dibayarkan : Rp {denda}                     ||')
        print('='*75)
    elif denda <= 0 :
        print('='*77)
        print('||                   Tidak ada denda yang dibayarkan                       ||')
        print('='*77)

    dk.loc[a, 'tanggal kembali'] = tglkembali
    dk.to_csv('datapeminjaman.csv', index=False)
    sleep(0.5)

    while True :
        tanyamenu = input('''
_____________________
                          
[1]. Tambah data
[2]. Kembali ke menu
_____________________                         
>> ''').lower()

        if tanyamenu == '1' :
            pengembalian()
            break
        elif tanyamenu == '2' :
            menu()
            break
        else :
            print(f' >>> {tanyamenu} tidak ada di pilihan <<<')
            sleep(1)
            continue


def pengunjung() :
    os.system('cls') 
    nama      = input('Masukkan nama                : ')
    noanggota = input('Masukkan nomor anggota       : ')
    tanggal   = input('Masukkan tanggal (YYY-MM-DD) : ')
    alamat    = input('Masukkan alamat              : ')

    df = pd.read_csv('datapengunjung.csv')
    try:                 
        if df.empty: 
            df = pd.DataFrame(columns=('nomor anggota', 'nama', 'tanggal', 'alamat'))
            
    except FileNotFoundError:
        df = pd.DataFrame(columns=('nomor anggota', 'nama','tanggal', 'alamat'))
      
    df.loc[-1] = (noanggota, nama, tanggal, alamat)
    df.to_csv('datapengunjung.csv', index=False)
    sleep(1.5)
    print('\n           << Data berhasil ditambahkan! >>           ')
    sleep(2)
    while True :
        tanyamenu = input('''\n
_______________________
                                                    
[1]. Tambah data
[2]. Kembali ke menu
_______________________                          
>> ''').lower()
    
        if tanyamenu == '1' :
            pengunjung()
            break
        elif tanyamenu == '2' :
            menu()
            break
        else :
            print(f' >>> {tanyamenu} tidak ada di pilihan <<< ')   
            continue    
        

def riwayatbuku() : 
    os.system('cls')
    df3 = pd.read_csv('datapeminjaman.csv')

    print('+','-'*121,'+')
    print('|                                                     RIWAYAT PEMINJAMAN                                                    |')
    print('+','-'*121,'+')
    print(tabulate(df3, headers='keys', tablefmt="fancy_grid", showindex=False))
    sleep(0.5)

    tanyamenu = input('\nApakah ingin kembali ke menu? (ya/tidak) : ').lower()
    while True :
        if tanyamenu == 'ya' :
            menu()
            break
        elif tanyamenu == 'tidak' :
            break
    
def riwayatpengunjung() :
    os.system('cls')
    var = pd.read_csv('datapengunjung.csv')
    
    print('+','-'*66,'+')
    print('|                       RIWAYAT PENGUNJUNG                           |')
    print('+','-'*66,'+')
    print(tabulate(var, headers='keys', tablefmt="rounded_grid", showindex=False))
    sleep(0.5)
    
    tanyamenu = input('\nApakah ingin kembali ke menu? (ya/tidak) : ').lower()
    while True :
        if tanyamenu == 'ya' :
            menu()
            break
        elif tanyamenu == 'tidak' :
            break
    
def keluar() :
    os.system('cls')
    tanya = input('Apakah anda yakin ingin keluar dari program? (ya/tidak) : ').lower()
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

[1]. Peminjaman buku
[2]. Pengembalian buku  
[3]. Daftar pengunjung
[4]. Riwayat peminjaman
[5]. Riwayat pengunjung          
[6]. Keluar
""")       
    while True :
        pilihan = input("Pilih menu(1/2/3/4/5/6) : ")
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
        else :
            print(f' >>> {pilihan} tidak ada di pilihan <<< ')
            sleep(2)
            continue
login()


