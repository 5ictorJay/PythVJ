import random

print('DICE ROLL SIMULATOR')
print('\n------------------')

def dadu():
    dadu= random.randint(1,6)
    return dadu

while True:
    roll=input('Roll the dice? (y/n)'
    if roll == 'y':
        print(f'You have rolled: {dadu}')
    else:
        break
