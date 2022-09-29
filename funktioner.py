# Övning 3 går ut på att implementera så många av nedanstående funktioner som möjligt
# Ta bort pass och implementera funktionerna


def best(name):
    # TODO Skriv ut att namnet är bäst
    # Ex: "Katherine" in - skriver ut "Katherine är bäst"
    return (name,"är bäst")
print(best("Hampus"))


def square(number):
    # TODO Returnera talet kvadrerat
    # Ex: 5 in - 25 ut  
    return number**2
print(square(5))


def sums(a, b):
    # TODO Returnera summan av a och b
    # Ex: 2, 6 in - 8 ut
 return a+b

print(sums(5,6))


# Nu blir det lite svårare


def maximum(a, b, c):
    # TODO Returnera det största av a,b,c
    # Ex: 3, 6, 12 in - 12 ut
    if a>b and c:
        return a
    elif b>c:
        return b
    else:
        return c
print(maximum(2,3,4))





def palindrom(ord):
    # TODO Returnera True om ord är ett palindrom
    # Ex: abba in - True ut
    # Palindrom är ett ord som stavas likadant baklänges och framlänges.
    if ord == ord[::-1]:
        return(True)
    else:
        return(False)
print(palindrom("hampus"))
print(palindrom("racecar"))


def prime(nr):
    # TODO Returnera True om nr är ett primtal, annars returnera false
    # Ex: 5 in - True ut
   pass