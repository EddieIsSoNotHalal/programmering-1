# Travelbag
# Skelettkod till uppgiften

travelbag = []

while True:
   menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program")

   if menyval == "1":
       print(*travelbag)

   elif menyval == "2":
     tjenare = input("Vad vill du lägga till?").split(" ")
     print(tjenare)
     travelbag.append(tjenare)

   elif menyval == "3":
       goddag = input("Vad vill du ta bort?").split(" ")
       print(goddag)
       travelbag.remove(goddag)

   elif menyval == "4":
       break