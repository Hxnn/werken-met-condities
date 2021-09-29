print('Welkom bij de sollicitatie! Beantwoord deze vragen!')

Ervaring = int(input('Hoeveel jaar heeft u in de praktijkervaring met dieren-dressuur '))
Ervaring2 = int(input('Hoeveel jaar ervaring heeft u met jongleren? '))
Ervaring3 = int(input('Hoeveel jaar heeft u praktijkevaring met acrobatiek? '))
Diploma = str(input('Heeft u een MBO-4 diploma ondernemen? (y/n) '))
Rijbewijs = str(input('Heeft u een Vrachtwagen rijbewijs? (y/n) '))
Hoed = str(input('Heeft u een hoge hoed? (y/n) '))
lengteS = 10
lengteH = 20
haar = "y"
snor = "y"
Man = str(input('Wat is uw geslacht? (m/v) '))
if Man == "m":
    snor = str(input('Heeft u een snor? (y/n) '))
    if snor == "y":
        lengteS = int(input('Hoe breed is uw snor? '))
else:
    haar = str(input('Heeft u rood krullend haar? (y/n) '))
    if haar == "y":
        lengteH = int(input('Hoelang is uw haar? '))

Lengte = str(input('Hoelang bent u in cm? '))
Gewicht = str(input('Wat is uw gewicht? '))
Certificaat = str(input('Heeft u de certificaat "Overleven met gevaarlijk personeel?" (y/n) '))
Vakantie = str(input('Gaat u vaak op vakantie? (y/n) '))
Huisdieren = int(input("Hoevele huisdieren heeft u? "))
Alergieen = str(input('Heeft u allergieën? (y/n) '))
Huis = str(input('Woont u in een huis of appartement? '))
if int(Ervaring) <= 3 or int(Ervaring2) <= 4 or int(Ervaring3) <= 3 or Diploma == "n" or Rijbewijs == "n" or Hoed == "n"\
    or (snor == "n" and int(lengteS <= 9) or
        (haar == "n" and int(LengteH <= 19) or int(Lengte) <= 150 or int(Gewicht) <= 90 or Certificaat == "n")):
    print("Wij kunnen u helaas niet aannemen! Sucks to suck")
else:
    print("Gefeliciteerd! U bent aangenomen!")
