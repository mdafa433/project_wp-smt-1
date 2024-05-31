from datetime import datetime


def penjualan():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n")
    print("-" * 60)
    print("\n")
    print("MENU LIST NAKAMA COFFEE".center(60),"\n")
    print("\tKode".ljust(9), "Menu List".ljust(22),"Price".ljust(30))
    print("\t1\t","Blonde Cafe Latte","\t40.000")
    print("\t2\t","Caramel Machiato","\t35.000")
    print("\t3\t","Skinny Macha","\t\t35.000")
    print("\t4\t","Irish Coffe","\t\t40.000")
    print("\t5\t","Iced Latte","\t\t30.000")
    print("\t6\t","Cafe Americano","\t30.000")
    print("\t7\t","Cappucino","\t\t30.000")
    print("\t8\t","Cloud Machiato","\t35.000")
    print("\t9\t","Creamy Iced","\t\t35.000")
    print("\t10\t","Caffe Latte","\t\t35.000")
    print("-" * 60)

    jumlahpesan = []
    listnama = []
    harga = []
    diskon = []
    totalharga = []

    banyak_macam = int(input("Berapa Macam Kopi Yang Dipesan = "))
    print("\n")
    i = 0
    a = 0
    total_bayar = 0
    while i < banyak_macam:
        pesan = str(input("Masukan Kode Pesanan = "))
        jumlahpesan.append(int(input("Masukkan Jumlah Pesanan = ")))

        print("-" * 60)

        if pesan == "1":
            listnama.append("Blonde Cafe Latte")
            harga.append(int(40000))
            diskon.append(0)
            totalharga.append(int((harga[i]*jumlahpesan[i])))
        elif pesan == "2":
            listnama.append("Caramel Machiato")
            harga.append(int(35000))
            diskon.append(0)
            totalharga.append(int((harga[i]*jumlahpesan[i])))
        elif pesan == "3":
            listnama.append("Skinny Macha")
            harga.append(int(35000))
            diskon.append(0)
            totalharga.append(int((harga[i]*jumlahpesan[i])))
        elif pesan == "4":
            listnama.append("Irish Coffe")
            harga.append(int(40000))
            diskon.append(0)
            totalharga.append(int((harga[i]*jumlahpesan[i])))
        elif pesan == "5":
            listnama.append("Iced Coffe")
            harga.append(int(30000))
            diskon.append(0)
            totalharga.append(int((harga[i]*jumlahpesan[i])))
        elif pesan == "6":
            listnama.append("Cafe Americano")
            harga.append(int(30000))
            diskon.append(0)
            totalharga.append(int((harga[i]*jumlahpesan[i])))
        elif pesan == "7":
            listnama.append("Cappucino")
            harga.append(int(30000))
            diskon.append(0)
            totalharga.append(int((harga[i]*jumlahpesan[i])))
        elif pesan == "8":
            listnama.append("Cloud Machiato")
            harga.append(int(35000))
            diskon.append(0)
            totalharga.append(int((harga[i]*jumlahpesan[i])))
        elif pesan == "9":
            listnama.append("Creamy Iced")
            harga.append(int(35000))
            diskon.append(0)
            totalharga.append(int((harga[i]*jumlahpesan[i])))
        elif pesan == "10":
            listnama.append("Caffe Latte")
            harga.append(int(35000))
            diskon.append(0)
            totalharga.append(int((harga[i]*jumlahpesan[i])))
        else:
            listnama = "-"
            harga = "-"
            diskon = "-"
            totalharga = "-"
            pilihan = input(
            "Menu Tidak Tersedia \nPress 'Enter' untuk mengulang kembali \n")
            penjualan()
        i += 1
    
    print("-------------------------------------------------".center(60))
    print("Nakama Coffee".center(60))
    print(dt_string.center(60))
    print("-------------------------------------------------".center(60))
    print("".ljust(5),"%s   %s  %s  %s  %s" % ("No".ljust(1),"List Order".ljust(17),"Price".ljust(8),"QTY".ljust(6),"Total"))
    while a < banyak_macam:
        total_bayar += totalharga[a]
        print("".ljust(5),"%i   %s  %i      %i      %i" % (a+1,listnama[a].ljust(18),harga[a],jumlahpesan[a],totalharga[a]))
        a += 1
    print("_________________________________________________".center(60))
    ppn = total_bayar * 0.03
    total_pembayaran = total_bayar + ppn
    print("".rjust(27),"Jumlah Bayar  Rp. ",total_bayar)
    print("".rjust(27),"PPN           Rp. ",ppn)
    print("".rjust(27),"              ____________+")
    print("".rjust(27),"Total Bayar   Rp. ",total_pembayaran)
    print("-------------------------------------------------".center(60))
    print("\n")
    tanya()

def main_menu():
    print('Selamat Datang Di Program Penjualan'.center(60,"-"),"\n")
    print("List Layanan Penjualan".center(60),"\n")
    print('1. Program Hitung Penjualan')
    print('2. Exit Program')

    pilihan = input('\n Pilih Menu Layanan = ')

    if pilihan == '1':
        penjualan()
    elif pilihan == '2':
        print("\n",'Terima Kasih Dan Sampai Berjumpa Kembali!'.center(60),"\n")
        exit()


def login():
    print('-' * 60)
    print('LOGIN PENJUALAN'.center(60), "\n")
    username = input('Masukan Username Anda = ')
    print("\n")
    if username == 'Rafi' or username == "RAFI" or username == "rafi":
        password = input("Masukkan Password Anda = ")
        if password == "19220988":
            print("\n")
            print('Login Sukses!'.center(60),"\n")
            main_menu()
        else:
            print("\n")
            print("Password Anda Salah!".center(60),"\n")
            login()
    elif username == 'Dafa' or username == "DAFA" or username == "dafa":
        password = input("Masukkan Password Anda = ")
        if password == "19221128":
            print("\n")
            print('Login Sukses!'.center(60),"\n")
            main_menu()
        else:
            print("\n")
            print("Password Anda Salah!".center(60),"\n")
            login()
    if username == 'Rayya' or username == "RAYYA" or username =="rayya":
        password = input("Masukkan Password Anda = ")
        if password == "19221038":
            print("\n")
            print('Login Sukses!'.center(60),"\n")
            main_menu()
        else:
            print("\n")
            print("Password Anda Salah!".center(60),"\n")
            login()
    elif username == 'Andika' or username == "ANDIKA" or username == "andika":
        password = input("Masukkan Password Anda = ")
        if password == "19221479":
            print("\n")
            print('Login Sukses!'.center(60),"\n")
            main_menu()
        else:
            print("\n")
            print("Password Anda Salah!".center(60),"\n")
            login()
    elif username == 'Restian' or username == "RESTIAN" or username == "restian":
        password = input("Masukkan Password Anda = ")
        if password == "19220804":
            print("\n")
            print('Login Sukses!'.center(60),"\n")
            main_menu()
        else:
            print("\n")
            print("Password Anda Salah!".center(60),"\n")
            login()
    else:
        print("Data Tidak Ditemukan!".center(60))
        login()

def tanya():
    tanya = input('Kembali Memesan..? (Y/N) : ')
    if tanya == 'y' or tanya == 'Y':
        print("\n")
        penjualan()
    elif tanya == 'n'or tanya == 'N':
        print("\n")
        main_menu()
    else:
        print('Input Salah')
        print('Masukan Input Dengan Denar')
        tanya()

login()
main_menu()
penjualan()
tanya()