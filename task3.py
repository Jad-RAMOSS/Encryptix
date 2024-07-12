import random
import string 

def generatePassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)for _ in range(length))
    return password

def userInput():
    while True:
        try:
            length = int(input("Enter your desired length for the password: "))
            if length <6:
                raise ValueError("Password length must be at least 6 characters")
            return length
        except ValueError as e:
            print(e)

def printPassword(password):
    print(f"Generated Password: {password}")
    
def main():
    length = userInput()
    password = generatePassword(length)
    printPassword(password)

if __name__ == "__main__":
    main()