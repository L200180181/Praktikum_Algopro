##Kegiatan 1

Nama = 'Muhammad Azka Nur Lutfi'
NIM = 'L200180181'
TTL = 'Karanganyar, 9 September 1999'
Alamat = 'Jengglong Rt 02 Rw 01 Bejen Karanganyar'
Prodi = 'Informatika'
Hobi = 'Menonton film, jogging, berenang, panahan'
Makanan_yang_disukai = 'Magelangan'
Minuman_yang_disukai = 'Es Degan'
Warna_yang_disukai = 'Merah'
IG = 'ksatrianaga9'

##Kegiatan 2

Nama = 'Muhammad Azka Nur Lutfi'
NIM = 'L200180181'
TTL = 'Karanganyar, 9 September 1999'
Alamat = 'Jengglong Rt 02 Rw 01 Bejen Karanganyar'
Prodi = 'Informatika'
Hobi = 'Menonton film, bersepeda, berenang, panahan'
Makanan_yang_disukai = 'Magelangan'
Minuman_yang_disukai = 'Es Kelapa Muda'
Warna_yang_disukai = 'Merah'
IG = 'ksatrianaga9'

Nama_singkat = Nama[0] + Nama[9] + Nama[14] + Nama[18:23]
Username = Nama [0] + TTL [13] + TTL [25:29]
Password = Nama [0:3] + NIM [7:]

##Kegiatan 3

Nama = 'Muhammad Azka Nur Lutfi'
NIM = 'L200180181'
X = '1' + NIM[7:] # variabel X menyimpan data 1 dan 3 digit terakhir dari NIM saya
a = int(X) # variabel A menyimpan konversi string variabel X ke integer
b = len(Nama) # variabel B menyimpan konversi Variabel X dengan cara menghitung jumlah huruf yang ada didalam kata Nama 
type(a) # menyeleksi objek di variabel a
type(b) # menyeleksi objek di variabel b
a/b # membagi varabel a dengan variabel b
a//b # membagi variabel a dengan variabel b lalu dibulatkan menjadi puluhan
10*(a-999) # mengalikan 10 dengan variabel a yang dikurangi dengan 999
b**2 # mengkuadratkan variabel b
a%b # menghitung hasil sisa pembagian a dengan b
c = 12.5 # 12.5 disimpan di variabel c
type(c) # menyeleksi objek di variabel c 
a/c # membagi variabel a dengan variabel c
a//c # membagi variabel a dengan variabel c lalu dibulatkan menjadi puluhan
a%c # membagi hasil sisa pembagian a dengan c
c>b # mengecek apakah variabel c lebih besar daripada b
type(c > b) # menyeleksi objek apakah variabel c lebih besar daripada b
a > b and b > c # mengecek apakah a lebih besar b dan b lebih besar c merupakan boolean atau decision
a > 1100 or b < 10 # mengecek a lebih besar 1100 atau b lebih kecil dari 10 merupakan boolean atau decision

##Kegiatan 4
Nama = 'Muhammad Azka Nur Lutfi'
NIM = 181
Tinggi = 1.63
Berat = 70
Tahunlahir = 1999
Aku = (Tahunlahir, Berat, Tinggi, NIM, Nama)
Data = [Tahunlahir, Berat, Tinggi, NIM, Nama]
type(Aku) # Memeriksa tipe data dari Aku adalah tuple, karena ditulis dengan kurung biasa dan elemen list tidak dapat diubah
Aku[0] # Menampilkan tahun lahir karena pada Aku indeks ke 0 adalah data dari TahunLahir
a = NIM%4;Aku[a] # Karena sisa hasil bagi dari NIM = 181 dan 4 adalah 70 maka Aku[a] sama dengan Aku[70] yang menampilkan indeks ke 70 adalah data dari NIM
type(Aku[a]) # Memeriksa tipe data dari Aku indeks ke 70 adalah integer, 181 adalah bilangan bulat
Aku[a:4] # a = 70 maka Aku[70:4] adalah menampilkan indeks 70 hingga indeks 4
type(Aku[4]) # Memeriksa tipe data dari Aku indeks ke 4 adalah string, karena indeks ke 4 adalah Nama menyimpan data berupa teks ‘Muhammad Azka Nur Lutfi’
Aku[0]='ok' # Error saat indeks 0 ingin diubah dengan ‘ok’ karena elemen tuple tidak dapat diubah dan proses ini gagal
type(Data) # Memeriksa tipe data dari Aku adalah list, karena ditulis dengan kurung siku dan elemen list dapat diubah
type(Data[4]) # Memeriksa tipe data dari Data indeks ke 4 adalah string, karena indeks ke 4 adalah Nama menyimpan data berupa teks ‘Muhammad Azka Nur Lutfi’
Data[4][5] # Menampilkan huruf ke 5 dari sebuah Data indeks 4
Data[4][a:6] # Menampilkan slicing dari indeks 3 sampai indeks 5 dari sebuah Data indeks 4
Data[0]='ok';Data # Karena elemen list, indeks 0 dapat diubah menjadi string ‘ok’ dan indeks data menjadi ['ok', 70, 1.63, 181, 'Muhammad Azka Nur Lutfi']
Data[-a] # Menampilkan indeks 70 dari belakang karena a = 70 maka Data[-70]
range(a) # Range untuk membuat list baru 0 – 1 karena dengan data a adalah 70

       

