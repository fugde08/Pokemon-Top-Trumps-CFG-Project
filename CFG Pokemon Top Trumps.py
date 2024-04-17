import random
import requests
import time


print("""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨⬛⬜⬜
⬜⬜⬜⬜⬜⬛⬛🟨🟨🟨🟨🟨⬛🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨⬛🟨🟨🟨🟨🟨⬛⬛⬜
⬜⬜⬜⬜⬛⬛⬛⬛🟨🟨⬛⬛🟨🟨⬛⬛🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨⬛⬛🟨🟨⬛⬛🟨🟨⬛⬛⬛⬛
⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬛⬛⬛⬛⬛⬛
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟨🟨🟥🟥🟨🟨🟨🟨⬛⬛⬛⬛⬛🟨🟨🟨🟨🟥🟥🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛🟨🟥🟥🟥🟥🟨🟨🟨⬛🟥🟥🟥⬛🟨🟨🟨🟥🟥🟥🟥🟨⬛⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟨⬛⬛⬛⬜⬛🟨🟥🟥🟥🟥🟨🟨🟨⬛🟥🟥🟥⬛🟨🟨🟨🟥🟥🟥🟥🟨⬛⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟥🟥🟨🟨🟨🟨⬛🟥🟥🟥⬛⬛⬛🟨🟨🟥🟥🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛⬛🟨🟨⬛🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨⬛🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜
⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨⬛🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜
⬛⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨⬛🟨⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛🟨🟨⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬛🟨🟨🟨⬛⬛⬛⬛⬛🟨🟨⬛🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛🟨🟨🟨⬛⬛⬛🟨🟨⬛🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛🟨🟨🟨⬛🟨🟨🟨⬛🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬜⬜⬜⬜⬜⬜

░█▀▀█ ░█▀▀▀█ ░█─▄▀ ░█▀▀▀ ░█▀▄▀█ ░█▀▀▀█ ░█▄─░█ 　 ▀▀█▀▀ ░█▀▀▀█ ░█▀▀█ 　 ▀▀█▀▀ ░█▀▀█ ░█─░█ ░█▀▄▀█ ░█▀▀█ ░█▀▀▀█ 
░█▄▄█ ░█──░█ ░█▀▄─ ░█▀▀▀ ░█░█░█ ░█──░█ ░█░█░█ 　 ─░█── ░█──░█ ░█▄▄█ 　 ─░█── ░█▄▄▀ ░█─░█ ░█░█░█ ░█▄▄█ ─▀▀▀▄▄ 
░█─── ░█▄▄▄█ ░█─░█ ░█▄▄▄ ░█──░█ ░█▄▄▄█ ░█──▀█ 　 ─░█── ░█▄▄▄█ ░█─── 　 ─░█── ░█─░█ ─▀▄▄▀ ░█──░█ ░█─── ░█▄▄▄█
""")
def introduction():
    username = input("\nWelcome player, please enter a username: ")
    while not username:
        username = input("Invalid username, please try again: ")

    return username

player_name = introduction()

def rounds(player_name):
    battle_ready = input(f"\n{player_name} are you ready to battle? (y/n) ").lower()
    if battle_ready == "y" or battle_ready == "yes":
        while True:
           no_rounds = input("\nExcellent, how many cards would you like? (1-15): ")
           if no_rounds.isdigit() and 1 <= int(no_rounds) <= 15:
               no_rounds = int(no_rounds)
               break
           else:
               input("Please enter a valid number between 1 and 15: ")
    else:
        print("Okay, have a nice day.")
        exit()
    return no_rounds

number_of_rounds = rounds(player_name)

def random_pokemon():
    pokemon_id = random.randint(1, 150)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)
    pokemon_data = response.json()

    name = pokemon_data['name']
    pokemon_id = pokemon_data['id']
    weight = pokemon_data['weight'] / 10  # Convert decigrams to kilograms
    height = pokemon_data['height'] * 10  # Convert decimeters to centimeters
    num_moves = len(pokemon_data['moves'])
    health = pokemon_data['stats'][0]['base_stat']
    attack = pokemon_data['stats'][1]['base_stat']
    defense = pokemon_data['stats'][2]['base_stat']

    player_pokemon = {
        'name': name,
        'id': pokemon_id,
        'weight': weight,
        'height': height,
        'moves': num_moves,
        'health': health,
        'attack': attack,
        'defense': defense
    }

    return player_pokemon

