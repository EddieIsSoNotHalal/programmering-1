import random


#skottår

def skottår(år):
    if år %4 != 0:
        return(år,"är inte ett skottår")
    elif år %400 != 0 and år %100 == 0:
        return(år, "är inte ett skottår")
    else:
        return(år,"är ett skottår")

år = int(input("Skriv in ett årtal "))
print(skottår(år))



#pyramid

nr = int(input("Gimme a number ")) 
for i in range(nr):
    for j in range(i+1):
        print(j+1, end=" ") 
    print("")


#gissa number

list = range(1,101)
nr = random.choice(list)
guess = int(input("GIMME A NUMBER"))

while guess != nr:
    if guess > nr:
        print("LOWER")
    elif guess < nr:
        print("HIGHER")
print("CORRECT")


#login

accounts = {}
logged_in = False
tries = 3

while True:
    menyval = input(
        "1. Skapa konto\n"
        "2. Logga in\n"
        "3. Läs en rolig historia\n"
        "4. Logga ut\n"
        "5. Avsluta program\n"
    )

    if menyval == "1":

        username = input("Create a username: ")
        
        if username in accounts:
            print("A account with given username already exists")
        
        else:
            password = input("Create a password: ")
            accounts.update({username: password})
            print("Account was successfully created")
    

    elif menyval == "2":

        if logged_in == True:
                print("You are already logged in")
        else:
            while tries > 0:
            
                user_login = input("Enter your username: ")
                
                if user_login not in accounts:
                    print("A account with given username does not exist")
                else:
                    pswrd_login = input("Enter your password: ")  


                if user_login in accounts:
                    if accounts[user_login] == pswrd_login:
                        logged_in = True
                        print(f"Welcome {user_login}!")
                        break

                    if logged_in == False:
                        tries -=1
                        print(f"The given password is wrong. You have {tries} tries left.")




    elif menyval == "3":
        if logged_in == True:
            print("""Here is your reward for being logged in. This is santas number: 0700622318.\nCall him an he will get you whatever you want for christmas""")
        else:
            print("I dont have any reward for you. Try to log in and check if something is waiting for you")

        

   
    elif menyval == "4":
        if logged_in == True:
            log_out = input("Are you certain that you want to log out? ").capitalize()
            if log_out == "Yes":
                logged_in = False
                print("You have successfully logged out")
            if log_out == "No":
                continue        
        else:
            print("You can't log out if you are not logged in")
            

    elif menyval == "5":
        break