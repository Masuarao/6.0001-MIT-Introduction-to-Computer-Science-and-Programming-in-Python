import numpy as np

# get input for x from user
x = input("Enter number x: ")
x = int(x)

# get input for y from user 
y = input("Enter number y: ")
y = int(y)

# Calculate x ^ y and convert to string
x_power_y = x**y
x_power_y = str(x_power_y)

# Calculate log x and convert to string 
log_2_x = np.log(x) / np.log(2)
log_2_x = str(int(log_2_x))

# Print results 
print("X**y = " + x_power_y)
print("log(x) = " + log_2_x)
