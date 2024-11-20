list_values = [1, 2, 3, 4, 5]


# normal for
squared_values2 = []
for i in list_values:
    squared_values2.append(i**2)
print(squared_values2)


# list comprehension
squared_values = [i**2 for i in list_values]
print(squared_values)

short_values = [i**2 for i in range(1, 6) if i % 2 == 1]
print(short_values)
