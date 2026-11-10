# Thanksgiving Feast Simulator

This creative Assignment 3 model simulates guests arriving at Thanksgiving dinner. Each guest randomly chooses three dishes from turkey, stuffing, potatoes, cranberry sauce, and pie. If all three selected dishes still have servings, the guest receives a complete plate.

## Run the model

```bash
python thanksgiving_feast_model.py
```

The program asks you for the number of guests, servings per dish, and whether debug mode should be turned on. Debug mode prints each guest's plate result. The final visualization has two graphs: a bar chart showing leftover servings for each dish and a pie chart showing complete versus incomplete plates.

## Model assumptions

- Every guest randomly chooses three different dishes.
- Every dish is equally likely to be chosen.
- Each guest can receive at most one serving of each selected dish.
- The model does not include seconds, preferences, allergies, or food waste.

## Collaborators

- Janeth Ochoa
