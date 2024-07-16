# Een lijst met de mogelijke statuten
statuten = ["medewerker","zelfstandige","ambtenaar"]

'''
functie voor het berekenen van het pensioen per week
- medewerker vanaf 65 = €350 en vanaf 70 €20 extra
- zelfstandige vanaf 65 = €300 en vanag 70 €15 extra
- ambtenaar vanaf 65 = €370 en vanaf 70 €25 extra
'''

def pensioen(statuut, leeftijd):
    if leeftijd < 65:   # Persoon is jonger dan 65 en dus nog niet pensioensgerechtigd 
        return f"Van werken wordt je gelukkig, je mag nog {65 - leeftijd} jaar genieten van je baan."
    
    # Persoon is wel pensioensgerechtigd, we berekenen het persion op basis van de leeftijd 
    # (tussen 65 en 69 krijgen ze het standaard bedrag voor hun statuut en vanaf 70 komt daar
    # een extra bedrag bij.)
    if statuut == "medewerker" and leeftijd < 70:
        pensioen_per_week = 350
    if statuut == "medewerker" and leeftijd >= 70:
        pensioen_per_week = 370
    if statuut == "zelfstandige" and leeftijd < 70:
        pensioen_per_week = 300
    if statuut == "zelfstandige" and leeftijd >= 70:
        pensioen_per_week = 315
    if statuut == "ambtenaar" and leeftijd < 70:
        pensioen_per_week = 370
    if statuut == "ambtenaar" and leeftijd >= 70:
        pensioen_per_week = 395  
    return f"Je krijgt € {pensioen_per_week} per week."

# We vragen de gebruiker om zijn leeftijd en werkstatuur om het pensioen te berekenen
leeftijd = int(input("What is je leeftijd? "))
statuut = input("Wat is je werkstatuut? ")

# We tonen op het scherm het bedrag dat de persoon per week krijgt als pensioen,
# tenzij deze nog geen 65 jaar is, dan komt er een melding dat ze nog x-aantal
# jaren mogen werken.
print(pensioen(statuut, leeftijd))