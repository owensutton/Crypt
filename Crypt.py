#
# Program Name: Crypt
# Original Developer: Owen Sutton
# Description: This program was developed with the goal of being able to encrypt and decrypt files on your computer.
#
#  Developed in Python3.
#
#
# Change Log
#
# Version #   Developer     Date of Change   Description of Change
# ---------   -----------   --------------   ----------------------
# 1.0         Owen Sutton   01/11/2022       New Program
#
#


from cryptography.fernet import Fernet

# Generate a random key
def GenRanKey():
    key = Fernet.generate_key()
    print("Key Generated = " + key)

while True:
    option = input("Do you wish to generate a random key? Encrypt a file? or decrypt a file?:\n\n1 - Generate random key\n2 - Encrypt File\n3 - Decrypt File\nEnter choice here: ")
    try:
        option_Int = int(option)
        if option_Int == 1:
            GenRanKey()
            break

        elif option_Int == 2:

            break
        elif option_Int == 3:

            break
        else:
            print("Invalid input entered, please try again!")

    except:
        print("Invalid input entered, please try again!")


# places key into filekey file.
#with open('filekey.key', 'wb') as filekey:
 #   filekey.write(key)


