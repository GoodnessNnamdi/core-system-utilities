import random
import string

num_passwords = int(input("How many passswords do you want to generate😏?: "))
char_length = int(input("Enter the number of characters for each passwords: "))

all_characters = string.ascii_letters + string.digits + string.punctuation

print("\nGenerated Passwords: ")

for i in range(num_passwords):
    passsword = "".join(random.choices(all_characters, k = char_length))
    print (passsword)
