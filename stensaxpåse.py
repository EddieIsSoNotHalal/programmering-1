
import random
from turtle import end_fill

computer = random.choice(["rock", "paper", "scissors"]).lower()

user = input("rock, paper or scissors? ").lower()

print("The computer chose", computer,"and the user chose", user +".")

if computer == user:
    print("It's a draw")

if user == ("scissors") and computer == ("paper"):
    print("You win")

if user == ("scissors") and computer == ("rock"):
    print("You lose")

if user == ("rock") and computer == ("scissors "):
    print("You win")

if user == ("rock") and computer == ("paper"):
    print("You lose")

if user == ("paper") and computer == ("rock"):
    print("You win")

if user == ("paper") and computer  == ("scissors"):
    print("You lose")



# TODO - Implement the if statements that prints who wins