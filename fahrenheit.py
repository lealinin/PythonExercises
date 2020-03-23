# Define a function that takes in an input
# temperature in Fahrenheit and converts it
# to Celsius


def f_t_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp


f100_in_celsius = f_t_c(100)
print(f100_in_celsius)