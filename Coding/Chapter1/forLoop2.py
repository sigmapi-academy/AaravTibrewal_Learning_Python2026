import random as R

li = [item for item in range(R.randint(1,10), R.randint(20, 40), R.randint(1, 6))]

countE = 0
countO = 0

for var in li:
    if var % 2 == 0:
        countE += 1
    else:
        countO += 1
    print(var, end=' ')
        
print(f'\nCount of even numbers: {countE}')
print(f'Count of odd numbers: {countO}')
