def hitung(alas,tinggi) :
    a=alas
    t=tinggi
    luas=a*t/2
    return luas
alas=6
tinggi = 10

print "<!DOCTYPE html>"
print
print """<html>
<head><title>Luas Bangun Geometri</title></head>
<body>"""
print """<table>
<tr>
    <th rowspan='8' width='150'> GAMBAR </th>
    <td><h3> Bangun Geometri <h3></td>
</tr>
<tr>
    <td>Nama Bangun</td>
    <td>:</td>
    <td>Segitiga</td>
</tr>
<tr>
    <td>Dimensi (2D/3D)</td>
    <td>:</td>
    <td>2d</td>
</tr>
<tr>
    <td>Rumus Luas</td>
    <td>:</td>
    <td>a*t/2</td>
</tr>
<tr>
    <td>Alas</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(alas)
print """<tr>
    <td>Tinggi</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(tinggi)
print """<tr>
    <td>Luas</td>
    <td>:</td>
    <td>{}</td>
</tr>
""".format(hitung(alas,tinggi))
print"""
</table>"""

print"</body></html>"
