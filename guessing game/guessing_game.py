import random

def play():
    print('********************************')
    print('*Welcome to the  Guessing Game!*')
    print('********************************')
    
    secret_number = random.randrange(1,101)
    points = 1000
    
    print('Set the difficulty level.')
    print('(1) Easy, (2) Medium, (3) Hard')
    
    level = int(input('\nSet the level: '))
    
    if(level == 1):
        num_retries = 20
    elif(level == 2):
        num_retries = 10
    else:
        num_retries = 5
    
    for round_played in range(1, num_retries + 1) :
        print('Attempt {} of {}.'.format(round_played, num_retries))
        
        guess_str = input('Write a number between 1 and 100: ')
        guess = int(guess_str)
        
        if(guess < 1 or guess > 100):
            print('You should write an number between 1 and 100.')
            continue
    
        hit = guess == secret_number
        greater = guess > secret_number
        less = guess < secret_number
        
        if(hit):
            print('You hit and made {} points!'.format(points))
            break
        else:
            if(greater):
                print('Wrong! It was greater than the secret number.')
            elif(less):
                print('Wrong! It was less than the secret number.')
        
        lost_points = abs(secret_number - guess)
        points = points - lost_points
    
        if(round_played == num_retries):
            print('The secret number was: ', secret_number)
    
    print('End of the game.')

if(__name__ == '__main__'):
    play()
