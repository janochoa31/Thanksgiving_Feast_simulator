#!/usr/local/bin/python3

#janeth ochoa
#assignment 3 creating a model using python script and the help of AI

#Thanksgiving Feast Model 
##########################

# Import numpy so the program can make random dish choices.
import numpy as np
# Import matplotlib so the program can make graphs.
import matplotlib.pyplot as plt


# Ask the user how many guests are coming to Thanksgiving dinner.
num_guests = int(input("How many guests are coming? "))
# Ask the user how many servings of each dish are available.
servings_each = int(input("How many servings of each dish are available? "))
# Ask the user whether they want to see information about every guest.
debug_answer = input("Turn debug mode on? (yes/no): ").lower()
# Turn debug on when the user types yes or y.
debug = debug_answer == "yes" or debug_answer == "y"

# Stop the program if the user enters an impossible number.
if num_guests < 1 or servings_each < 1:
    raise ValueError("Please enter numbers greater than zero.")

# Make a list of the Thanksgiving dishes in the model.
dishes = ["Turkey", "Stuffing", "Potatoes", "Cranberry", "Pie"]
# Make a dictionary showing how many servings of each dish are available.
remaining = {}
# Put the starting number of servings into the dictionary for every dish.
for dish in dishes:
    remaining[dish] = servings_each

# Create variables to count complete and incomplete plates.
complete_plates = 0
incomplete_plates = 0
# Set a seed so the same random choices happen each time we run the program.
np.random.seed(7)

# Simulate each guest arriving at the Thanksgiving dinner.
for guest in range(1, num_guests + 1):
    # Randomly choose three different dishes for this guest.
    choices = [str(dish) for dish in np.random.choice(dishes, size=3, replace=False)]
    # Start by assuming the guest can receive a complete plate.
    can_make_plate = True

    # Check each dish selected by the guest.
    for dish in choices:
        # If one selected dish is gone, the plate cannot be complete.
        if remaining[dish] == 0:
            can_make_plate = False

    # Use an if/else statement to count the type of plate.
    if can_make_plate:
        # Remove one serving from each dish on the complete plate.
        for dish in choices:
            remaining[dish] -= 1
        # Add one to the complete-plate count.
        complete_plates += 1
        # Print the guest's choices when debug mode is on.
        if debug:
            print("Guest", guest, "received", list(choices))
    else:
        # Add one to the incomplete-plate count.
        incomplete_plates += 1
        # Print a message when this guest could not get a complete plate.
        if debug:
            print("Guest", guest, "could not receive", list(choices))

# Print the final counts so the results are easy to read.
print("Complete plates:", complete_plates)
print("Incomplete plates:", incomplete_plates)
print("Leftover servings:")
# Print the leftover amount for every dish.
for dish in dishes:
    print(dish, ":", remaining[dish])

# Create a figure with two simple graphs.
plt.figure(figsize=(12, 5))

# Make the first graph a bar chart of the leftover servings.
plt.subplot(1, 2, 1)
# Get the leftover numbers in the same order as the dish names.
leftovers = [remaining[dish] for dish in dishes]
# Draw one bar for each Thanksgiving dish.
plt.bar(dishes, leftovers, color=["brown", "gold", "tan", "red", "orange"])
# Label the first graph.
plt.title("Thanksgiving Leftovers")
plt.xlabel("Dish")
plt.ylabel("Servings remaining")
# Rotate the dish names so they fit under the bars.
plt.xticks(rotation=35)

# Make the second graph a pie chart of plate outcomes.
plt.subplot(1, 2, 2)
# Put the two plate counts into a list for the pie chart.
plate_counts = [complete_plates, incomplete_plates]
# Give the two pie sections names.
plate_labels = ["Complete plates", "Incomplete plates"]
# Draw the pie chart and show percentages.
plt.pie(plate_counts, labels=plate_labels, autopct="%1.1f%%",
        colors=["green", "lightcoral"])
# Label the second graph.
plt.title("Plate Results")

# Adjust the graphs so the labels do not overlap.
plt.tight_layout()
# Display the graphs at the end of the program.
plt.show()

# Print the final counts so the results are easy to read.
print("Complete plates:", complete_plates)
print("Incomplete plates:", incomplete_plates)
print("Leftover servings:")
# Print the leftover amount for every dish.
for dish in dishes:
    print(dish, ":", remaining[dish])

# Create a figure with two simple graphs.
plt.figure(figsize=(12, 5))

# Make the first graph a bar chart of the leftover servings.
plt.subplot(1, 2, 1)
# Get the leftover numbers in the same order as the dish names.
leftovers = [remaining[dish] for dish in dishes]
# Draw one bar for each Thanksgiving dish.
plt.bar(dishes, leftovers, color=["brown", "gold", "tan", "red", "orange"])
# Label the first graph.
plt.title("Thanksgiving Leftovers")
plt.xlabel("Dish")
plt.ylabel("Servings remaining")
# Rotate the dish names so they fit under the bars.
plt.xticks(rotation=35)

# Make the second graph a pie chart of plate outcomes.
plt.subplot(1, 2, 2)
# Put the two plate counts into a list for the pie chart.
plate_counts = [complete_plates, incomplete_plates]
# Give the two pie sections names.
plate_labels = ["Complete plates", "Incomplete plates"]
# Draw the pie chart and show percentages.
plt.pie(plate_counts, labels=plate_labels, autopct="%1.1f%%",
        colors=["green", "lightcoral"])
# Label the second graph.
plt.title("Plate Results")

# Adjust the graphs so the labels do not overlap.
plt.tight_layout()
# Display the graphs at the end of the program.
plt.show()



