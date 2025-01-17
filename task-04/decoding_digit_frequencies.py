input_string = input()
numbers = '1234567890'

count_numbers = {str(i):0 for i in range(10) }

for i in input_string:
    if i in numbers:
        count_numbers[i] += 1
result = " ".join(map(str,count_numbers.values()))
print(result)


#this creates a dictionary for all the digits from 0 to 9 and then while iterating
#through the string, it checks for the element being a number and if it is
#it updates the occurance of the element
#at last prints the values in the asked format
