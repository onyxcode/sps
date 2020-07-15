import random
def primary():
  print("Change password")

  f = open("password.txt", "w")
  f.write(input("Enter your new password: "))
  f.close()
  f = open("password.txt")
  currentPWD = f.read()
  print("Your new password is: " + currentPWD)

if __name__== "__main__":
  primary()