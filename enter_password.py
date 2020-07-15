import random
from past.builtins import raw_input


print("Keep it logically awesome.")

f = open("password.txt")
prompt = raw_input("Please enter your password: ")
currentPWD = f.read()

if prompt == currentPWD:
  print("Correct password!")

else:
  print("Incorrect password!")

f.close()