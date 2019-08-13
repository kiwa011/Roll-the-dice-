import random 
decision = raw_input ( "do you want to roll the dice: ")
while decision != 'no':
    print random.randint(1,6)
    decision = raw_input ( "do you want to role the dice: ")