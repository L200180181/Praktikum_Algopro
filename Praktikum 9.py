# PRAKTIKUM 9
# MUHAMMAD AZLA NUR LUTFI
# L200180181
# D

# Kegiatan 1
a = open("L200180181","w")
a.write("L200180181\n")
a.write("09-09-1999\n")
a.write("Muhammad Azka Nur Lutfi\n")
a.write("Karanganyar")
a.close()

# Kegiatan 2,3&4

import shelve

a = open("L200180181","r")

b = shelve.open("Praktikum 9.data")
b["Data"] = a.read()
b.close

a.close()

b = shelve.open("Praktikum 9.data")
print(b["Data"])
b.close()
