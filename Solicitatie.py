print('Welkom bij de sollicitatie! Beantwoord deze vragen!')

Ervaring = input('Hoeveel jaar heeft u in de praktijkervaring met dieren-dressuur ')
if int(Ervaring) >= 4:
    Ervaring2 = input('Hoeveel jaar ervaring heeft u met jongleren? ')
    if int(Ervaring2) >= 5:
        Ervaring3: str = input('Hoeveel jaar heeft u praktijkervaring met acrobatiek? ')
    var = int(Ervaring3) >= 3 or int(Ervaring) >= 4 or int(Ervaring2) >= 5
    Diploma = input('Heeft u een MBO-4 diploma ondernemen? (y/n) ')
    if Diploma == "y":
        Rijbewijs = input('Heeft u een Vrachtwagen rijbewijs? (y/n) ')
        if Rijbewijs == "y":
                Hoed: str = input('Heeft u een hoge hoed? (y/n) ')
        if Hoed == "y":
                Man: str = input('Wat is uw geslacht? (m/v) ')
        if Man == "m":
                Snor: str = input('Heeft u een snor breder dan 10cm? (y/n) ')
        if Man == "v":
                Snor: str = input('Heeft u rood krullend haar langer dan 20cm? (y/n) ')
        if Snor == "y":
                Lengte: str = input('Hoelang bent u in cm? ')
        if int(Lengte) >= 150:
                Gewicht: str = input('Wat is uw gewicht? ')
        if int(Gewicht) >= 90:
                Certificaat: str = input('Heeft u de certificaat "Overleven met gevaarlijk personeel?" (y/n)')
        if Certificaat == "y":
                print('Gefeliciteerd! U bent aangenomen!')
        elif int(Ervaring3) <= 3 or Diploma == "n" or Rijbewijs == "n" or Hoed == "n" or Snor == "n" or int(Lengte) <= 150 or int(Gewicht) <= 90 or Certificaat == "n":
            print('Wij kunnen u helaas niet aannemen!')