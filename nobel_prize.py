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

# Bekräfta att önskat fält finns i listan
def checkFalt(field: str):
    if field not in cat:
        return False
    else:
        return True

# prisberäkning
#  variables: pris: totala pris
#             pris_del: fördelning mellan vinnare
#
def beraknaVinstPengar(pris: float, pris_del: float):
    summaPerVinnare = pris / pris_del
    res = round(summaPerVinnare, 3)
    return res

# utskrift år och fält
def utskriftArochFalt(year: int, field: str):
    res = getInforamationFromServer(int(year), field)

    for p in res["nobelPrizes"]:
        print("----------------------------")
        peng = p["prizeAmount"]
        idagpeng = p["prizeAmountAdjusted"]
        print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")
        prize_cnt = 0

        for m in p["laureates"]:
            print("----------------------------")
            if "knownName" in m:
                print(m['knownName']['en'])
            print(m['motivation']['en'])
            andel = m['portion']
            prize_cnt += 1
        print("*" * 30)
        money_for_thattime = calcMoneyForEachPrize(peng, prize_cnt)
        result1 = f'{money_for_thattime:.3f}'
        print(f"The money of the time for each prizer is {result1}")

        money_for_now = calcMoneyForEachPrize(idagpeng, prize_cnt)
        result2 = f'{money_for_now:.3f}'
        print(f"The Today's value for each prizer is {result2}")





def main():
    print(HELP_STRING)

    while True:

        # TODO 5p Skriv bara ut hjälptexten en gång när programmet startar inte efter varje gång användaren matat in en fråga
        #      Förbättra hjälputskriften så att användaren vet vilka fält, exempelvis kemi som finns att välja på
        menu_choice = input("Skriv önskat årtal och vilket fält efter: ")
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

        aaa = input(">")
        a, b = aaa.split()
        c = cat[b]

        c = {"nobelPrizeYear": int(a), "nobelPrizeCategory": c}

        res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=c).json()
        # TODO 5p  Lägg till någon typ av avskiljare mellan pristagare, exempelvis --------------------------

        # TODO 20p Skriv ut hur mycket pengar varje pristagare fick, tänk på att en del priser delas mellan flera mottagare, skriv ut både i dåtidens pengar och dagens värde
        #   Skriv ut med tre decimalers precision. exempel 534515.123
        #   Skapa en funktion som hanterar uträkningen av prispengar och skapa minst ett enhetestest för den funktionen
        #   Tips, titta på variabeln andel
        # Feynman fick exempelvis 1/3 av priset i fysik 1965, vilket borde gett ungefär 282000/3 kronor i dåtidens penningvärde

        for p in res["nobelPrizes"]:
            peng = p["prizeAmount"]
            idagpeng = p["prizeAmountAdjusted"]
            print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")

            for m in p["laureates"]:
                print(m['knownName']['en'])
                print(m['motivation']['en'])
                andel = m['portion']

if __name__ == '__main__':
    main()