import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50004))
s.listen(5)
print ("Server komunikasi tentang data sudah siap")
data = ''
kamus = {'nama':'Muhammad Azka Nur Lutfi','NIM':'L200180181','angkatan':'2018'}
while data.lower() !='keluar':
    komm, addr = s.accept()
    while data.lower() !='keluar':
        data = komm.recv(1024)
        if data.lower() == 'keluar':
            s.close()
            break
        print ('Perintah:',data)
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('Maaf, perintah tidak dimengerti')
