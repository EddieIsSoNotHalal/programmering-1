
import random
from traceback import print_last
from turtle import end_fill


print("Välkommen till THE ULTIMATE HÄNGAGUBBEN GAME!!") 
input("Tryck Enter för att börja")

word = random.choice(["skola", "reinhold", "bänkpress", "mattebok", "programmering"])

guessword = '_' * len(word)
print (guessword)

lettersguessed = []

lives = 8

while lives > 0:
    guessletter = input("Skriv in en bokstav: ")
        
    if guessletter in word:
            print("Korrekt!! Bokstaven som du gissade finns i ordet")
            print()
    else:
        lives -=1 
        lettersguessed.append(guessletter)
        print(f"Tyvärr bokstaven {guessletter} finns inte med. Du har {lives} försök kvar")
        print(f"De här bokstäverna har du gissat på som var inkorrekta {lettersguessed}")

