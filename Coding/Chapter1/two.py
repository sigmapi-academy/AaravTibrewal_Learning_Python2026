# Display the appropriate message as per the color of signal at the road crossing. 
signal = input('Enter the colour: ')
if signal == 'red' or signal == "RED":
    print('Stop')
elif signal == 'orange' or signal =="ORANGE":
    print("Be slow")
elif signal == 'green' or signal =='GREEN':
    print('Go!')