import random
user_count = 0
computer_count = 0
options = ['rock', 'paper', 'scissor']

while True:
    ans = input('Type rock or paper or scissor ').lower()
    if ans == 'q':
        break
    if ans not in options:
        print('Type with correct spelling.')
        continue

    random_numbers = random.randint(0, 2)
    computer_picks = options[random_numbers]
    print('Computer picked', computer_picks+'.')

    if ans == 'rock' and computer_picks == 'scissor':
        print('You won!!')
        user_count += 1
    elif ans == 'paper' and computer_picks == 'rock':
        print('You won!!')
        user_count += 1
    elif ans == 'scissor' and computer_picks == 'paper':
        print('You won!!')
        user_count += 1
    else:
        print('You lose')
        computer_count += 1
print('/n')
print('You won it', user_count, 'times.')
print('Computer won it', computer_count, 'times.')
print('Goodbye')

