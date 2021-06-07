# Ask the user for the temperature in Fahrenheit and store it in a variable call deg_f. Calculate the equivalent
# temperature in degrees Celsius and store it in def_c. Output a message to the user giving the temperature in Celsius.

def_f = int(input("Enter temperature in Fahrenheit: "))
def_c = (def_f - 32) * (5/9)
print(def_c)

