# menghasilkan 1,2,3,4,5,6,7,8,9,10 lalu mencetak "num sudah mencapai 10"
num=1
while(num<=10):
    print(num)
    num +=1
else:
    print("num sudah mencapai %d" %(num))
# Prints out 1,2,3,4,5,6,7,8,9,10,11,12,13,14
for i in range(1, 15):
    if(i%15==0):
        break
    print(i)
else:
    print("ini tidak akan dicetak karena perulangan dihentikan oleh break bukan karena kesalahan kondisi")