#
# Program Name: Crypt
# Original Developer: Owen Sutton
# Description: This program was developed with the goal of being able to encrypt and decrypt files on your computer.
#
#  Developed in Python3.
#
# Change Log
#
# Version #   Developer     Date of Change   Description of Change
# ---------   -----------   --------------   ----------------------
# 1.01        Owen Sutton   01/11/2022       New Program
# 1.01        Owen Sutton   01/13/2022       Completed random password generator Added. Started work on Message Encryption.
# 1.02        Owen Sutton   01/18/2022       Completed work on message encryption and developed path for Message Decryption.
#


print("""

   _____   ________    __      __   ________   _______      
  /  ___|  |   __  |   \ \    / /   |  __  |  |__   __|        
 |  /      |  |__| |    \ \  / /    | |__| |    |   |     
 | |       |   \  \      \    /     |   ___|    |   |     
 | \____   |  | \  \      |  |      |  |        |   | 
  \_____|  |__|  \__|     |__|      |__|        |___| 
  
  
Created By: Owen Sutton
Email: Owensutton7@gmail.com

""")

import random
import string
from cryptography.fernet import Fernet

# Generate a random key
def GenRanKey():
    key = Fernet.generate_key()
    return key

def GenRanPassword(PLength):
    # Gather letters, numbers, symbols
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    # put all together and randomized
    all = lower + upper + num + symbols
    temp = random.sample(all,PLength)

    Password = "".join(temp)

    return Password



while True:
    option = input("Do you wish to generate a random password? Encrypt a file or text? or decrypt a file or text?:\n\n1 - Generate random Password\n2 - Encrypt File\n3 - Decrypt File\nEnter choice here: ")
    try:
        option_Int = int(option)
        if option_Int == 1:
            while True:
                length = input("What would you like the length of the password to be?:\n")
                try:
                    # Generate password
                    Password = GenRanPassword(int(length))
                    print("Password = " + str(Password))
                    break
                except:
                    print("Invalid input entered, please try again!")
            break

        elif option_Int == 2:
            while True:
                eoption = input("Would you like to encrypt a message or file?\n1 - Encrypt Message\n2 - Encrypt File\nEnter choice here: ")
                eoption_int = int(eoption)
                try:
                    if eoption_int == 1:
                        # get message to be encrypted
                        message = input("What message would you like to encrypt?\nEnter choice here: ")
                        # generate random key
                        pk = Fernet.generate_key()
                        pk2 = Fernet(pk)
                        print("Your randomly generated key is = " + str(pk))
                        # encrypt the message
                        emessage = pk2.encrypt(message.encode())
                        print("Original message: ", message)
                        print("Encrypted message: ", emessage)
                        print("Note, you will need the random generate key to be able to decrypt the message. Don't lose it!")
                        break

                    elif eoption_int == 2:
                        break

                    else:
                        print("Invalid input entered, please try again!")
                except:
                    print("Invalid input entered, please try again!")

            break
        elif option_Int == 3:
            MessageorFile = input("Would you like to decrypt a message or file?\n1 - Message\n2 - File\n Enter Here: ")
            while True:
                IntMess = int(MessageorFile)
                try:
                    if IntMess == 1:
                        print("You have choosen to decrypt a message or file!")
                        GetEmessage = input("What is the encrypted text? \nEnter Here: ")
                        GetRanKey = input("What is your key? \nEnter Here: ")

                        a = str.encode(str(GetRanKey))
                        x = Fernet(a)

                        y = str.encode(str(GetEmessage))

                        decryptedmessage = x.decrypt(y).decode()

                        print("Decrypted message: ", decryptedmessage)

                        break

                    elif IntMess == 2:

                        break
                    else:
                        print("Invalid input entered, please try again!")
                        break
                except:
                    print("Invalid input entered, please try again!")

            break
        else:
            print("Invalid input entered, please try again!")

    except:
        print("Invalid input entered, please try again!")



# places key into filekey file.
#with open('filekey.key', 'wb') as filekey:
 #   filekey.write(key)

