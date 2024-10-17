squares = [i ** 2 for i in range(5)]
print(squares)

squares = (i ** 2 for i in range(5))
print(squares)
print(type(squares))

for i in squares:
    print(i)
print('Done')

for i in squares:
    print(i)
print('Done')

squares = (i ** 2 for i in range(5))
for i in squares:
    print(i)
print('Done')
print('='*30)

squares = (i ** 2 for i in range(5))
print(iter(squares) is squares)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
#print(next(squares))
print('Done')

squares = (i ** 2 for i in range(5))
print(3 in squares)
print(list(squares))
print(4 in squares)

squares = (i ** 2 for i in range(5))
print(4 in squares)
print(list(squares))

