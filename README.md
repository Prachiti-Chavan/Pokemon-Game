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

E-commerce Data Analysis 

This analysis provides insights into various aspects of your Amazon sales data, helping you understand customer behavior, product performance, and promotional impact.

Dataset taken from kaggle = E-Commerce Sales Dataset by THE DEVASTATOR

1. Sales Performance Over Time:
Analyzed monthly sales trends using a line chart. This helps identify peak sales months and potential seasonality.

3. Top Selling Products/Categories:
Identified the top 10 products (or categories) by total sales using a bar chart. This allows you to focus marketing efforts on high-performing products.
Profitability by Category:
Calculated the probability of product categories using value counts and normalization. This reveals the relative contribution of each category to overall sales.

4. Promotion Applied:
Analyzed the impact of promotions by creating a new "Promotion" category. This involved:
Handling missing values in the "promotion-ids" column.
Defining a function to categorize promotions based on ID lists and a free shipping code.
Calculating the probability of different promotion categories (Free Financing, Free Shipping, None, or Other). This provides insights into the effectiveness of different promotions.

