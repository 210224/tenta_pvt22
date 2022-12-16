import requests

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1

# Tip: use the page below to see what data we get back and how the api works
# we only use /nobelPrizes
# Documentation, help and tools for testing the api can be found here: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1


HELP_STRING = """
Ange ett år och fält
Exempelvis 1965 fysik
Tryck 2 för att lista alla fält
Tryck Q för att avsluta
Tryck H för att få en hjälpruta
"""

cat = {"fysik": "phy",
       "kemi": "che",
       "litteratur": "lit",
       "ekonomi": "eco",
       "fred": "pea",
       "medicin": "med"}

# TODO 10p programmet skall ge en hjälpsam utskrift istället för en krasch om användaren skriver in fel input
# TODO 15p om användaren inte anger ett område som exempelvis fysik eller kemi så skall den parametern inte skickas med till apiet och vi får då alla priser det året
"--------------------------------------"


# TODO 10p the program should give a helpful output instead of a crash if the user enters the wrong input
# TODO 15p if the user does not specify a field such as physics or chemistry, then that parameter should not be sent to the api and we will then receive all the prizes for that year


def main():
    print(HELP_STRING)

    while True:

        # TODO 5p Skriv bara ut hjälptexten en gång när programmet startar inte efter varje gång användaren matat in en fråga
        #      Förbättra hjälputskriften så att användaren vet vilka fält, exempelvis kemi som finns att välja på
        menu_choice = input("Välj ett fält: ")
        if menu_choice == '1':
            pass
        if menu_choice == '2':
            print("Lista med alla fält:")
            for item in cat:
                print(item)
            pass
        # TODO 5p Gör så att det finns ett sätt att avsluta programmet, om användaren skriver Q så skall programmet stängas av
        #      Beskriv i hjälptexten hur man avslutar programmet
        # TODO 5p Gör så att hjälptexten skrivs ut om användaren skriver h eller H
        "---------------------------------------"
        if menu_choice.upper() == 'H':
            print(HELP_STRING)
        if menu_choice.upper() == 'Q':
            print("Good-bye and thank you for the fish!")
            return
        # TODO 5p Only print the help text once when the program does not start after each time the user enters a question
        # Improve the help printout so that the user knows which fields, for example chemistry, are available to choose from

        # TODO 5p Make sure there is a way to terminate the program, if the user types Q the program should be shut down
        # Describe in the help text how to end the program
        # TODO 5p Make the help text printed if the user types h or H



if __name__ == '__main__':
    main()