"""
Fuzzy Race Membership Functions

This code demonstrates the creation of Gaussian membership functions for three categories of race variable: White, Moderate, and Black.

The 'skfuzzy' library is used to generate Gaussian membership functions using the 'gaussmf' function. 
Each membership function is defined over the range [1, 10] with parameters specifying the mean and standard deviation.

The resulting membership functions are then plotted using Matplotlib.

"""

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# Generate the race variable
race = np.linspace(1, 10, 100)

# Define Gaussian membership functions for each race category
white_membership = fuzz.gaussmf(race, 1.75, 1)
moderate_membership = fuzz.gaussmf(race, 4.75, 1)
black_membership = fuzz.gaussmf(race, 7.75, 1)

# Plot the membership functions
plt.plot(race, white_membership, label='White')
plt.plot(race, moderate_membership, label='Moderate')
plt.plot(race, black_membership, label='Black')

# Add labels and legend
plt.xlabel('Race')
plt.ylabel('Membership Value')
plt.title('Fuzzy Race Membership Functions')
plt.legend()

# Show plot
plt.show()
