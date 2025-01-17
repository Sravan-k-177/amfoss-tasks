def sum_combination(squares, req_number , start=0, combination = [], number_of_combinations = 0):
    if req_number == 0:
        number_of_combinations += 1
        return number_of_combinations
    for i in range(start, len(squares)):
        if squares[i] > req_number:
            continue
        combination.append(squares[i])
        number_of_combinations = sum_combination(squares, req_number - squares[i], i + 1, combination, number_of_combinations)
        combination.pop()
    return number_of_combinations

req_number = int((input()))
power = int(input())

sqaures = []

for i in range(1, int(req_number ** (1/power)) + 2):
    sqaures.append(i**power)

combination_count = sum_combination(sqaures, req_number, 0, [], 0)

print(combination_count)
#print(sqaures)


#for this question i used a similar logic as two sum question in leet code
#i used a recursion funciton so that it checks for all the permutations 
#first the powers of natural numbers are produces from 1 till the number below which exceeds the requrired sum
#i used +2 because due to approximations when it it typecasted as int, i sometimes returns a number lower than expected, so i used +2
#it now checks for all the permutations which could work and keeps a track of them
#finally returns the count
