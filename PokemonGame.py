import random

class Trainer:
    def __init__(self, name):
        self.name = name

class Pokemon:
    def __init__(self, name, health, attacks):
        self.name = name
        self.health = health
        self.attacks = attacks

    def choose_attack(self):
        print(f"Available attacks for {self.name}:")
        for i, attack in enumerate(self.attacks, start=1):
            print(f"{i}. {attack['name']} (Damage: {attack['damage']})")

        attack_choice = int(input(f"Choose an attack (1-{len(self.attacks)}): "))
        return self.attacks[attack_choice - 1]

def battle(player1, player2):
    for _ in range(2):
        print("\nRound start!")
        player1_attack = player1.choose_attack()
        player2_attack = player2.choose_attack()

        player1_damage = player1_attack['damage']
        player2_damage = player2_attack['damage']

        player2.health -= player1_damage
        player1.health -= player2_damage

        print(f"{player1.name} used {player1_attack['name']} and dealt {player1_damage} damage to {player2.name}.")
        print(f"{player2.name} used {player2_attack['name']} and dealt {player2_damage} damage to {player1.name}.")

        if player1.health <= 0 or player2.health <= 0:
            break

    if player1.health > player2.health:
        print(f"{player1.name} wins!")
    elif player2.health > player1.health:
        print(f"{player2.name} wins!")
    else:
        print("It's a tie!")

# Define Pokémon and their attacks
pikachu = Pokemon("Pikachu", 100, [
    {"name": "Thunderbolt", "damage": 60},
    {"name": "Quick Attack", "damage": 30},
    {"name": "Tail Whip", "damage": 40}
])

charizard = Pokemon("Charizard", 100, [
    {"name": "Flamethrower", "damage": 70},
    {"name": "Dragon Rage", "damage": 80},
    {"name": "Wing Attack", "damage": 30}
])

staryu = Pokemon("Staryu", 100, [
    {"name": "Tackle", "damage": 20},
    {"name": "Water Gun", "damage": 40},
    {"name": "Hydropump", "damage": 50}
])

psyduck = Pokemon("Psyduck", 100, [
    {"name": "Scratch", "damage": 30},
    {"name": "Confusion", "damage": 60},
    {"name": "Tail Whip", "damage": 40}
])

# Let players choose their trainers
ash = Trainer("Ash")
misty = Trainer("Misty")

player1_trainer = ash if input("Player 1, choose Ash (a) or Misty (m): ").lower() == 'a' else misty
player2_trainer = ash if input("Player 2, choose Ash (a) or Misty (m): ").lower() == 'a' else misty

# Let players choose their Pokémon
player1_pokemon = pikachu if input("Player 1, choose Pikachu (p) or Charizard (c): ").lower() == 'p' else charizard
player2_pokemon = staryu if input("Player 2, choose Staryu (s) or Psyduck (d): ").lower() == 's' else psyduck

# Start the battle
battle(player1_pokemon, player2_pokemon)
