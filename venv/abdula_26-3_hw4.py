data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
del numbers[0]
letters[-1] = 'G'
letters[1] = 'c'
letters.append(True)
letters[-1], letters[0] = letters[0] , letters[-1]
letters[1], letters[7] = letters [7] , letters[1]
letters[3], letters[5] = letters[5], letters[3]
del numbers[0]
del numbers[0]
numbers.append(4)
numbers.append(9)

print(tuple(letters))
print(tuple(numbers))