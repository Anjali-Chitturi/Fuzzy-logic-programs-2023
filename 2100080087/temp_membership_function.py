"""
Fuzzy Temperature Membership Functions

This code demonstrates the creation of trapezoidal membership functions for different temperature categories: Warm, Moderate, Cold, and Hot.

Using the 'skfuzzy' library, trapezoidal membership functions are defined for each temperature category over the range [-10, 50].
The 'trapmf' function is used to create trapezoidal membership functions with specified parameters defining the four points of the trapezoid.

The resulting membership functions are then plotted using Matplotlib.

"""

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

# Generate the temperature variable
temp = np.linspace(-10, 50, 100)

# Define trapezoidal membership functions for each temperature category
warm_membership = fuzz.trapmf(temp, [20, 25, 30, 35])
moderate_membership = fuzz.trapmf(temp, [10, 15, 20, 25])
cold_membership = fuzz.trapmf(temp, [-5, 0, 5, 10])
hot_membership = fuzz.trapmf(temp, [30, 35, 40, 45])

# Plot the membership functions
plt.plot(temp, warm_membership, label='Warm')
plt.plot(temp, moderate_membership, label='Moderate')
plt.plot(temp, cold_membership, label='Cold')
plt.plot(temp, hot_membership, label='Hot')

# Add labels and legend
plt.xlabel('Temperature')
plt.ylabel('Membership Value')
plt.title('Fuzzy Temperature Membership Functions')
plt.legend()

# Show plot
plt.show()
