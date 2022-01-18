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
# 1.03        Owen Sutton   01/18/2022       Completed work for encrypting and decrypting a file.
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

import os
import sys
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
    option = input("Do you wish to generate a random password? Encrypt a file or text? or decrypt a file or text?:\n\n1 - Generate random Password\n2 - Encrypt\n3 - Decrypt\nEnter choice here: ")
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
                        print("Note the file you wish to have encrypted should be placed in the 'encrypt_file' folder. ")
                        efile = input("What is the name of the file you wish to encrypt? \nEnter Here: ")

                        ef = Fernet.generate_key()
                        ef2 = Fernet(ef)

                        # move working directory to the encrypt_file folder
                        cwd = os.getcwd()
                        os.chdir(os.path.join(cwd, "encrypt_file"))
                        files = os.listdir()

                        with open(str(efile), 'rb') as file:
                            original = file.read()

                        encrypted = ef2.encrypt(original)

                        with open(str(efile), 'wb') as encrypted_file:
                            encrypted_file.write(encrypted)

                        print("Contents of the file have been encrypted successfully.")
                        print("Your private key is: ", ef)
                        print("Don't lose your private key, you won't be able to decrypt the file without it.")

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
                        print("You have chosen to decrypt a message!")
                        GetEmessage = input("What is the encrypted text? \nEnter Here: ")
                        GetRanKey = input("What is your key? \nEnter Here: ")

                        a = str.encode(str(GetRanKey))
                        x = Fernet(a)

                        y = str.encode(str(GetEmessage))

                        decryptedmessage = x.decrypt(y).decode()

                        print("Decrypted message: ", decryptedmessage)

                        break

                    elif IntMess == 2:
                        print("You have chosen to decrypt a file!")

                        getefile = input("What is the encrypted file? \nNote: file must be located in the encrypt_file folder\nEnter Here: ")
                        getpkey = input("What is the private key?\n Enter Here: ")

                        pkey = str.encode(str(getpkey))
                        dec = Fernet(pkey)

                        # Move active directory to the encrypt file folder
                        cwd = os.getcwd()
                        os.chdir(os.path.join(cwd, "encrypt_file"))
                        files = os.listdir()

                        with open(str(getefile), 'rb') as enc_file:
                            encrypted_stuff = enc_file.read()

                        decrypt_stuff = dec.decrypt(encrypted_stuff)

                        with open(str(getefile), 'wb') as dec_file:
                            dec_file.write(decrypt_stuff)

                        print("File successfully decrypted!")

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

