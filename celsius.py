# Define a function that takes in an input
# temperature in Celsius and converts it
# to Fahrenheit


def c_to_f(c_temp):
    f_temp = (c_temp * (9/5)) + 32
    return f_temp


c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)