#PRAKTIKUM 8
#MUHAMMAD AZKA NUR LUTFI
#L200180181
#KELAS D

#Kegiatan 1 Membuat Modul
#1
a={'NIM':'L200180181','Nama':'Muhammad Azka Nur Lutfi','Alamat':'Karanganyar Regency','Perguruan Tinggi':'Universitas Muhammadiyah Surakarta','Fakultas':'Komunikasi dan Informatika','Prodi':'Informatika','Kelas':'D'}
print("Nama : "+a['Nama'])
print("NIM : "+a['NIM'])
print("Alamat : "+a['Alamat'])
print("Perguruan Tinggi : "+a['Perguruan Tinggi'])
print("Fakultas : "+a['Fakultas'])
print("Prodi : "+a['Prodi'])
print("Kelas : "+a['Kelas'])

#2
a={'NIM':'L200180181','Nama':'Muhammad Azka Nur Lutfi','Alamat':'Karanganyar','Kodepos':'57716','TTL':'Karanganyar 9 September 1999','Tinggi badan':'163','Berat badan':'70'}
b="""Pilihan yang tersedia:
b menampilkan bantuan ini
N menampilkan NIM
n menampilkan Nama
A menampilkan Alamat
K menampilkan kodepos
T menampilkan Tanggal lahir
t menampilkan Tinggi badan
B menampilkan Berat badan
k keluar\n"""
def nim():
    print 'NIM: '+x['NIM']
def nama():
    print 'Nama: '+x['Nama']
def alamat():
    print 'Alamat: '+x['Alamat']
def kodepos():
    print 'Kodepos: '+x['Kodepos']
def tlahir():
    print 'TTL: '+x['TTL']
def tbadan():
    print 'Tinggi badan: '+x['Tinggi badan']
def bbadan():
    print 'Berat badan: '+x['Berat badan']
key = ('b', 'N', 'n', 'A', 'K', 'T', 't', 'B', 'k')
print b
data = raw_input("Pilihan saudara: ")
while data != 'k':
    if data == 'b':
        print b
        data = raw_input("Pilihan saudara: ")
    elif data == 'N':
        nim ()
        data = raw_input("Pilihan saudara: ")
    elif data == 'n':
        nama ()
        data = raw_input("Pilihan saudara: ")
    elif data == 'A':
        alamat ()
        data = raw_input("Pilihan saudara: ")
    elif data == 'K':
        kodepos ()
        data = raw_input("Pilihan saudara: ")
    elif data == 'T':
        tlahir ()
        data = raw_input("Pilihan saudara: ")
    elif data == 't':
        tbadan ()
        data = raw_input("Pilihan saudara: ")
    elif data == 'B':
        bbadan ()
        data = raw_input("Pilihan saudara: ")
    elif data != key:
        print "perintah tidak dikenal"
        data = raw_input("Pilihan saudara: ")
else:
        print "Terima Kasih"

#Kegiatan 2 Membuat Fungsi
def konversiSuhu(C = 0, F = 0):
    "Fungsi mengkonversikan Celcius ke Fahrenheit atau sebaliknya"
    if C != 0:
        y = ((9*C/5) + 32)
        print("Suhu", C, "Celcius setara dengan", y, "Fahrenheit")
    elif F != 0:
        b = ((F-32) * 5/9)
        print("Suhu", F, "Celcius setara dengan", b, "Celcius")
    else:
        print("Suhu 0 Celcius setara dengan 32 Fahrenheit")
    return;

        
