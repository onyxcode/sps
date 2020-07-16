from past.builtins import raw_input


# yes
def menu():
  print("Press (1) to change a password. | Press (2) to enter your password.")
  prompt = raw_input("What would you like to do?\n")

  if prompt == "1":
    change()
  if prompt == "2":
    enter()
  else:
    print("That is not a valid option!")



def change():
  from passlib.context import CryptContext
  print("Change password")
  prompt = raw_input("Please confirm your old password to continue: ")
  f = open("password.txt")
  currentPWD = f.read()

  if prompt == currentPWD:
    print("Correct password!")

  else:
    print("Incorrect password!")
    exit(0)

  f = open("password.txt", "w")
  f.write(input("Enter your new password: "))
  # Don't exit the file after opening otherwise the password.txt file will be blank
  f.close()
  f = open("password.txt")
  currentPWD = f.read()
  print("Your new password is: " + currentPWD)
  menu()


def enter():
  print("Welcome.")

  f = open("password.txt")
  # Default password is "apple"
  prompt = raw_input("Please enter your password: ")
  currentPWD = f.read()

  if prompt == currentPWD:
    print("Correct password!")

  else:
    print("Incorrect password!")

  f.close()

  menu()


menu()