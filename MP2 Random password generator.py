
# PROJECT 2: Random Password Generator

import random      # For random character selection
import string      # Provides pre-defined character sets

pass_len = 12      # Set password length (you can change this)

# Combine all possible characters into one pool
# ascii_letters = A-Z and a-z (52 characters)
# digits = 0-9 (10 characters)  
# punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ (32 characters)
# Total = 94 characters for maximum complexity
char_values = string.ascii_letters + string.digits + string.punctuation

# Generate password: pick random characters and join them into a string
result = "".join([random.choice(char_values) for i in range(pass_len)])

# Display the generated password
print("Your random password is:", result)