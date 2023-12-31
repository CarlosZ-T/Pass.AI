# Import random library...
import random

# Print welcome message to the users...
print('Welcome To Your Personal Password Generator!')

# Set a variable equal to all available characters...
possible_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMONPQRSTUVWXYZ1234567890!@#$%^&*().,?~'

# Set a variable equal to how many passwords have been requested and prompt the user...
pass_num = input('\nEnter how many passwords to generate here: ')
# Ensure that the variable is an integer...
pass_num = int(pass_num)

# Set a variable for password length and prompt the user...
pass_length = input('\nEnter the desired password length here: ')
# Ensure that the variable is an integer...
pass_length = int(pass_length)

# Print the passwords to the user...
print('\nCheck out your passwords below:')
# Create a counter variable...
count = 1

# Create a for loop to generate random passwords...
for password in range(pass_num):
    # Set a variable for the passwords...
    pwds = ''
    # Create a nested loop for...
    for c in range(pass_length):
        # Add random characters to the password variable...
        pwds += random.choice(possible_chars)
    # Print the passwords to the user...    
    print(f'\n{count}. {pwds}')
    # Increment the counter...
    count += 1

