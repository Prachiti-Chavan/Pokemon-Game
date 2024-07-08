Pokemon Battle Simulator

This project simulates Pokemon battles using Python classes. It includes implementations for Pokemon, Moves, and a Trainer class to engage in battles with wild Pokemon.

The game revolves around three primary classes:
Pokemon: This class represents a Pokemon with its stats, moves, and methods for attacking, taking damage, gaining experience, and accessing stats.

Move: Defines a move that a Pokemon can use, including details like power, accuracy, category, and any special effects it might inflict.

Trainer: Represents a trainer who has a team of Pokemon and can engage in battles with them.

Usage
The program begins by encountering a wild Pokemon randomly chosen from a predefined list.
Ash (the Trainer) selects one of his Pokemon to battle with.
Moves for the selected Pokemon are displayed, and Ash chooses a move to attack the wild Pokemon.
The wild Pokemon then attacks back.
The battle continues until either the wild Pokemon or Ash's Pokemon faints.
If Ash defeats the wild Pokemon, he has a chance to catch it based on a random catch rate.
After the battle, the program proceeds to the next encounter with a different wild Pokemon.
This process repeats for two encounters.
