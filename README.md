# Pokemon-Game
Pokemon Game
This Python script simulates a Pokémon battle between two trainers and their chosen Pokémon. Here’s a breakdown of how it works:

Classes Defined:
Trainer Class: Represents a Pokémon trainer with a name.

Pokemon Class: Represents a Pokémon with attributes including name, health, and a list of attacks. The choose_attack method allows a Pokémon to select an attack from its list.

Functions Defined:
battle(player1, player2): Simulates a two-round battle between two Pokémon. Each round consists of both Pokémon selecting attacks, calculating damage based on chosen attacks, and reducing opponent health accordingly. The battle concludes with a winner or a tie if both Pokémon have the same remaining health after two rounds.
Pokémon and Attacks Defined:

Defined instances of Pokémon (Pikachu, Charizard, Staryu, Psyduck) with their respective attributes including health and attacks.
Gameplay Flow:

Trainer Selection: Players choose their trainers (Ash or Misty) via user input.
Pokémon Selection: Players choose their Pokémon (Pikachu or Charizard for player 1, Staryu or Psyduck for player 2) via user input.
Battle Initiation: Starts the battle between the selected Pokémon of player 1 and player 2.
How to Run:

Run the script.
Follow prompts to select trainers and Pokémon for both players.
Observe the battle simulation output, which shows each round’s actions and the final outcome.
