import raz


bank = raz.bank

user = raz.user
komputer= raz.komputer

kozir_komp = []                                                 # Козыри на руках у КОМПЮТЕРА
kozir_user = []                                                 # Козыри на руках у USER
s = str(bank[-1])

def kozir_na_rukah():

    a = 0
    while a < 6:
        d = str(user[a])
        f = str(komputer[a])

        if s[1]==d[1]:
            kozir_user.append(user[a])
            kozir_user.sort()

        if s[1]==f[1]:
            kozir_komp.append(komputer[a])
            kozir_komp.sort()
        a += 1
    print(kozir_user,kozir_komp)
    return kozir_user,kozir_komp



def komy_xod0():

    aw = 0
    if kozir_user == [] and kozir_komp != []:
        aw += 1
        print('\nХОДИТ Komputer, НАЙБОЛЬШАЯ КАРТА:', kozir_komp[-1])


    elif kozir_user != [] and kozir_komp == []:
        print('\nХОДИТ USER, НАЙБОЛЬШАЯ КАРТА:', kozir_user[-1])

    elif kozir_user == [] and kozir_komp == []:
        af = str(user[-1])
        ak = str(komputer[-1])

        if af[0] > ak[0]:
            print('\nХОДИТ USER, НАЙБОЛЬШАЯ КАРТА:', user[-1])
        else:
            aw += 1
            print('\nХОДИТ Komputer, НАЙБОЛЬШАЯ КАРТА:', komputer[-1])


    elif kozir_user[-1] > kozir_komp[-1]:
        print('\nХОД USERA, БОЛЬШИЙ КОЗЫРЬ:', kozir_user[-1])
    else:
        aw += 1
        print('\nХОД Komputerа, КОЗЫРЬ:', kozir_komp[-1])

kozir_na_rukah()
# kozir_na_rukah()
komy_xod0()