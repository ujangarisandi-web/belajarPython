nilai = 50

if nilai == 75:  #equal eksplisit
    print('nilai anda', nilai)

if nilai is 60:  #equal
    print('nilai anda', nilai)
if nilai is not 60:  #not equal
    print('nilai anda bukan : 60')
print(50 * '=')
nilai = 60
if 80 <= nilai <= 100:
    print('nilai anda adalah A')
elif 70 <= nilai < 80:
    print('nilai anda adalah B')
elif 60 <= nilai < 70:
    print('nilai anda adalah C')
elif 50 <= nilai < 60:
    print('nilai anda adalah T, lakukan pebaikan')
else:
    print('maaf anda tidak lulus matakuliah ini')

print(50 * '=')
print('operator logika untuk list dan string')
print(' ')

gorengan = [
    'bakwan', 'cireng', 'bala-bala', 'gehu', 'combro', 'pisang goreng',
    'pukis', 'risoles'
]
beli = 'bandros'

if beli in gorengan:
    print('Mamang bilang, "ya, saya jual', beli, '"')
if not beli in gorengan:
    print('"saya gak jual', beli, '"')

print(50 * '=')

karakter = 'z'
if karakter in beli:
    print('ada', karakter, 'di', beli)
else:
    print('tidak ada', karakter, 'di', beli)
