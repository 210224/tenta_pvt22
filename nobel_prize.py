import requests

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1

# Tip: use the page below to see what data we get back and how the api works
# we only use /nobelPrizes
# Documentation, help and tools for testing the api can be found here: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1


HELP_STRING = """
Tryck 1 Ange ett år och fält - Exempelvis 1965 fysik
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


def printResult(peng: float, idagPeng: float, prize_cnt:int):
    print("*" * 30)
    pengarVarde_Ar = beraknaVinstPengar(peng, prize_cnt)
    result1 = f'{pengarVarde_Ar:.3f}'
    print(f"Prissummans värde då: {result1}")

    pengarVarde_idag = beraknaVinstPengar(idagPeng, prize_cnt)
    result2 = f'{pengarVarde_idag:.3f}'
    print(f"Prissummans värde idag: {result2}")


# hämta vinnarna
def hamtaInformationFranServer (year: int, field: str):
    params = {"nobelPrizeYear": year, "nobelPrizeCategory": field}
    res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=params).json()
    return res

# prisberäkning
#  variabler: pris: totala priset
#             pris_del: fördelning mellan vinnare
#
def beraknaVinstPengar(pris: float, pris_del: float) -> float:
    summaPerVinnare = pris / pris_del
    res = round(summaPerVinnare, 3)
    return res

# utskrift år och fält
def utskriftArochFalt(year: int, field: str):
    res = hamtaInformationFranServer(int(year), field)

    for p in res["nobelPrizes"]:
        print("----------------------------")
        peng = p["prizeAmount"]
        idagPeng = p["prizeAmountAdjusted"]
        print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")
        prize_cnt = 0

        for m in p["laureates"]:
            print("----------------------------")
            if "knownName" in m:
                print(m['knownName']['en'])
                print(m['motivation']['en'])
                andel = m['portion']
                prize_cnt += 1
        printResult(peng, idagPeng, prize_cnt)

def skrivUtAllInformationForAr(year: int):
    for item in cat:
        print("*" * 30)
        print(f"Field is {item}")
        res = hamtaInformationFranServer(int(year), item)

        for p in res["nobelPrizes"]:
            print("----------------------------")
            peng = p["prizeAmount"]
            idagPeng = p["prizeAmountAdjusted"]
            print(f"{p['categoryFullName']['se']} prissumma {peng} SEK")
            print(f"{p['categoryFullName']['se']} prissumma {idagPeng} SEK")
            prize_cnt = 0

            for m in p["laureates"]:
                print("----------------------------")
                if "knownName" in m:
                    print(m['knownName']['en'])
                print(m['motivation']['en'])
                andel = m['portion']
                prize_cnt += 1
            printResult(peng, idagPeng, prize_cnt)


def main():
    print(HELP_STRING)

    while True:

        menu_choice = input("\nVäl ett alternativ ovan? \n \n").upper().strip()

        if menu_choice == '1':
            field = ""
            year = ""
            aaa = input(">")
            str_list = aaa.split()
            flag = "All"
            if len(str_list) == 1:
                flag = "All"
                year = str_list[0]
            else:
                flag = "OneField"
                year, field = aaa.split()

            if flag == "OneField" and not checkFalt(field):
                print("Skriv rätt fält.\n För att se alla fält tryck 2")
            else:
                if flag == "OneField":
                    utskriftArochFalt(int(year), field)
                else:
                    skrivUtAllInformationForAr(int(year))

        if menu_choice == '2':
            print("Alla fält:")
            for item in cat:
                print(item)
            continue
        if menu_choice.upper() == 'H':
            print(HELP_STRING)
            continue
        if menu_choice.upper() == 'Q':
            print("Good-bye and thank you for the fish!")
            return


if __name__ == '__main__':
    main()