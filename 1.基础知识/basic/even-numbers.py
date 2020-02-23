
even = list(range(2, 11, 3))
print(even)


squares = []

for val in range(1, 11):
    square = val**2
    squares.append(square)

print(squares)

print(min(squares)) 
print(max(squares)) 
print(sum(squares) / len(squares)) 

squares = [value**3 for value in range(1, 11)]

print(squares)