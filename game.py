game_running = True

while game_running:
    new_round = True

# Beginning of game
    print('___' * 7)
    print('Select Your Fighter')
    print('---' * 7)
    print('1) Old Man Jenkins')
    print('2) Whoopie Goldberg')
    print('3) Papa Smurf')
    print('4) Nicholas Cage')

# Player Selection
    player_fighter = input()
    if player_fighter == '1':
        player = {'name': 'Old Man Jenkins', 'attack': 10,
                  'heal': 16, 'health': 100}
    elif player_fighter == '2':
        player = {'name': 'Whoopie Goldberg', 'attack': 5,
                  'heal': 20, 'health': 100}
    elif player_fighter == '3':
        player = {'name': 'Papa Smurf', 'attack': 20,
                  'heal': 5, 'health': 80}
    elif player_fighter == '4':
        player = {'name': 'Nicholas Cage', 'attack': 8,
                  'heal': 5, 'health': 120}
    else:
        print('---' * 7)
        print('Selection invalid, you are now a paper bag')
        print('---' * 7)
        player = {'name': 'Paper Bag', 'attack': 0,
                  'heal': 0, 'health': 50}

# Monster Selected automatically
    if player_fighter == '1':
        monster = {'name': 'Young Kids', 'attack': 15,
                   'health': 100}
    elif player_fighter == '2':
        monster = {'name': 'Oprah Winfrey', 'attack': 10,
                   'health': 100}
    elif player_fighter == '3':
        monster = {'name': 'Smurfette', 'attack': 25,
                   'health': 80}
    elif player_fighter == '4':
        monster = {'name': 'The Declaration of Independence', 'attack': 13,
                   'health': 120}
    else:
        monster = {'name': 'God', 'attack': 100,
                   'health': 1000}

# Newly Defined Names
    hero = player['name']
    monster_name = monster['name']

# Greeting Message
    print('___' * 7)
    print(
        f'Welcome {hero}! You are challenging {monster_name}! Your Stats are: {player} and your opponents are {monster}')
    print('---' * 7)

# While Loop To Reset Game
    while new_round == True:
        player_won = False
        monster_won = False

# Action Selector
        print('___' * 7)
        print('Please Select an Action!')
        print('---' * 7)
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')

        player_choice = input()

# Attack Result
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - monster['attack']
                if player['health'] <= 0:
                    monster_won = True
            print('Your health is now: ')
            print('___' * 7)
            print(player['health'])
            print('---' * 7)
            print('___' * 7)
            print(f'{monster_name}s health is now: ')
            print('---' * 7)
            print(monster['health'])

# Heal results
        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']
            player['health'] = player['health'] + monster['attack']
            print('___' * 7)
            print(f'{hero} successfully healed')
            print('---' * 7)
            print(
                f'After the healing and {monster_name}s attack your health is now')
            print('---' * 7)
            print(player['health'])

# Exit Game Result
        elif player_choice == '3':
            new_round = False
            game_running = False
            print('___' * 7)
            print('Exited Game')
            print('___' * 7)
        else:
            print('___' * 7)
            print('Invalid Command')
            print('___' * 7)

# Win Conditions
        if player_won == True or monster_won == True:
            if monster_won == True:
                print('___' * 7)
                print(
                    f'You Suck! {hero} has been defeated by the great {monster_name}')
                print('---' * 7)
            elif player_won:
                print('___' * 7)
                print(f'You won! {hero} has defeated {monster_name}')
                print('---' * 7)
            new_round = False
