import random

i = 1
n = 100
counter = 0
while i <= n:
    i = i + 1
    rechen_operator = ['+', '-', '/', '*']
    zufaellig = random.choice(rechen_operator)
    #print(zufaellig)

    ##Bei Addition, Subtraktion und Multiplikation werden ganze Zahlen zwischen 1 und 20 miteinander verknüpft.
    zahl_eins = random.randint(1, 20)
    zahl_zwei = random.randint(1, 20)

    #print(zahl_eins)
    #print(zahl_zwei)

    print(zahl_eins, zufaellig, zahl_zwei, "=")
    ##eingabe_1 = int(input("Lösung: "))
    

eingabe_1 = int(input("Ergebnis: "))


while eingabe_1 != 0:
    
    ##Rechenoperationen
    while eingabe_1 != 0:
        if zufaellig == '+':
                print(zahl_eins, "+", zahl_zwei, "=")
                eingabe_1 = int(input("Addition: "))
                ## Prüfen ob, Eingabe größer ungleich null ist
                ergebnis = zahl_eins + zahl_zwei
                if eingabe_1 == ergebnis and eingabe_1 > 0:
                            counter+=1
                            prozent = counter // (1 * 100)
                            print("Ihr Ergebnis ist richtig.", "\n", counter, "von 1 oder", prozent, "% Richtige")
                else:
                            prozent = counter // 1 * 100
                            print("Ergebnis ist falsch", "\n", counter, "von 1 oder", prozent, "% Richtige")
                            break

            
        ##Subtraktion
        ## Das Ergebnis der Subtraktion ist stets größer 0. Es kommen keine negativen Zahlen vor.
            
    ## Auf Rechenoperator pruefen
        if zufaellig == '-':
                print(zahl_eins, "-", zahl_zwei, "=")
                eingabe_1 = int(input("Subtraktion: "))
                ## Prüfen ob, Eingabe größer ungleich null ist
                ##if eingabe_1 != 0:
                ergebnis = zahl_eins - zahl_zwei
                if eingabe_1 == ergebnis and eingabe_1 > 0:
                            counter+=1
                            prozent = counter // (1 * 100)
                            print("Ihr Ergebnis ist richtig.", "\n", counter, "von 1 oder", prozent, "% Richtige")
                else:
                            prozent = counter // 1 * 100
                            print("Ergebnis ist falsch", "\n", counter, "von 1 oder", prozent, "% Richtige")
                            break
        ##Multiplikation
        ##Bei der Multiplikation kommen keine Aufgaben mit einem Faktor 1 vor
        if zufaellig == '*':
                print(zahl_eins, "*", zahl_zwei, "=")
                eingabe_1 = int(input("Multiplikation: "))
                ## Prüfen ob, Eingabe größer ungleich null ist
                ##if eingabe_1 != 0:
                ergebnis = zahl_eins * zahl_zwei
                if eingabe_1 == ergebnis and eingabe_1 > 0:
                            counter+=1
                            prozent = counter // (1 * 100)
                            print("Ihr Ergebnis ist richtig.", "\n", counter, "von 1 oder", prozent, "% Richtige")
                else:
                            prozent = counter // 1 * 100
                            print("Ergebnis ist falsch", "\n", counter, "von 1 oder", prozent, "% Richtige")
                            break
        ##Division
        ##Die Division liefert als Ergebnis immer eine ganze Zahl
        ##Bei der Division sollen Ergebnis und Nenner im Intervall zwischen 1 und 20 liegen. Aufgaben bei denen Zähler und
        ##Nenner identisch sind kommen nicht vor (Ergebnis =1 ). Ebenso werden keine Aufgaben mit einem Nenner = 1 erstellt.
        if zufaellig == '/':
                print(zahl_eins, "/", zahl_zwei, "=")
                eingabe_1 = int(input("Division: "))
                ## Prüfen ob, Eingabe größer ungleich null ist
                ##if eingabe_1 != 0:
                ergebnis = zahl_eins / zahl_zwei
                if eingabe_1 == ergebnis and eingabe_1 > 0:
                            counter+=1
                            prozent = counter // (1 * 100)
                            print("Ihr Ergebnis ist richtig.", "\n", counter, "von 1 oder", prozent, "% Richtige")
                else:
                            prozent = counter // 1 * 100
                            print("Ergebnis ist falsch", "\n", counter, "von 1 oder", prozent, "% Richtige")
                            break
    break
