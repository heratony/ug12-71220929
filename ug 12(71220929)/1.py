a = int(input("masukkan awal deret: "))
b = int(input("masukkan akhir deret: "))

jumlah = 0
for count in range (a,b):
    if count%6 != 0 and count %3 != 0 and count %2 == 1:
        print(count, end=" ")
    
