input_string = input()
numbers = '1234567890'

count_numbers = {str(i):0 for i in range(10) }

for i in input_string:
    if i in numbers:
        count_numbers[i] += 1
result = " ".join(map(str,count_numbers.values()))
print(result)
