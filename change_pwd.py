import random
def uno():
  print("Change password")

  f = open("password.txt", "w")
  f.write(input("Enter your new password: "))
  # Don't exit the file after opening otherwise the password.txt file will be blank
  f.close()
  f = open("password.txt")
  currentPWD = f.read()
  print("Your new password is: " + currentPWD)

if __name__== "__main__":
  uno()
