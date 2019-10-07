# list sebagai iterable
# gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']

# for g in gorengan:
#     print(g)
#     print(len(g))

# list sebagai iterable
# bakwan = 'bakwan'

# for i in bakwan:
#     print(i)

# for didalam for

gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']
buah = ['semangka', 'jeruk', 'aple', 'anggur']
sayur = ['kangkung', 'wortel', 'tomat', 'kentang']

daftar_belanja = [gorengan, buah, sayur]

# print(daftar_belanja)

for subdaftarBelanja in daftar_belanja:
    print(subdaftarBelanja)
    for komponen in subdaftarBelanja:
        print(komponen)