def game(number_of_rounds):
    player_score = 0
    opponent_score = 0

    for i in range(number_of_rounds):
        player_pokemon = random_pokemon()
        oppositions_pokemon = random_pokemon()
        rounds_played = i + 1
        print("""      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ➖➖🟥🟥🟥🟥🟥
                ➖🟥🟥🟥🟥🟥🟥🟥
                🟥🟥🟥🟥🟥🟥🟥🟥🟥
                🟥🟥🟥⬛⬛⬛🟥🟥🟥
                  ⬛⬛⬛⬜⬛⬛⬛⬛
                ⬜⬜⬜⬛⬛⬛⬜⬜⬜
                ⬜⬜⬜⬜⬜⬜⬜⬜⬜
                ➖⬜⬜⬜⬜⬜⬜⬜
                ➖➖⬜⬜⬜⬜⬜⠀⠀⠀⠀⠀⠀
        ⠀           
        """)
        print(f"\nRound {rounds_played} - you have captured:")
        print(f"\nName: {player_pokemon['name']}")
        print(f"ID: {player_pokemon['id']}")
        print(f"1. Weight: {player_pokemon['weight']} kg")
        print(f"2. Height: {player_pokemon['height']} cm")
        print(f"3. No. of moves: {player_pokemon['moves']}")
        print(f"4. Health: {player_pokemon['health']}")
        print(f"5. Attack: {player_pokemon['attack']}")
        print(f"6. Defence: {player_pokemon['defense']}")
        time.sleep(3.0)
        stat_choice = int(input("\nWhich stat would you like to use (1-6)? Highest stat wins. "))

        print(f"\nYour opponent has caught:")
        print(f"\nName: {oppositions_pokemon['name']}")
        print(f"ID: {oppositions_pokemon['id']}")
        print(f"1. Weight: {oppositions_pokemon['weight']} kg")
        print(f"2. Height: {oppositions_pokemon['height']} cm")
        print(f"3. No. of moves: {oppositions_pokemon['moves']}")
        print(f"4. Health: {oppositions_pokemon['health']}")
        print(f"5. Attack: {oppositions_pokemon['attack']}")
        print(f"6. Defence: {oppositions_pokemon['defense']}")

        if stat_choice == 1:
            print(f"\nYour opponent's Pokemon is {oppositions_pokemon['name']} (Id {oppositions_pokemon['id']}) and weighs {oppositions_pokemon['weight']}kg.\nYour Pokemon {player_pokemon['name']} weighs {player_pokemon['weight']}kg.")
            if player_pokemon['weight'] > oppositions_pokemon['weight']:
                player_score += 1
                print("\nYou have won this round. Congratulations!")
            else:
                opponent_score += 1
                print("\nYou have been defeated, try again.")
        elif stat_choice == 2:
            print(f"\nYour opponent's Pokemon is {oppositions_pokemon['name']} (Id {oppositions_pokemon['id']}) and is {oppositions_pokemon['height']}cm tall.\nYour Pokemon {player_pokemon['name']} is {player_pokemon['height']}cm tall.")
            if player_pokemon['height'] > oppositions_pokemon['height']:
                player_score += 1
                print("You have won this round. Congratulations!")
            else:
                opponent_score += 1
                print("\nYou have been defeated, try again.")
        elif stat_choice == 3:
            print(f"\nYour opponent's Pokemon is {oppositions_pokemon['name']} (Id {oppositions_pokemon['id']}) and has {oppositions_pokemon['moves']} moves.\nYour Pokemon {player_pokemon['name']} has {player_pokemon['moves']} moves.")
            if player_pokemon['moves'] > oppositions_pokemon['moves']:
                player_score += 1
                print("\nYou have won this round. Congratulations!")
            else:
                opponent_score += 1
                print("\nYou have been defeated, try again.")
        elif stat_choice == 4:
            print(f"\nYour opponent's Pokemon is {oppositions_pokemon['name']} (Id {oppositions_pokemon['id']}) and has {oppositions_pokemon['health']} health.\nYour Pokemon {player_pokemon['name']} and has {player_pokemon['health']} health.")
            if player_pokemon['health'] > oppositions_pokemon['health']:
                player_score += 1
                print("\nYou have won this round. Congratulations!")
            else:
                opponent_score += 1
                print("\nYou have been defeated, try again.")
        elif stat_choice == 5:
            print(f"\nYour opponent's Pokemon is {oppositions_pokemon['name']} (Id {oppositions_pokemon["id"]}) and has {oppositions_pokemon['attack']} attack strength.\nYour Pokemon {player_pokemon["name"]} has attack strength {player_pokemon["attack"]}.")
            if player_pokemon['attack'] > oppositions_pokemon['attack']:
                player_score += 1
                print("\nYou have won this round. Congratulations!")
            else:
                opponent_score += 1
                print("\nYou have been defeated, try again.")
        elif stat_choice == 6:
            print(f"\nYour opponent's Pokemon is {oppositions_pokemon['name']} (Id {oppositions_pokemon["id"]}) and has level {oppositions_pokemon['defence']} of defence.\nYour Pokemon {player_pokemon["name"]} has level {player_pokemon["defence"]} of defence.")
            if player_pokemon['defence']> oppositions_pokemon['defence']:
                player_score += 1
                print("\n\nYou have won this round. Congratulations!")
            else:
                opponent_score += 1
                print("\nYou have been defeated, try again.")
        else:
            print(f"\nPlease enter a valid digit of 1 to 6:")

    return player_score, opponent_score

results = game(number_of_rounds)
def score(results):
    print("\nBattle Results:")
    print(f"\nYour Score: {results[0]}")
    print(f"Opponent's Score: {results[1]}")
    if results[0] > results[1]:
        print("\nCongratulations! You are the overall winner!")
    elif results[0] < results[1]:
        print("\nOpponent wins the overall battle! Better luck next time.")
    else:
        print("\nIt's a tie! Both sides fought well.")

end_game = score(results)
