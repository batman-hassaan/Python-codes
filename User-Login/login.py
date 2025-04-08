
def account():
    name = input("enter username : ")
    while len(name) != 5:
        print("the username should be 5 character long")
        name = input("enter username : ")
    
    password = input("enter password 6 character long : ")
    while not (len(password)==6 and any(char.isdigit() for char in password) and any(char.islower() for char in password) and any(char.isupper() for char in password)):
             password = input("enter password 6 character long : ")         
    print("account successfully created")
    return name ,password

def login(correct_username, correct_password):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print(f"Hi {username} you are logged in.")
    else:
        print("The username or password is incorrect.")

# main program
print("Welcome to User Registration System")
a = input("do you want to make an account(yes/no) : ").lower()
if a == "yes":
      name,password = account()
      login(name,password)
elif a =="no":
      print("thank you")
else:
      print("invalid input")      
