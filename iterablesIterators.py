l = [1,2,3]

iterator = iter(l)
print(type(iterator))
print(id(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))
print('DONE')

iterator = iter(l)
print(type(iterator))
print(id(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))
print('DONE')
print('='*30)
l = [1,2,3,4,5]
for element in l:
    print(element)

# iterator = iter(l)
# while True:
#     element = next(iterator)
#     print(element)

iterator = iter(l)
try:
    while True:
        element = next(iterator)
        print(element)
except StopIteration:
    print('Done iterating...')
    pass

r = range(10)
print(r)

r_iter = iter(r)
print(next(r_iter))
print(next(r_iter))
print(next(r_iter))
print(list(r_iter))

for i in range(100_000_000):
    print(i)
    if i > 4:
        break

from time import perf_counter
start = perf_counter()
l = range(10_000_000)
end = perf_counter()
print(f'elapsed: {end - start}')


start = perf_counter()
l = list(range(10_000_000))
end = perf_counter()
print(f'elapsed: {end - start}')

del l

r = range(10)
print(list(r))
print(list(r))

enum = enumerate('abc')
print(next(enum))
print(list(enum))
print(list(enum))
#print(next(enum))
print(list(enumerate('abc')))

print(iter(enum) is enum)


















