def citire_lista(lista_de_numere):
    string_citire = input("dati lista de numere separate prin virgula: ")
    valori = string_citire.split(",")
    for x in valori:
        lista_de_numere.append(int(x))
    return lista_de_numere


def prim(numar):
    """
    Verifica daca un numar intreg este prim
    :param numar: o valoare intreaga "numar"
    :return: True, daca "numar" este prim, respectiv False in caz contrar
    """
    if numar < 2:
        return False
    for i in range(2, numar // 2 + 1):
        if numar % i == 0:
            return False
    return True


def verificare_elemente_neprime(lista):
    """
    Verifica daca un sir de numere contine doar numere neprime
    :param lista: o lista de numere intregi
    :return: True, daca sirul are aceasta proprietate, respectiv False in caz contrar
    """
    for i in range(len(lista)):
        verificare = prim(lista[i])
        if verificare is True:
            return False
    return True


def get_longest_all_not_prime(lista):
    """
    Determina cea mai lunga subsecventa de elemente neprime dintr-o lista
    :param lista: o lista de numere intregi
    :return: o noua lista, ce reprezinta cea mai lunga subsecventa cu aceasta proprietate
    """
    rezultat = []
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            verificare = verificare_elemente_neprime(lista[i:j + 1])
            if verificare is True and len(rezultat) < len(lista[i:j + 1]):
                rezultat = lista[i:j + 1]
    return rezultat


def medie(lista):
    """
    Calculeaza media aritmetica a unui sir de numere
    :param lista: o lista de valori intregi
    :return: o valoare intreaga
    """
    suma = 0
    numar_elemente = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
        numar_elemente = numar_elemente + 1
    medie_aritmetica = suma / numar_elemente
    return medie_aritmetica


def verificare_medie_aritmetica(lista, numar):
    """
    Verifica daca media aritmetica a umui sir depaseste un intreg
    param lista: o lista de numere intregi
    param numar: o valoare inteaga
    :return: True, daca proprietatea este adevarata, respectiv False in caz contrar
    """
    medie_aritmetica = medie(lista)
    if medie_aritmetica < numar:
        return True
    return False


def get_longest_average_below(lista, numar):
    """
    Determina cea mai lunga subsecventa a umui sir cu proprietatea ca media sa nu depaseste valoarea unui intreg
    :param lista: o lista de numere intregi
    :param numar: o valoare intreaga
    :return: o noua lista, ce reprezinta secventa de lungime maxima cu aceasta proprietate
    """
    rezultat = []
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            verificare = verificare_medie_aritmetica(lista[i:j + 1], numar)
            if verificare is True and len(rezultat) < len(lista[i:j + 1]):
                rezultat = lista[i:j + 1]
    return rezultat


def test_prim():
    assert prim(25) is False
    assert prim(19) is True
    assert prim(10) is False


def test_verificare_elemente_neprime():
    assert verificare_elemente_neprime([1, 2, 3]) is False
    assert verificare_elemente_neprime([4, 6, 8]) is True
    assert verificare_elemente_neprime([2, 4, 6, 8]) is False


def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([4, 6, 8, 2, 5]) == [4, 6, 8]
    assert get_longest_all_not_prime([2, 3, 5, 7]) == []
    assert get_longest_all_not_prime([4, 6, 8, 10]) == [4, 6, 8, 10]


def test_medie():
    assert medie([1, 2, 3]) == 2
    assert medie([2, 4]) == 3
    assert medie([1, 2]) == 1.5


def test_verificare_medie_aritmetica():
    assert verificare_medie_aritmetica([1, 4, 5], 10) is True
    assert verificare_medie_aritmetica([1, 2, 3], 10) is True
    assert verificare_medie_aritmetica([17, 19, 10], 10) is False


def test_get_longest_average_below():
    assert get_longest_average_below([1, 2, 3, 4, 5], 10) == [1, 2, 3, 4, 5]
    assert get_longest_average_below([10, 19, 17], 30) == [10, 19, 17]
    assert get_longest_average_below([20, 30, 50], 100) == [20, 30, 50]


def meniu():
    print("1. Citire date")
    print("2. Toate numerele sunt neprime.")
    print("3. Media numerelor nu depășește o valoare citită.")
    print("4. Iesire")
    merge = True
    lista_de_numere = []
    while merge is True:
        optiune = int(input("Dati o valoare de la 1 la 4: "))
        if optiune == 1:
            lista_de_numere = []
            citire_lista(lista_de_numere)
        elif optiune == 2:
            rezultat = get_longest_all_not_prime(lista_de_numere)
            print(rezultat)
        elif optiune == 3:
            k = int(input("Dati numarul: "))
            rezultat = get_longest_average_below(lista_de_numere, k)
            print(rezultat)
        elif optiune == 4:
            merge = False
        else:
            print("Valoare gresita! Incercati din nou!")


def main():
    test_prim()
    test_verificare_elemente_neprime()
    test_get_longest_all_not_prime()
    test_medie()
    test_verificare_medie_aritmetica()
    test_get_longest_average_below()
    meniu()


if __name__ == '__main__':
    main()
