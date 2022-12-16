import requests

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur api:et fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa api:et fins här: https://app.swaggerhub.com/apis/NobelMedia/
# NobelMasterData/2.1


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


def check_falt(field: str):
    if field not in cat:
        return False
    else:
        return True


def print_result(peng: float, idagPeng: float, prize_cnt: int):
    print("*" * 30)
    pengarVarde_Ar = berakna_vinst_pengar(peng, prize_cnt)
    result1 = f'{pengarVarde_Ar:.3f}'
    print(f"Prissummans värde då: {result1}")

    pengarVarde_idag = berakna_vinst_pengar(idagPeng, prize_cnt)
    result2 = f'{pengarVarde_idag:.3f}'
    print(f"Prissummans värde idag: {result2}")


# hämta vinnarna
def hamta_information_fran_server(year: int, field: str):
    params = {"nobelPrizeYear": year, "nobelPrizeCategory": cat[field]}
    res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=params).json()
    return res

# prisberäkning
#  variabler: pris: totala priset
#             pris_del: fördelning mellan vinnare


def berakna_vinst_pengar(pris: float, pris_del: float) -> float:
    if pris_del == 0:
        return 0.000
    summaPerVinnare = pris / pris_del
    res = round(summaPerVinnare, 3)
    return res

# utskrift år och fält


def utskrift_ar_och_falt(year: int, field: str):
    res = hamta_information_fran_server(int(year), field)

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

            prize_cnt += 1
        print_result(peng, idagPeng, prize_cnt)


def skriv_ut_all_information_for_ar(year: int):
    for item in cat:
        print("*" * 30)
        print(f"Field is {item}")
        res = hamta_information_fran_server(int(year), item)

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

                prize_cnt += 1
            print_result(peng, idagPeng, prize_cnt)


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

            if flag == "OneField" and not check_falt(field):
                print("Skriv rätt fält.\n För att se alla fält tryck 2")
            else:
                if flag == "OneField":
                    utskrift_ar_och_falt(int(year), field)
                else:
                    skriv_ut_all_information_for_ar(int(year))

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
