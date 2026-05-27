start = int(input('Enter the start value: '))
stop =  int(input('Enter the stop value: '))
while start <= stop:
    print(start)
    start += 1
    if start == stop: #if this condition is true then else part will not work
        break
else:
    print('Loop ends')