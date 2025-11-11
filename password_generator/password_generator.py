import random
import string

def main():
    ask_username = input("Please enter your username: ")

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

    print(f"Hello : {ask_username}, your generated password is : {password}")


def creating_password(pw):
    characters = string.ascii_letters + string.digits + string.punctuation     

    password =''.join(random.choice(characters) for _ in range(pw))

    return password


if __name__=="__main__":
    main()