
from ctypes.wintypes import WORD


print("Hur gammal är du?")
år = int(input("År:"))
månader = int(input("Månader:"))

sec = 60*60*24*365*år + 60*60*24*30*månader

print(f"Du är {sec} sekunder gammal")
 
x = int(input("vilket tal vill du kvadrera?"))
print(x*x)