#Grid-Lock

#Grid-Lock

lines = [input() for i in range(10)]

words = [item.strip() for item in input().split(";")]
words.reverse()


def word_length_calc(x):
    x.strip()
    length = 0
    for i in x:
        length += 1
    return length

def string_reversal(x):
    reversed_string = ''
    for i in range(word_length_calc(x)-1,-1,-1):
        reversed_string += x[i]
    return reversed_string

def number_of_spaces(x):
    spaces = 0
    x = string_reversal(x)
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-"
    encountered_spaces = True
    for i in x:
        if i in alphabets:
            spaces += 1
            encountered_spaces = False
        elif i == "+" and not encountered_spaces:
            break
        else:
            continue
    return spaces

def blocks_before_space(y):
    y = string_reversal(y)
    blocks = 0
    for i in y:
        if i == '+':
            blocks += 1
        elif i == "-":
            break
    return blocks


spaces_sizes = [number_of_spaces(i) for i in lines  ]
starting_points = [blocks_before_space(i) for i in lines]
word_lengths = [word_length_calc(i) for i in words]

#print(spaces_sizes)
#print(starting_points)
#print(word_lengths)

for i in spaces_sizes:
    if i in word_lengths:
        word_index = word_lengths.index(i)
        line_index = spaces_sizes.index(i)
        start = (10-word_lengths[word_index] - starting_points[line_index])
        end = start + word_lengths[word_index]
        lines[line_index] =  lines[line_index][: start] + words[word_index] + lines[line_index][end:]
        words.pop(word_index)
        word_lengths.pop(word_index)
#print(lines)
result1 = "\n".join(lines)
#print(result1)



#for vertical placement

grid = [list(line) for line in lines]
transposed_grid = list(zip(*grid))
transposed_lines = [''.join(row) for row in transposed_grid]
#print(transposed_lines)

v_spaces_sizes = [number_of_spaces(i) for i in transposed_lines  ]
v_starting_points = [blocks_before_space(i) for i in transposed_lines]
v_word_lengths = [word_length_calc(i) for i in words]

#print(v_spaces_sizes)
for i in v_spaces_sizes:
    if i in v_word_lengths:
        word_index = v_word_lengths.index(i)
        line_index = v_spaces_sizes.index(i)
        start = (10-word_lengths[word_index] - v_starting_points[line_index])
        end = start + word_lengths[word_index]
        transposed_lines[line_index] = transposed_lines[line_index][:start] +  words[word_index] + transposed_lines[line_index][end:]

grid2 = [list(line) for line in transposed_lines]
reverted_grid = list(zip(*grid2))
reverted_lines = [''.join(row) for row in reverted_grid]
#print(reverted_lines)

result2 = "\n".join(reverted_lines)
print(result2)
