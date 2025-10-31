import random

input1 = input("Type in Rock, Paper, or Scissors: ")

input2 = input1.lower()

robotinput = random.randint(1, 3)

robotinputstr = 0

if robotinput == 1:
  robotinputstr = "rock"
elif robotinput == 2:
  robotinputstr = "paper"
elif robotinput == 3:
  robotinputstr = "scissors"

if input1 == "rock" and robotinputstr == "paper":
  print("You chosed rock and the robot chose paper. You lose.")
elif input1 == "paper" and robotinputstr == "scissors":
  print("You chosed paper and the robot chose scissors. You lose.")  
elif input1 == "scissors" and robotinputstr == "rock":
  print("You chosed scissors and the robot chose rock. You lose.")
elif input1  == "rock" and robotinputstr == "scissors":
  print("You chosed rock and the robot chose scissors. You win.")
elif input1 == "paper" and robotinputstr == "rock":
  print("You chosed paper and the robot chose rock. You win.")
elif input1 == "scissors" and robotinputstr == "paper":
  print("You chosed scissors and the robot chose paper. You win.")
elif input1 == "rock" and robotinputstr == "rock":
  print("You chosed rock and the robot chose rock. You tie.")
elif  input1 == "paper" and robotinputstr == "paper":
  print("You chosed paper and the robot chose paper. You tie.")
elif input1 == "scissors" and robotinputstr == "scissors":
  print("You chosed scissors and the robot chose scissors. You tie.")


