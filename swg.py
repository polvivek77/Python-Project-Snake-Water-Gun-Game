import random
snake=1
water=2
gun=3
while True:
    a=random.randint(1,3)
    b=int(input('\nsnake=1, water=2, gun=3\nWhat is your choice?: '))
    print(f'computer choice is: {a}')
    if b==snake:
        if a==snake:
            print('Its a draw')
        elif a==water:
            print('You win')
            break
        elif a==gun:
            print('You loose')
        
    elif b==water:
        if a==snake:
            print('You loose')
        elif a==water:
            print('Its a draw')
        elif a==gun:
            print('You win')
            break
        
    elif b==gun:
        if a==snake:
            print('You win')
            break
        elif a==water:
            print('You loose')
        elif a==gun:
            print('Its a draw')
    
print('Congractulations, You won the game !!')

    