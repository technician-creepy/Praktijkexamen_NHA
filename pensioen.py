'''
functie voor het berekenen van het pensioen per week
- medewerker vanaf 65 = €350 en vanaf 70 €20 extra
- zelfstandige vanaf 65 = €300 en vanag 70 €15 extra
- ambtenaar vanaf 65 = €370 en vanaf 70 €25 extra
'''
def pensioen(statuut, leeftijd):
    if leeftijd < 65:
        return f"Van werken wordt je gelukkig, je mag nog {65 - leeftijd} jaar genieten van je baan."



# We vragen de gebruiker om zijn leeftijd en werkstatuur om het pensioen te berekenen
leeftijd = int(input("What is je leeftijd?"))
statuut = input("Wat is je werkstatuut? ")

# Een lijst met de mogelijke statuten
statuten = ["medewerker","zelfstandige","ambtenaar"]

# TEST CODE TE VERWIJDEREN VOOR INZENDEN EXAMEN
print(pensioen(statuut, leeftijd))