group_size = int(input())
room_numbers = [int(item.strip()) for item in input().split()]

number_of_people = len(room_numbers)

for i in set(room_numbers):
    if i > number_of_people//group_size:
        print(i)
        break


#assuming a pattern to be always exixtant        
#since the room number of captain is more than the hightest room number of others
#this returns thee number which is higher than the room numbers which were alloted to passangers
#the room numbers list could be sorted and the last element be returned, but the group size is given, so i tried to use it
