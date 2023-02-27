#Containers for tallies and tokens
briantoken = []
kaylatoken = []
briantally = ['I','I','I','I','I']
Kaylatally = []

#funtions adds a tally/token to a users container based on how they answer the CLI prompts

def addbriantally():
    briantally.append('I')
    print(f'nice work brian, you now have {len(briantally)} tallys!')

def addkaylatally():
        Kaylatally.append('I')
        print(f'nice work kayla, you now have {len(Kaylatally)} tallys!')
#Checks if there are more than 5 tallys in the container, 
#if there are this program removes 5 and adds 1 token to the token list    
def addbriantoken():
    print('Checking for tokens please wait...')
    if len(briantally) >= 5:
        briantally.remove('I')
        briantally.remove('I')
        briantally.remove('I')
        briantally.remove('I')
        briantally.remove('I')
        briantoken.append('I')
        print(f'congrats brian you have {len(briantally)} tallies, and {len(briantoken)} tokens!')
    else:
        print('no tokens to add')
def addkaylatoken():
    print('Checking for tokens please wait...')
    if len(Kaylatally) >= 5:
        Kaylatally.remove('I')
        Kaylatally.remove('I')
        Kaylatally.remove('I')
        Kaylatally.remove('I')
        Kaylatally.remove('I')
        kaylatoken.append('I')
        print(f'congrats kayla you have {len(Kaylatally)} tallies, and {len(kaylatoken)} tokens!')
    else:
        print('no tokens to add')

#Main program that branches into other functions. 
#Uses CLI to guide user through a basic menu to add tallys or convert to tokens
def program():
        answer = input('hello, whos account would you like to work with? brian or kayla?')
        if answer == 'brian':
            answer2 = input('Hi brian, would you like to add a tally or cash in a token? (tally/cash-in)')
            if answer2 == 'tally':
                addbriantally()
            elif answer2 == 'cash-in':
                addbriantoken()
            else:
                program()
        elif answer == 'kayla':
            answer2 = input('Hi kayla, would you like to add a tally or cash in a token? (tally/cash-in)')
            if answer2 == 'tally':
                addkaylatally()
            elif answer2 == 'cash-in':
                addkaylatoken()
            else:
                program()       
        else:
            print('have a good day!')   

#Runs program infinitely so it is able to keep track and return user to main menu
while True:
    program() 