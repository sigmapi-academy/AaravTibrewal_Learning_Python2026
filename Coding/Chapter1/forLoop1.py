vowels='aeiouAEIOU'
name = input('Enter any name: ')
count = 0
for char in name:  
    if char in vowels:
        count += 1
print(f'Number of vowels: {count}')