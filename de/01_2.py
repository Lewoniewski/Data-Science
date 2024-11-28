passagiere = int(input("Geben Sie die Anzahl der Passagiere ein: "))

if passagiere <= 35:
    print("Wählen Sie den Bus für die Reise.")
elif passagiere <= 120:
    print("Wählen Sie den Zug für die Reise.")
else:
    print("Wählen Sie das Flugzeug für die Reise.")