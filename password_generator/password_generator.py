import random
import string
import csv

def main():
    ask_username = input("Please enter your username: ")

    ask_website = input("Please enter which site you plan to use it: ")

    while True:
        try:
            ask_password = int(input("Please enter how many characters do you want for password: "))
            
            if ask_password < 8:
                print("Must be at least 8 characters long")
            else:           
                break   
                
        except ValueError:
            print("Invalid input, Please enter a number")
        
    password = creating_password(ask_password)


    with open("credential.txt","a") as file:
        file.write(f"Hello {ask_username}, your password is: {password}\n")
        file.write(f"This is going to be used for {ask_website}\n\n")

    print(f"{ask_username} your password is now generated")


def creating_password(pw):
    characters = string.ascii_letters + string.digits + string.punctuation     

    password =''.join(random.choice(characters) for _ in range(pw))

    return password


if __name__=="__main__":
    main()