group_size = int(input())
room_numbers = [int(item.strip()) for item in input().split()]

number_of_people = len(room_numbers)

for i in set(room_numbers):
    if i > number_of_people//group_size:
        print(i)
        break
