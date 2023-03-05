
import random 
num = random.randint(0, 20)
num_guesses=0
guessed_number=0
guess_limit=4

while num_guesses<guess_limit:
    num_guesses +=1 
    guessed_number=int(input("Pogodi broj izmedju 0 i 20?:"))
    if (guessed_number==num):
        print(f"Pogodio si. Trazeni broj je:{guessed_number}")
        break
    elif(guessed_number>num):
        print("Pogadj ponovo. Tvoj broj je veci od ciljanog broja")
    else:
        print("Ponovo. Tvoj broj je manji od ciljanog")
else:
    print(f"Kraj igre. Trazeni broj je:{num}")
