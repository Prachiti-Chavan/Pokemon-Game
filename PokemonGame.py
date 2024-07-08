import random

class Pokemon:
    def __init__(self, name, type, health, attack, defence, special_attack, special_defence, speed, level, experience, moves):
        self.name = name
        self.type = type
        self.health = health
        self.base_attack = attack
        self.defence = defence
        self.special_attack = special_attack
        self.special_defence = special_defence
        self.speed = speed
        self.level = level
        self.experience = experience
        self.moves = moves
        self.is_wild = False  # For wild Pokémon

    def perform_attack(self, move, opponent):
        # Calculate damage based on move power and opponent's defence
        damage = move.power * (self.base_attack / opponent.defence)
        opponent.take_damage(damage)
        print(f"{self.name} used {move.name} and dealt {damage} damage to {opponent.name}.")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} fainted!")

    def gain_experience(self, exp):
        self.experience += exp
        # Check for level up
        if self.experience >= 100:  # Example threshold for leveling up
            self.level_up()

    def level_up(self):
        # Increase stats and potentially learn new moves
        self.level += 1
        print(f"{self.name} leveled up to level {self.level}!")

    def learn_move(self, move):
        self.moves.append(move)
        print(f"{self.name} learned {move.name}!")

    def get_stat(self, stat):
        if stat == 'health':
            return self.health
        elif stat == 'attack':
            return self.base_attack
        elif stat == 'defence':
            return self.defence
        elif stat == 'special_attack':
            return self.special_attack
        elif stat == 'special_defence':
            return self.special_defence
        elif stat == 'speed':
            return self.speed
        elif stat == 'level':
            return self.level
        elif stat == 'experience':
            return self.experience
        else:
            raise ValueError(f"Invalid stat '{stat}' requested.")

class Move:
    def __init__(self, name, type, power, accuracy, category, effect=None):
        self.name = name
        self.type = type
        self.power = power
        self.accuracy = accuracy
        self.category = category
        self.effect = effect

    def apply_effect(self, target):
        if self.effect:
            # Implement move effect on the target Pokémon
            print(f"{self.name} applied {self.effect} effect on {target.name}!")

class Trainer:
    def __init__(self, name):
        self.name = name
        self.team = []
        self.inventory = []

    def catch_pokemon(self, wild_pokemon):
        catch_rate = random.random()  # Generate a random catch rate
        if catch_rate > 0.5:  # Example catch success condition
            self.team.append(wild_pokemon)
            print(f"{self.name} caught {wild_pokemon.name}!")
        else:
            print(f"{self.name} failed to catch {wild_pokemon.name}!")

    def use_item(self, item, target):
        item.use(target)

    def battle(self, opponent):
        print(f"{self.name} encounters {opponent.name}!")

        for _ in range(2):  # Change to two encounters
            # Trainer's turn
            print(f"{self.name}'s turn:")
            print("Choose a Pokémon:")
            for i, pokemon in enumerate(self.team, start=1):
                print(f"{i}. {pokemon.name} ({pokemon.health} HP)")

            pokemon_choice = int(input("Enter Pokémon number: ")) - 1
            selected_pokemon = self.team[pokemon_choice]

            print(f"What move should {selected_pokemon.name} use?")
            for i, move in enumerate(selected_pokemon.moves, start=1):
                print(f"{i}. {move.name}")

            move_choice = int(input("Enter move number: ")) - 1
            selected_move = selected_pokemon.moves[move_choice]

            selected_pokemon.perform_attack(selected_move, opponent)

            # Check if opponent is defeated
            if opponent.health <= 0:
                print(f"{opponent.name} fainted!")
                self.catch_pokemon(opponent)  # Attempt to catch the opponent
                break

            # Opponent's turn
            print(f"{opponent.name}'s turn:")
            opponent_move = random.choice(opponent.moves)
            opponent.perform_attack(opponent_move, selected_pokemon)

            # Check if player's Pokémon is defeated
            if selected_pokemon.health <= 0:
                print(f"{selected_pokemon.name} fainted!")
                break

# Example Pokémon and Moves
pikachu = Pokemon("Pikachu", "Electric", 100, 50, 40, 60, 50, 90, 1, 0, [
    Move("Thunderbolt", "Electric", 90, 100, "Special"),
    Move("Quick Attack", "Normal", 40, 100, "Physical"),
    Move("Tail Whip", "Normal", None, None, "Status", "Lowers opponent's defence")
])

charizard = Pokemon("Charizard", "Fire", 120, 60, 50, 80, 70, 100, 1, 0, [
    Move("Flamethrower", "Fire", 95, 100, "Special"),
    Move("Dragon Claw", "Dragon", 80, 100, "Physical"),
    Move("Air Slash", "Flying", 75, 95, "Special")
])

bulbasaur = Pokemon("Bulbasaur", "Grass", 80, 40, 30, 50, 45, 70, 1, 0, [
    Move("Vine Whip", "Grass", 45, 100, "Physical"),
    Move("Poison Powder", "Poison", None, 75, "Status", "Poisons the opponent"),
    Move("Sleep Powder", "Grass", None, 75, "Status", "Puts opponent to sleep")
])

snorlax = Pokemon("Snorlax", "Normal", 160, 110, 65, 65, 110, 30, 1, 0, [
    Move("Body Slam", "Normal", 85, 100, "Physical"),
    Move("Rest", "Psychic", None, None, "Status", "Heals all status problems and recovers HP"),
    Move("Hyper Beam", "Normal", 150, 90, "Special")
])

butterfree = Pokemon("Butterfree", "Bug", 90, 45, 50, 90, 80, 70, 1, 0, [
    Move("Bug Buzz", "Bug", 90, 100, "Special"),
    Move("Sleep Powder", "Grass", None, 75, "Status", "Puts opponent to sleep"),
    Move("Air Slash", "Flying", 75, 95, "Special")
])

# Example Trainer (Ash)
ash = Trainer("Ash")
ash.team = [pikachu, charizard]

# List of wild Pokémon
wild_pokemons = [bulbasaur, snorlax, butterfree]

# Simulate two encounters for Ash
for _ in range(2):
    wild_pokemon = random.choice(wild_pokemons)
    ash.battle(wild_pokemon)
    print("\n--- Next Encounter ---\n")
