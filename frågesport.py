#FREEEDDIE

score = 0

print("Welcome to the ultimate frågesport by Robert Kwiefogwqr9")
name = input("What's your name?")
print("Hello", name+"!")
wannaplay = input("Do you want to play?").lower()
if wannaplay == "yes":
    print("okay letsgo")
else: 
    print("Fuck you. You have no choice")

question1 = input("Who is the former Mr.Olympia and the former governor of California?").capitalize()

if question1 == ("Arnold" or "Schwarzenegger" or "Arnold Schwarzenegger"):
    score =+1 
    print(f"Correct! You have {score} points")
else: 
    print (f"Wrong answer! Your score is still {score} points")

question2 = input("Wchich ice cream is Eddie favorite?").capitalize()

if question2 == ("Nogger"):
    score =+1
    print (f"Correct! You have {score} points")
else:
    print(f"Wrong answer! Your score is still {score} points")

question3 = input("What is Eddie?").capitalize()

if question3 == ("Human"):
    score =+1
    print("Correct")
else:
    print("Wrong answer")

print(f"Your final score is {score}/3 points")