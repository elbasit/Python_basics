import random

# This is simple random password generator 
# Which generates random on given 
# First name, Last name, phone, car number and birthday
# It generates two types of passwords
# First password is default of 8 words
# Second password is created on users given length.

# Writer Abdul Basit
# elbasit23@gmail.com
# https://github.com/elbasit

#Function for getting password length
def get_password_length():
    length = input("How long do you want your password: ")
    return int(length)


#Function for Generating random Password
def password_generator(length):


    printable = f'{F_name}{L_name}{phone}{car}{birthday}'

    printable = list(printable)
    random.shuffle(printable)

    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password


#Main Body
F_name = input("Enter your first name:")
L_name = input("Enter your last name:")
phone = input("Enter your phone number:")
car = input("Enter your car number:")
birthday = input("Enter your Date of birth:")

password_one = password_generator(8) #Code for Default Password
password_length = get_password_length() 
password_two = password_generator(password_length) # Code for Users password length

print("Here is password one with 8 digits default length: (" + str(len(password_one)) + "):\t\t" + password_one)
print("Here is password one with your choice of length(" + str(len(password_two)) + "):\t\t" + password_two)