import time

#ALTERNATIVE 1
#print('THIS IS A GAME')
#for n in range(3,0,-1):
#    print('Loading.')
#    print('Loading..')
#    print('Loading...')
#print('Welcome to the game!')

#ALTERNATIVE 2
print('THIS IS A GAME')
for x in range(3,0,-1):
    for n in range(0,4):
        time.sleep(1)
        print(f'Loading {"."*n}')
print("LET'S START!")
    
    





