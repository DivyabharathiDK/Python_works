#USECASE 1
#Select the most suitable transportation option based on available money and ticket prices.
#Pseudo code:
#check whether amount wallet is greater than f/t/b?
#if above is true, then check which means of transportation is lesser cost


wallet=1000
flight=6000
train=5000
bus=2000
if wallet>=flight or wallet>=train or wallet>=bus:
    print('Iam ready for Travel')
    if flight<=train or flight<=bus:
        print('Travel via Flight')
    elif train<flight and train <=bus:
        print('Travel via Train')
    else:
        print('Travel via bus')
else:
    print('No money to Travel')
