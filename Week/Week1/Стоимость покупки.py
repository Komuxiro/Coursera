A = int(input())  # рубли
B = int(input())  # копейки
N = int(input())  # кол-во пирожков
transfer_rur = A * 100 + B
count_penny = transfer_rur * N
print(count_penny // 100, count_penny % 100)
