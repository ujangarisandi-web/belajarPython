# for i in range(10, 40, 5):
#     print(i)

number = 50

for j in range(0, 40):
    print(j)
    if j is number:
        print('angka ditemukan', j)
        break
else:
    print('angka tidak ditemukan')

print('space diluar for')

# else untuk mamastikan sudah sampai di looping akhir
# for k in range(0, 5):
#     print(k)
# else:
#     print('hello')