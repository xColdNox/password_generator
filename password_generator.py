import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = "1234567890"
symbols = "!@#$%^&*=+"

# below I create a password randomized from all the categories

generated = lowercase + uppercase + numbers + symbols
passwordlen = 10
password = "".join(random.sample(generated, passwordlen))

# below I create a password which has letters first and symbols + numbers later for easier memorization

generate_letters = lowercase + uppercase
generate_num_symb = numbers + symbols
passwordletterlen = 6
password_num_symb_len = 4
passwordeasier = "".join(random.sample(generate_letters, passwordletterlen) + random.sample(generate_num_symb, password_num_symb_len))

print("Your unbreakable password is: " + password)
print("However if you want an easier to remember password, there you go: " + passwordeasier)
