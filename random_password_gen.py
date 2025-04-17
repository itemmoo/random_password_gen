import random
import math
import firebase_admin
from firebase_admin import credentials, db

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

password_use = input("What will this password be used for?: ").lower()

pass_len = int(input("Enter Password Length:"))

alpha_len = pass_len//2
num_len = math.ceil(pass_len*30/100)
special_len = pass_len-(alpha_len+num_len)


password = []


def generate_pass(length, array, is_alpha=False):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)


# alpha password
generate_pass(alpha_len, alpha, True)
# numeric password
generate_pass(num_len, num)
# special Character password
generate_pass(special_len, special)
# suffle the generated password list
random.shuffle(password)
# convert the list to string
gen_password = ""
for i in password:
    gen_password = gen_password + str(i)
print(gen_password)

print(f"\nGenerated Password for {password_use.capitalize()}: {gen_password}")


###############################################


# Path to your downloaded service account key
cred = credentials.Certificate("D:/key/serviceAccountKey.json")


# Initialize the Firebase Admin SDK
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://password-2e336-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('password')

# Get the current number of passwords in the database to assign the next reference
password_count = len(ref.get() or {}) + 1  # This gets the current count of passwords stored

# Create a new reference for the next password
password_ref = f'password{password_count}'

# Set data in the database with the new reference
ref.child(password_ref).set({
    'for': password_use,
    'pass': gen_password
})

# Retrieve data from the database to confirm it was added
data = ref.get()
print(data)

