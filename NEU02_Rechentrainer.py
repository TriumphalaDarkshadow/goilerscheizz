import random


"""Die Aufgabe Rechentrainer aus dem Workshop02

    erstellt: 09.04.2019
    author: ######
"""

##erst werden zwei Random Zahlen erzeugt
##anschließend ein Rechenzeichen
##Dann wird Aufgabe aus den beiden Zahlen + Rechenzeichen ausgegeben
##dann kann user antwort eingeben. ist antwort 0, wird die schleife verlassen

print("Training der vier Grundrechenarten:","\n","- Geben Sie jeweils die Lösung der Aufgabe ein.", "\n", "- Zum Beenden des Trainings geben Sie als Lösung die 0 ein.")

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

    ##Bei Addition, Subtraktion und Multiplikation werden ganze Zahlen zwischen 1 und 20 miteinander verknüpft.
    zahl_eins = random.randint(1, 20)
    zahl_zwei = random.randint(1, 20)

    print(zahl_eins)
    print(zahl_zwei)

    print(zahl_eins, zufaellig, zahl_zwei, "=")
    eingabe_1 = int(input("Lösung: "))
    break
##Programm soll automatisch Aufgabe erstellen

##Solange Eingabe nicht 0 ist, ansonsten Abbruchbedingung
##while Schleife: Skript wird solange ausgefüllt, bis User eingabe_01 = 0 eingibt

##if eingabe_1 != 0:
    
    ##Addition

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
if eingabe_1 == 0:
    print("Das Rechentraining ist beendet.")
##else:
  ## print("Das Rechentraining ist beendet."
      ##   "\n", "Sie haben von 7 Aufgaben", prozent, "korrekt gelöst") 
        
    ##eingabe_8 = int(input("7 + 16 = ")
    ##if eingabe_8 == 0:
       ## print("Das Rechentraining ist beendet."
         ##   "\n", "Sie haben von 7 Aufgaben", prozent, "korrekt gelöst")

    #natürliche Divison also Zähler ist ein Vielfaches vom Nenner -> Ergebnis ist ganze Zahl
        #nicht abrunden oder Nachkommastellen abschneiden
        #Division ohne Rest prüfen mit 
