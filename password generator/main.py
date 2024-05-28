import random
import string


def generate_password(length=12):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters)for _ in range(length))
    return password
if __name__=="__main__":
    password_length=12
    try:
        password_length=int(input("Enter desired password length(default is 12): "))
    except ValueError:
        print("Invalid input. Using default password length.")
    if password_length<=0:
        print("Password length should be greater than 0. Using default password length.")
        password_length=12
    generated_password=generate_password(password_length)
    print("Generated Password:",generated_password)
    


    