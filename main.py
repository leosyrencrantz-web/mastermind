import random
print("Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6\n Du ska försöka gissa denna kods siffror på max 12 drag\nEfter respektive gissning så kommer du få en respons:\nFör varje korrekt gissad siffra på korrekt plats i koden:\nFör varje korrekt gissad siffra på fel plats i koden:\nför dem siffror som inte finns med i koden ges ingen markering")

print("\n\nDu får välja mellan två svårighetsnivåer:\nLättare nivå: Alla siffror är garanterat olika\nSvårare nivå: Det kan finnas en upprepning av en eller flera siffror")

gissningar_list = []
feedback_list = []
while True:
    nivå = int(input("Ange önskad nivå: lättare (1), svårare (2) ->"))
    if nivå == 1 or nivå == 2 :
        break
    else :
        None

i = 0 
rand_num = []
if nivå == 1 :
    print("WEAK")
    while i < 4 :
        rand = random.randint(0,9)
        if rand in rand_num :
            continue
        else :
            rand_num.append(rand)
        i = i + 1

    



elif nivå == 2 :
    print("UR GONNA REGRET THIS :3")
    while i < 4 :
        rand = random.randint(0,9)
        rand_num.append(rand)
        i = i + 1

print(rand_num)

antal_omgångar = 12
antal_omgångar_körda = 0
while antal_omgångar_körda  < antal_omgångar :
    while True :
        gissning = input("Ange gissning som följd av fyra siffror ->")
        if len(gissning) == 4 and gissning.isdigit() :
            break
        else :
            print("kom ihåg endast 4")
            None
    print("this has endend") 
    print(gissning)
    gissningar_list.append(gissning)
    
    exakt_rätt = 0
    fel_plats = 0
    i = 0
    while i< 4 or 1 == 4 :
        if rand_num[i] == int(gissning[i]) :
            exakt_rätt = exakt_rätt + 1
        elif int(gissning[i]) in rand_num :
            fel_plats = fel_plats + 1
        else :
            None
        i = i + 1 
    

    feedback = f"{"Y"*exakt_rätt}{"H"*fel_plats}"
    feedback_list.append(feedback)  
    print(f"DRAG#        Drag        Feedback")
    
    for i in range(antal_omgångar_körda+1) :
        print(i+1)
        print(gissningar_list[i])
        print(feedback_list[i])







    antal_omgångar_körda  = antal_omgångar_körda  + 1
