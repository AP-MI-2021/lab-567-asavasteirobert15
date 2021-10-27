from Domain.expense2 import getnewexpense
from Logic.crud import create, update, delete, read
from Tests.tests_for_crud import test_crud


def show_menu():

    """
    Functie de afisare a meniului
    """

    print('1. Creare cheltuiala noua')
    print('2. Vizualizarea unei anumite cheltuieli de la un numar de apartament dat')
    print('3. Modificarea unei cheltuieli')
    print('4. Stergerea unei cheltuieli')
    print('5. Afisarea listei de cheltuieli')
    print('x. Exit !')


def main():
    list = []
    while True:
        show_menu()
        optiune = input("Alege optiunea: ")
        if optiune == '1':
            _nr_apartment = int(input('Introduceti numarul apartamentului: '))
            _sum = int(input('Introduceti suma aferenta cheltuielii: '))
            _data = input('Introduceti data cheltuielii ( in format DD.MM.YYYY ):')
            _type = input('Introduceti tipul cheltuielii (intretinere, canal sau alte cheltuieli): ')
            list = create(list, _nr_apartment, _sum, _data, _type)
            print('Cheltuiala a fost creata !')
        elif optiune == '2':
            _nr_apartment = int(input('Introduceti numarul apartamentului a carui cheltuiala doriti sa o vizionati: '))
            read_expense = read(list, _nr_apartment)
            print(f'Cheltuiala de la apartamentul cu nr {_nr_apartment} este {read_expense}')
        elif optiune == '3':
            _nr_apartment_update = int(input('Introduceti numarul apartamentului a carui cheltuiala doriti sa '
                                             'o modificati: '))
            _sum = int(input('Modificati suma daca este nevoie, daca nu introducesi suma curenta: '))
            _data = input('Modificati data daca este nevoie, daca nu introduceti data curenta: ')
            _type = input('Modificati tipul cheltuielii daca este necesar, altfel introduceti tipul curent: ')
            updated_expense = getnewexpense(_nr_apartment_update, _sum, _data, _type)
            list = update(list, updated_expense)
            print(f'Cheltuiala de la apartamentul {_nr_apartment_update} a fost modificata! ')
        elif optiune == '4':
            _nr_apartament_deleted = int(input('Introduceti numarul apartamentului a carui cheltuiala doriti sa '
                                               'o stergeti : '))
            list = delete(list, _nr_apartament_deleted)
            print(f'Cheltuiala de la apartamentul {_nr_apartament_deleted} a fost streasa')
        elif optiune == '5':
            print('Lista de cheltuieli este: ')
            print(list)
        elif optiune == 'x':
            break


test_crud()


main()