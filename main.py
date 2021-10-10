from math import pow


def citire_lista(lista_de_numere):
    string_citire = input("dati lista de numere separate prin virgula: ")
    valori = string_citire.split(",")
    for x in valori:
        lista_de_numere.append(int(x))
    return lista_de_numere


def invers(numar):
    """
    Calculeaza inversul unui numar intreg
    :param numar: o valoare intreaga "numar"
    :return: o valoare intreaga, ce reprezinta inversul lui "numar"
    """
    oglindit = 0
    while numar != 0:
        oglindit = (oglindit * 10) + (numar % 10)
        numar = numar // 10
    return oglindit


def palindrom(numar):
    """
    Verifica daca un numar este palindrom
    :param numar: o valoare intreaga "numar"
    :return: True, daca "numar" este palindrom, resprectiv False in caz contrar
    """
    oglindit = invers(numar)
    if oglindit == numar:
        return True
    return False


def verificare_elemente_palindromice(lista):
    """
    Verifica daca un sir de numere contine elemente palindromice
    :param lista: o lista de numere intregi
    :return: True, daca sirul are aceasta proprieatare, respectiv False in caz contrar
    """
    for i in range(len(lista)):
        verificare = palindrom(lista[i])
        if verificare is False:
            return False
    return True


def get_longest_all_palindromes(lista):
    """
    Determina cea mai lunga subsecventa de elemente palindromice dintr-o lista
    :param lista: o lista de numere intregi
    :return: o noua lista, ce reprezinta cea mai lunga subsecventa cu aceasta proprietate
    """
    rezultat = []
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            verificare = verificare_elemente_palindromice(lista[i:j + 1])
            if verificare is True and len(rezultat) < len(lista[i:j + 1]):
                rezultat = lista[i:j + 1]
    return rezultat


def calcul_putere(numar, k):
    """
    Calculeaza radicalul de ordin k a unui numar intreg
    :param numar: o valoare intreaga
    :param k: o valoare intreaga
    :return: True, daca numarul are aceasta proprietate, respectiv False in caz contrar
    """
    putere = float(1/k)
    rezultat = pow(numar, putere)
    if rezultat == int(rezultat):
        return True
    return False


def verificare_calcul_putere(lista, k):
    """
    Verifica daca intr-un sir de numere toate acetea pot fi scrise ca un numar ridicat la puterea k
    :param lista: o lista de numere intregi
    :param k: o valoare intreaga
    :return: True, daca sirul are aceasta proprietate, respectiv False in caz contrar
    """
    for i in range(len(lista)):
        verificare = calcul_putere(lista[i], k)
        if verificare is False:
            return False
    return True


def get_longest_powers_of_k(lista, k):
    """
    Determina cea mai lunga subsecventa de elemente cu partea imtreaga si fractionara egale dintr-o lista
    :param lista: o lista de numere reale
    :param k: o valoare intreaga
    :return: o noua lista, ce reprezinta cea mai lunga subsecventa cu aceasta proprietate
    """
    rezultat = []
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            verificare = verificare_calcul_putere(lista[i:j + 1], k)
            if verificare is True and len(rezultat) < len(lista[i:j + 1]):
                rezultat = lista[i:j + 1]
    return rezultat


def test_imvers():
    assert invers(25) == 52
    assert invers(19) == 91
    assert invers(10) == 1


def test_palindrom():
    assert palindrom(25) is False
    assert palindrom(9) is True
    assert palindrom(11) is True


def test_verificare_elemente_palindromice():
    assert verificare_elemente_palindromice([25, 15, 36]) is False
    assert verificare_elemente_palindromice([4, 9, 5]) is True
    assert verificare_elemente_palindromice([101, 171, 192]) is False


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert get_longest_all_palindromes([10, 11, 121, 13]) == [11, 121]
    assert get_longest_all_palindromes([51, 40, 32]) == []


def test_calcul_putere():
    assert calcul_putere(8, 2) is False
    assert calcul_putere(9, 2) is True
    assert calcul_putere(16, 4) is True


def test_verificare_calcul_putere():
    assert verificare_calcul_putere([2, 4, 6, 8], 3) is False
    assert verificare_calcul_putere([4, 9, 25, 36], 2) is True
    assert verificare_calcul_putere([2], 2) is False


def test_get_longest_powers_of_k():
    assert get_longest_powers_of_k([4, 25, 9, 10, 11], 2) == [4, 25, 9]
    assert get_longest_powers_of_k([2, 3, 4, 5], 2) == [4]
    assert get_longest_powers_of_k([2, 3, 5], 3) == []


def meniu():
    print("1. citire date")
    print("2. toate numerele sunt palindroame.")
    print("3. toate numerele se pot scrie ca x ** k, k citit, x întreg pozitiv.")
    print("4. iesire")
    merge = True
    lista_de_numere = []
    while merge is True:
        optiune = int(input("dati o valoare de la 1 la 4: "))
        if optiune == 1:
            lista_de_numere = []
            citire_lista(lista_de_numere)
        elif optiune == 2:
            rezultat = get_longest_all_palindromes(lista_de_numere)
            print(rezultat)
        elif optiune == 3:
            k = int(input("dati valoarea lui k: "))
            rezultat = get_longest_powers_of_k(lista_de_numere, k)
            print(rezultat)
        elif optiune == 4:
            merge = False
        else:
            print("Valoare gresita! Incercati din nou!")


def main():
    test_imvers()
    test_palindrom()
    test_verificare_elemente_palindromice()
    test_get_longest_all_palindromes()
    test_calcul_putere()
    test_verificare_calcul_putere()
    test_get_longest_powers_of_k()
    meniu()


if __name__ == '__main__':
    main()