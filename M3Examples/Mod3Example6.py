print(f'{"Num":<7}{"Sqr"}')
print('-'*14)

numbers = [5,6,7,8,9,10]

squares = []

for num in numbers:
    sqr = num**2 
    squares.append(sqr)
    print(f'{num:<7}{sqr}')
