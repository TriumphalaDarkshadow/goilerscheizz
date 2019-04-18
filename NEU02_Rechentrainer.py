import random


"""Die Aufgabe Rechentrainer aus dem Workshop02

    erstellt: 09.04.2019
    author: ######
"""

##erst werden zwei Random Zahlen erzeugt
##anschliesend ein Rechenzeichen
##Dann wird Aufgabe aus den beiden Zahlen + Rechenzeichen ausgegeben
##dann kann user antwort eingeben. ist antwort 0, wird die schleife verlassen

print("Training der vier Grundrechenarten:","\n","- Geben Sie jeweils die Loesung der Aufgabe ein.", "\n", "- Zum Beenden des Trainings geben Sie als Loesung die 0 ein.")

print("\n")

##Zaehlen von Aufgaben
counter = 0

n = 100
i = 1
##Zufallsrechenoperator

##while Schleife fuer zufaellige Zahlen und Rechenoperator -> es wird immer dieselben zwei
##Zahlen ausgegebn
while i <= n:
    i = i + 1
    rechen_operator = ['+', '-', '/', '*']
    zufaellig = random.choice(rechen_operator)
    print(zufaellig)

    ##Bei Addition, Subtraktion und Multiplikation werden ganze Zahlen zwischen 1 und 20 miteinander verknuepft.
    zahl_eins = random.randint(1, 20)
    zahl_zwei = random.randint(1, 20)

    
    #print(zahl_eins)
    #print(zahl_zwei)

    print(str(zahl_eins) + " " + zufaellig + " " + str(zahl_zwei) + " " + "=")
    eingabe_1 = float(input("Loesung: "))
    
##Programm soll automatisch Aufgabe erstellen

##Solange Eingabe nicht 0 ist, ansonsten Abbruchbedingung
##while Schleife: Skript wird solange ausgefuellt, bis User eingabe_01 = 0 eingibt

##if eingabe_1 != 0:
    
    ##Addition

    while eingabe_1 != 0:
        if zufaellig == '+':
                   # print(zahl_eins + "+"+ zahl_zwei + "=")
                   # eingabe_1 = int(input("Addition: "))
                    ## Pruefen ob, Eingabe groeser ungleich null ist
                    ergebnis = zahl_eins + zahl_zwei
                    if eingabe_1 == ergebnis and eingabe_1 > 0:
                                counter+=1
                                prozent = counter // (1 * 100)
                                print("Ihr Ergebnis ist richtig.", "\n", counter, "von ", str(i-1), "oder", prozent, "% Richtige")
                                break
                    else:
                                prozent = counter // 1 * 100
                                print("Ihr Ergebnis ist falsch.", "\n", counter, "von ", str(i-1), "oder", prozent, "% Richtige")
                                break

                
            ##Subtraktion
            ## Das Ergebnis der Subtraktion ist stets groeser 0. Es kommen keine negativen Zahlen vor.
                
        ## Auf Rechenoperator pruefen
        if zufaellig == '-':
                   # print(zahl_eins, "-", zahl_zwei, "=")
                   # eingabe_1 = int(input("Subtraktion: "))
                    ## Pruefen ob, Eingabe groeser ungleich null ist
                    ##if eingabe_1 != 0:
                    ergebnis = zahl_eins - zahl_zwei
                    if eingabe_1 == ergebnis and eingabe_1:
                                counter+=1
                                prozent = counter // (1 * 100)
                                print("Ihr Ergebnis ist richtig.", "\n", counter, "von ", str(i-1), "oder", prozent, "% Richtige")
                                break
                    else:
                                prozent = counter // 1 * 100
                                print("Ihr Ergebnis ist falsch.", "\n", counter, "von ", str(i-1), "oder", prozent, "% R#ichtige")
                                break
            ##Multiplikation
            ##Bei der Multiplikation kommen keine Aufgaben mit einem Faktor 1 vor
        if zufaellig == '*':
                    #print(zahl_eins, "*", zahl_zwei, "=")
                    #eingabe_1 = int(input("Multiplikation: "))
                    ## Pruefen ob, Eingabe grer ungleich null ist
                    ##if eingabe_1 != 0:
                    ergebnis = zahl_eins * zahl_zwei
                    if eingabe_1 == ergebnis and eingabe_1:
                                counter+=1
                                prozent = counter // (1 * 100)
                                print("Ihr Ergebnis ist richtig.", "\n", counter, "von ", str(i-1), "oder", prozent, "% Richtige")
                                break
                    else:
                                prozent = counter // 1 * 100
                                print("Ihr Ergebnis ist falsch.", "\n", counter, "von ", str(i-1), "oder", prozent, "% Richtige")
                                break
                            
            ##Division
            ##Die Division liefert als Ergebnis immer eine ganze Zahl
            ##Bei der Division sollen Ergebnis und Nenner im Intervall zwischen 1 und 20 liegen. Aufgaben bei denen Zhler und
            ##Nenner identisch sind kommen nicht vor (Ergebnis =1 ). Ebenso werden keine Aufgaben mit einem Nenner = 1 erstellt.
        if zufaellig == '/':
                    #print(zahl_eins, "/", zahl_zwei, "=")
                    #eingabe_1 = int(input("Division: "))
                    ## Prfen ob, Eingabe grer ungleich null ist
                    ##if eingabe_1 != 0:
                    ergebnis = zahl_eins / zahl_zwei
                    if eingabe_1 == ergebnis and eingabe_1:
                                counter+=1
                                prozent = counter // (1 * 100)
                                print("Ihr Ergebnis ist richtig.", "\n", counter, "von ", str(i-1), "oder", prozent, "% Richtige")
                                break
                    else:
                                prozent = counter // 1 * 100
                                print("Ihr Ergebnis ist falsch.", "\n", counter, "von ", str(i-1), "oder", prozent, "% Richtige")
                                break
    if eingabe_1 == 0:
        print("Das Rechentraining ist beendet.")
##else:
  ## print("Das Rechentraining ist beendet."
      ##   "\n", "Sie haben von 7 Aufgaben", prozent, "korrekt gelst") 
        
    ##eingabe_8 = int(input("7 + 16 = ")
    ##if eingabe_8 == 0:
       ## print("Das Rechentraining ist beendet."
         ##   "\n", "Sie haben von 7 Aufgaben", prozent, "korrekt gelst")

    #natrliche Divison also Zhler ist ein Vielfaches vom Nenner -> Ergebnis ist ganze Zahl
        #nicht abrunden oder Nachkommastellen abschneiden
        #Division ohne Rest prfen mit 
