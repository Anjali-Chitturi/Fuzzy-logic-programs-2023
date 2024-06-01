"""
Fuzzy Logic Defuzzification

This code demonstrates the use of fuzzy logic to perform defuzzification and compares the results using different methods.

The example uses a trapezoidal membership function defined over the range [0, 5]. It then applies two different defuzzification methods: bisector and mean of maximum (MOM). 

The defuzzification methods are applied using the 'defuzz' function from the 'skfuzzy' library. The result of each method is printed and visualized using matplotlib.

"""

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

# Generate the universe variables
x = np.arange(0, 5.05, 0.1)

# Generate the fuzzy membership function
mfx = fuzz.trapmf(x, [2, 2.5, 3, 4.5])

# Perform defuzzification using bisector method
defuzz_bisector = fuzz.defuzz(x, mfx, 'bisector')

# Perform defuzzification using mean of maximum (MOM) method
defuzz_mom = fuzz.defuzz(x, mfx, 'mom')

# Print the defuzzification results
print('Bisector defuzzification result:', defuzz_bisector)
print('Mean of maximum defuzzification result:', defuzz_mom)

# Plot the membership function and defuzzification results
plt.plot(x, mfx, 'k')
plt.vlines(defuzz_bisector, 0, fuzz.interp_membership(x, mfx, defuzz_bisector),
           label='Bisector', color='b')
plt.vlines(defuzz_mom, 0, fuzz.interp_membership(x, mfx, defuzz_mom),
           label='Mean of maximum', color='g')
plt.xlabel('x')
plt.ylabel('Membership Function Value')
plt.title('Fuzzy Logic Defuzzification')
plt.legend()
plt.show()
