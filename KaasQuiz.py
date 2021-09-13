print('Welkom bij de "belangrijkste" quiz van je leven')
Kaas = input('Is de kaas geel? (y/n) ')

if Kaas == "y":
    Gaten = input('Zitten er gaten in? (y/n) ')
    if Gaten == "y":
        Duur = input('Is de kaas belachelijk duur? (y/n) ')
        if Duur == "y": print('Emmenthaler')
        else: print('Leerdammer')
    elif Gaten == "n":
        Hard = input('Is de kaas hard als een steen? (y/n) ')
        if Hard == "y": print('Pammigiano Reggiano')
        else: print('Goudse Kaas')
if Kaas == "n":
    Schimmels = input('Heeft de kaas blauwe schimmels? (y/n) ')
    if Schimmels == "y":
        Korst1 = input('Heeft de kaas een korst? (y/n) ')
        if Korst1 == "y": print('Bleu de Rochbaron')
        else: print("Foume d'Ambert")
    elif Schimmels == "n":
        Korst2 = input('Heeft de kaas een korst? (y/n) ')
        if Korst2 == "y": print('Camembert')
        else: print('Mozzarella')