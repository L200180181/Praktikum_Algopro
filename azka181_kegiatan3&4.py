Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## Kegiatan 3
>>> Nama = 'Muhammad Azka Nur Lutfi'
>>> NIM = 'L200180181'
>>> X = '1' + NIM[7:] # variabel X menyimpan data 1 dan 3 digit terakhir dari NIM saya
>>> a = int(X) # variabel A menyimpan konversi string variabel X ke integer
>>> b = len(Nama) # variabel B menyimpan konversi Variabel X dengan cara menghitung jumlah huruf yang ada didalam kata Nama
>>> type(a) # menyeleksi objek di variabel a
<class 'int'>
>>> type(b) # menyeleksi objek di variabel b
<class 'int'>
>>> a/b # membagi varabel a dengan variabel b
51.34782608695652
>>> a//b # membagi variabel a dengan variabel b lalu dibulatkan menjadi puluhan
51
>>> 10*(a-999) # mengalikan 10 dengan variabel a yang dikurangi dengan 999
1820
>>> b**2 # mengkuadratkan variabel b
529
>>> a%b # menghitung hasil sisa pembagian a dengan b
8
>>> c = 12.5 # 12.5 disimpan di variabel c
>>> type(c) # menyeleksi objek di variabel c
<class 'float'>
>>> a/c # membagi variabel a dengan variabel c
94.48
>>> a//c # membagi variabel a dengan variabel c lalu dibulatkan menjadi puluhan
94.0
>>> a%c # membagi hasil sisa pembagian a dengan c
6.0
>>> c>b # mengecek apakah variabel c lebih besar daripada b
False
>>> type(c > b) # menyeleksi objek apakah variabel c lebih besar daripada b
<class 'bool'>
>>> a > b and b > c # mengecek apakah a lebih besar b dan b lebih besar c merupakan boolean atau decision
True
>>> a > 1100 or b < 10 # mengecek a lebih besar 1100 atau b lebih kecil dari 10 merupakan boolean atau decision
True
>>> 
>>> ##Kegiatan 4
>>> Nama = 'Muhammad Azka Nur Lutfi'
>>> NIM = 181
>>> 
>>> Tinggi = 1.63
>>> Berat = 70
>>> Tahunlahir = 1999
>>> Aku = (Tahunlahir, Berat, Tinggi, NIM, Nama)
>>> Data = [Tahunlahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku) # Memeriksa tipe data dari Aku adalah tuple, karena ditulis dengan kurung biasa dan elemen list tidak dapat diubah
<class 'tuple'>
>>> Aku[0] # Menampilkan tahun lahir karena pada Aku indeks ke 0 adalah data dari TahunLahir
1999
>>> a = NIM%4;Aku[a] # Karena sisa hasil bagi dari NIM = 181 dan 4 adalah 70 maka Aku[a] sama dengan Aku[70] yang menampilkan indeks ke 70 adalah data dari NIM
70
>>> type(Aku[a]) # Memeriksa tipe data dari Aku indeks ke 70 adalah integer, 181 adalah bilangan bulat
<class 'int'>
>>> Aku[a:4] # a = 70 maka Aku[70:4] adalah menampilkan indeks 70 hingga indeks 4
(70, 1.63, 181)
>>> type(Aku[4]) # Memeriksa tipe data dari Aku indeks ke 4 adalah string, karena indeks ke 4 adalah Nama menyimpan data berupa teks ‘Muhammad Azka Nur Lutfi’
<class 'str'>
>>> Aku[0]='ok' # Error saat indeks 0 ingin diubah dengan ‘ok’ karena elemen tuple tidak dapat diubah dan proses ini gagal
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    Aku[0]='ok' # Error saat indeks 0 ingin diubah dengan ‘ok’ karena elemen tuple tidak dapat diubah dan proses ini gagal
TypeError: 'tuple' object does not support item assignment
>>> type(Data) # Memeriksa tipe data dari Aku adalah list, karena ditulis dengan kurung siku dan elemen list dapat diubah
<class 'list'>
>>> type(Data[4]) # Memeriksa tipe data dari Data indeks ke 4 adalah string, karena indeks ke 4 adalah Nama menyimpan data berupa teks ‘Muhammad Azka Nur Lutfi’
<class 'str'>
>>> Data[4][5] # Menampilkan huruf ke 5 dari sebuah Data indeks 4
'm'
>>> Data[4][a:6] # Menampilkan slicing dari indeks 3 sampai indeks 5 dari sebuah Data indeks 4
'uhamm'
>>> Data[0]='ok';Data # Karena elemen list, indeks 0 dapat diubah menjadi string ‘ok’ dan indeks data menjadi ['ok', 70, 1.63, 181, 'Muhammad Azka Nur Lutfi']
['ok', 70, 1.63, 181, 'Muhammad Azka Nur Lutfi']
>>> Data[-a] # Menampilkan indeks 70 dari belakang karena a = 70 maka Data[-70]
'Muhammad Azka Nur Lutfi'
>>> range(a) # Range untuk membuat list baru 0 – 1 karena dengan data a adalah 70
range(0, 1)
>>> 
