group_size = int(input())
room_numbers = [int(item.strip()) for item in input().split()]

count_kosam = {}


for i in room_numbers:
    if i in count_kosam:
        count_kosam[i] += 1
    else:
        count_kosam[i] = 1

for i in count_kosam:
    if count_kosam[i] == 1:
        print(i)
        break
