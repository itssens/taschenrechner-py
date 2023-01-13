import os

print("""
__________              .__                         
\______   \ ____   ____ |  |__   ____   ___________ 
 |       _// __ \_/ ___\|  |  \ /    \_/ __ \_  __ 
 |    |   \  ___/\  \___|   Y  \   |  \  ___/|  | \/
 |____|_  /\___  >\___  >___|  /___|  /\___  >__|   
        \/     \/     \/     \/     \/     \/
     """)
print("Rechenart Auswählen auswählen")
print("1.Addieren")
print("2.Subtrahieren")
print("3.Multiplizieren")
print("4.Dividieren")

def löschen():
    os.system('cls' if os.name == 'nt' else 'clear')

def addieren(x, y):
    return x + y

def subtrahieren(x, y):
    return x - y

def dividieren(x, y):
    return x / y

def multiplizieren(x, y):
    return x * y
    
while True:
    antwort = input("Auswahl eingeben(1/2/3/4): ")

    if antwort in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Gebe die erste Zahl ein: "))
            num2 = float(input("Gebe die zweite Zahl ein: "))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Gültige Zahl ein.")
            continue

        if antwort == '1':
            löschen()
            print(num1, "+", num2, "=", addieren(num1, num2))

        elif choice == '2':
            löschen()
            print(num1, "-", num2, "=", subtrahieren(num1, num2))

        elif choice == '3':
            löschen()
            print(num1, "*", num2, "=", multiplizieren(num1, num2))

        elif choice == '4':
            löschen()
            print(num1, "/", num2, "=", dividieren(num1, num2))
        
        nochmal = input("Noch eine Berechnung? (ja/nein): ")
        if nochmal == "nein":
          break
        else:
            print("Ungültige Eingabe.")
    else:
        print("Ungültige Eingabe.")
