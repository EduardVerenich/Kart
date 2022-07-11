import random

bank1 = ['5ч', '6ч', "7ч", '8ч', "9ч", "Вч", 'Дч', "Кч", 'Тч',
         '5б', "6б", '7б', "8б", '9б', 'Вб', "Дб", 'Кб', "Тб",
         '5к', '6к', "7к", '8к', "9к", "Вк", 'Дк', "Кк", 'Тк',
         '5п', "6п", '7п', "8п", '9п', "Вп", 'Дп', "Кп", 'Тп']
bank = []
user = []
komputer = []


def razdach0():
    r = 35
    while 0 <= r:
        x = random.randint(0, r)
        bank.append(bank1[x])
        del bank1[x]
        r -= 1
    return bank


def rez_igrokam():

    i = 1
    while i <= 6:
        import main
        bank=main.bank

        if bank[0] != []:
            komputer.append(bank[0])
            del bank[0]
        if bank[0] != []:
            user.append(bank[0])
            del bank[0]
        i += 1
    return komputer, user


def razdach_user():

    b = 0
    for i in user:
        b += 1
    c = 6
    c -= b
    while c > 0:
        if bank != []:
            user.append(bank[0])
            print('aw=0 дали useru: ', bank[0])
            del bank[0]
        c -= 1
        return user


def razdach_comp():
    b = 0
    for i in komputer:
        b += 1
    c = 6
    c -= b
    while c > 0:
        if bank != []:
            komputer.append(bank[0])
            print('aw=0 дали comp: ', bank[0])
            del bank[0]
        c -= 1
        return komputer
# razdach0()
# rez_igrokam()
#
print(bank)
print(user,komputer)