n = int(input())
elements_of_a = [int(item.strip()) for item in input().split()]

n = int(input())
elements_of_b = [int(item.strip()) for item in input().split()]

count_elements_a = {}
count_elements_b ={}

for i in elements_of_a:
    if i in count_elements_a:
        count_elements_a[i] += 1
    else:
        count_elements_a[i] = 1

for i in elements_of_b:
    if i in count_elements_b:
        count_elements_b[i] += 1
    else:
        count_elements_b[i] = 1

    if i not in count_elements_a:
        count_elements_a[i] = 0

req_elements = []

for i in count_elements_b:
    if count_elements_b[i] > count_elements_a[i]:
        req_elements.append(i)

req_elements = sorted(req_elements)

result = " ".join(map(str, req_elements))
print(result)
