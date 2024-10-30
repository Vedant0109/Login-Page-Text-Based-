import json
from time import sleep


def register(dictionary):
  username= input("Enter your username: ")
  while len(username)<=7:
    print("Your username should be atleast of 8 digits")
    username=input("Re-Enter your username: ")
  while username in u_p:
    print("Username already taken try anthor")
    username=input("Re-Enter your username: ")
  print(f"Your username is {username}")
  password= input("Enter your password: ")
  while len(password)<=7:
    print("Your password should be of atleast 8 words")
    password=input("Re-Enter your password: ")
  print(f"Your password is {password}")
  u_p[username]=password # appends username and password to dictionary 
  with open("thing.json", "w") as file:
    json.dump(u_p , file)
  print("You successfully registered")
  sleep(3)




def login(dictionary):
  username = input("Enter your username: ")
  while username not in u_p:
      print("Username not found")
      username = input("Enter your username: ")
  password= u_p[username]
  t_password= input("Enter your password: ")
  while t_password!=password:
    print("Wrong password")
    t_password=input("Re-Enter your password: ")
  print("You Succesfully logged In.")



def change_password(dictionary):
  username = input("Enter your username: ")
  while username not in u_p:
      print("Username not found")
      username = input("Enter your username: ")
  password= u_p[username]
  n_password= input("Enter your new password: ")
  while n_password==password:
    print("Your original password can't be your new password")
    n_password= input("Enter your password: ")
  while len(n_password)<=7:
    print("Your password should be of atleast 8 words")
    n_password=input("Re-Enter your password: ")
  u_p[username]=n_password
  print("Successfully changed your password")
  with open("thing.json", "w") as file:
    json.dump(u_p , file)



with open('thing.json', 'r') as file:
    u_p = json.load(file)
print("Welcome , this is a login page")

sleep(3)

choice1=None

while choice1 != "q":
  choice1= input("1. Regster\n2. Login\n3. Change password\nq to qu ")
  if choice1=="1":
    register(u_p)

  elif choice1=="2":
    login(u_p)
      
        
  elif choice1=="3":
    change_password(u_p)

  elif choice1=="q":
    break

  else:
    print("Invalid input")