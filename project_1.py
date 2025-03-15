'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lenka Křístková
email: lennie.ho93@gmail.com
'''


# Zadané texty
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]


oddelovac = '-' * 41

# Uživatelská jména a hesla ze zadání
uzivatele = {'bob': '123', 'ann': 'pass123', 
             'mike': 'password123', 'liz': 'pass123'}


# Vyzvání uživatele k přihlášení
uzivatel = input('Zadej své uživatelské jméno: ')
heslo = input('Zadej heslo: ')


# Výpis uživatele a uvítání
if uzivatel in uzivatele.keys() and heslo in uzivatele.values():
    print('username:', uzivatel)
    print('password', heslo)
    print(oddelovac)
    print('Welcome to the app, ', uzivatel)
    print('We have 3 texts to be analysed.')
    print(oddelovac)

    # získání čísla textu od uživatele
    cislo_textu = int(input('Enter a number btw. 1 and 3 do select:'))
    if cislo_textu < 0 and cislo_textu > 3:
        print('Wrong number, terminating program')
    print(oddelovac)
        
    # první tabulka o údajích z textu
    print('There are', len(TEXTS[cislo_textu - 1].split()), 
          'words in the selected text')

    titlecase = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if slovo.istitle():
            titlecase.append(slovo)
        
    print('There are', len(titlecase), 'titlecase words.')


    uppercase = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if slovo.isupper():
            uppercase.append(slovo)

    print('There are', len(uppercase), 'uppercase words.')


    lowercase = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if slovo.islower():
            lowercase.append(slovo)
        
    print('There are', len(lowercase), 'lowercase words.')


    numeric_strings = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if slovo.isnumeric():
            numeric_strings.append(slovo)

    print('There are', len(numeric_strings), 'numeric strings.')


    soucet = sum(int(cislo) for cislo in numeric_strings)
    print('The sum of all the numbers', soucet)


    print(oddelovac)

    print('LEN| OCCURENCES  |NR.')

    print(oddelovac)
    
    
    # druhá tabulka o údajích z textu
    jedno_pismeno = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if len(slovo) == 1:
            jedno_pismeno.append(slovo)

    print('1|'.center(5), len(jedno_pismeno) * '*', '|', len(jedno_pismeno))


    dve_pismena = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if len(slovo) == 2:
            dve_pismena.append(slovo)

    print('2|'.center(5), len(dve_pismena) * '*', '|',  len(dve_pismena))


    tri_pismena = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if len(slovo) == 3:
            tri_pismena.append(slovo)

    print('3|'.center(5), len(tri_pismena) * '*', '|', len(tri_pismena))


    ctyri_pismena = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if len(slovo) == 4:
            ctyri_pismena.append(slovo)

    print('4|'.center(5), len(ctyri_pismena) * '*', '|', len(ctyri_pismena))


    pet_pismen = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if len(slovo) == 5:
            pet_pismen.append(slovo)

    print('5|'.center(5), len(pet_pismen) * '*', '|', len(pet_pismen))


    sest_pismen = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if len(slovo) == 6:
            sest_pismen.append(slovo)

    print('6|'.center(5), len(sest_pismen) * '*', '|', len(sest_pismen))


    sedm_pismen = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if len(slovo) == 7:
            sedm_pismen.append(slovo)

    print('7|'.center(5), len(sedm_pismen) * '*', '|', len(sedm_pismen))


    osm_pismen = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if len(slovo) == 8:
            osm_pismen.append(slovo)

    print('8|'.center(5), len(osm_pismen) * '*', '|', len(osm_pismen))


    devet_pismen = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if len(slovo) == 9:
            devet_pismen.append(slovo)

    print('9|'.center(5), len(devet_pismen) * '*', '|', len(devet_pismen))


    deset_pismen = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if len(slovo) == 10:
            deset_pismen.append(slovo)

    print('10|'.center(5), len(deset_pismen) * '*', '|', len(deset_pismen))


    jedenact_pismen = []
    for slovo in TEXTS[cislo_textu - 1].split():
        if len(slovo) == 11:
            jedenact_pismen.append(slovo)

    print('11|'.center(5), len(jedenact_pismen) * '*', '|', 
          len(jedenact_pismen))



# kód pro špatné zadání jména a hesla
else:
    print(f'''username: {uzivatel}
password: {heslo}
unregistered user, terminating program..''')
    

