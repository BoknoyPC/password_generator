import random
import string

def main():
    ask_username = input("Please enter your username: ")

    ask_password = int(input("Please enter how many characters do you want for password: "))

    password = creating_password(ask_password)

    print(f"Hello your username is : {ask_username}, your generated password is : {password}")


def creating_password(pw):
    characters = string.ascii_letters + string.digits + string.punctuation     

    password =''.join(random.choice(characters) for _ in range(pw))

    return password


if __name__=="__main__":
    main()