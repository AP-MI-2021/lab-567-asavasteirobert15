from Domain.expense import getnewexpense, get_expense_into_string
from Logic.add_value_if_date import add_value_if_date
from Logic.biggest_sum_by_type import biggest_sum_by_type
from Logic.crud import create, update, delete, read
from Logic.delete_all_expenses_apartment import delete_all_expenses_apartment


def show_menu():
    """
    Functie de afisare a meniului
    """

    print('1. Creare cheltuiala noua.')
    print('2. Vizualizarea unei anumite cheltuieli de la un numar de apartament dat.')
    print('3. Modificarea unei cheltuieli.')
    print('4. Stergerea unei cheltuieli.')
    print('5. Ștergerea tuturor cheltuielilor pentru un apartament dat.')
    print('6. Adunarea unei valori la toate cheltuielile dintr-o dată citită.')
    print('7. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.')
    print('a. Afisarea listei de cheltuieli.')
    print('x. Exit !')


def handle_crate(cheltuieli):
    try:
        _id = int(input('Introdueti id-ul cheltuielii: '))
        _nr_apartment = int(input('Introduceti numarul apartamentului: '))
        _sum = int(input('Introduceti suma aferenta cheltuielii: '))
        _data = input('Introduceti data cheltuielii ( in format DD.MM.YYYY ):')
        _type = input('Introduceti tipul cheltuielii (intretinere, canal sau alte cheltuieli): ')
        cheltuieli = create(cheltuieli, _id, _nr_apartment, _sum, _data, _type)
        print('Cheltuiala a fost creata !')
    except ValueError as ve:
        print('Eroare: ', ve)

    return cheltuieli


def handle_read(cheltuieli):
    try:
        _id = int(input('Introduceti id-ul cheltuielii pe care dorit sa o vizionati: '))
        read_expense = read(cheltuieli, _id)
        print(get_expense_into_string(read_expense))
    except ValueError as ve:
        print('Eroare: ', ve)

    return cheltuieli


def handle_update(cheltuieli):
    try:
        _id = int(input('Introduceti id-ul cheltuielii pe care doriti sa o modificati'))
        _nr_apartment = int(input('Modificati numarul apartamentului daca este nevoie, daca nu introduceti'
                                  ' numarul de apartament curent: '))
        _sum = int(input('Modificati suma daca este nevoie, daca nu introducesi suma curenta: '))
        _data = input('Modificati data daca este nevoie, daca nu introduceti data curenta: ')
        _type = input('Modificati tipul cheltuielii daca este necesar, altfel introduceti tipul curent: ')
        updated_expense = getnewexpense(_id, _nr_apartment, _sum, _data, _type)
        cheltuieli = update(cheltuieli, updated_expense)
        print(f'Cheltuiala cu id-ul {_id} a fost modificata! ')
    except ValueError as ve:
        print('Eroare: ', ve)

    return cheltuieli


def handle_show_list(cheltuieli):
    try:
        print('Lista de cheltuieli este: ')
        print(cheltuieli)
    except ValueError as ve:
        print('Eroare: ', ve)


def handle_delete(cheltuieli):
    try:
        _id_deleted = int(input('introduceti id-ul cheltuielii pe care doriti sa o stergeti: '))
        cheltuieli = delete(cheltuieli, _id_deleted)
        print(f'Cheltuiala cu id-ul {_id_deleted} a fost streasa')
    except ValueError as ve:
        print('Eroare: ', ve)

    return cheltuieli


def handle_delete_all_expenses_apartment(cheltuieli):
    try:
        _nr_apartment_to_delete = int(input('Introduceti numarul apartamentului a carui cheltuieli doriti a fi '
                                            'sterse: '))
        cheltuieli = delete_all_expenses_apartment(cheltuieli, _nr_apartment_to_delete)
        print(f'Cheltuielile apartamentului cu nr {_nr_apartment_to_delete} au fost sterse cu succes !')
    except ValueError as ve:
        print('Eroare', ve)

    return cheltuieli


def handle_add_value_if_date(cheltuieli):
    try:
        _data = input("Introduceti data cheltuielilor carora doriti sa le adaugati o anumita valoare: ")
        _value = float(input('Introduceti valoare pe care doriti sa o adaugati: '))
        cheltuieli = add_value_if_date(cheltuieli, _data, _value)
        print(f'Sumele cheltuielilor de la data {_data} au fost marite cu valoarea de {_value} cu succes')
    except ValueError as ve:
        print('Eroare', ve)

    return cheltuieli



def handle_biggest_sum_by_type(cheltuieli):
    try:
        sum_max_intretinere = biggest_sum_by_type(cheltuieli, 'intretinere')
        print(f'Cea mai mare valoare a cheltuielilor de tip intretinere este {sum_max_intretinere}')
        sum_max_canal = biggest_sum_by_type(cheltuieli, 'canal')
        print(f'Cea mai mare valoare a cheltuielilor de tip canal este {sum_max_canal}')
        sum_max_alte_cheltuieli = biggest_sum_by_type(cheltuieli, 'alte cheltuieli')
        print(f'Cea mai mare valoare a cheltuielilor de tip alte cheltuieli este {sum_max_alte_cheltuieli}')
    except ValueError as ve:
        print('Eroare', ve)

    return cheltuieli


def main():
    list = []
    while True:
        show_menu()
        optiune = input("Alege optiunea: ")
        if optiune == '1':
            list = handle_crate(list)
        elif optiune == '2':
            list = handle_read(list)
        elif optiune == '3':
            list = handle_update(list)
        elif optiune == '4':
            list = handle_delete(list)
        elif optiune == '5':
            list = handle_delete_all_expenses_apartment(list)
        elif optiune == '6':
            list = handle_add_value_if_date(list)
        elif optiune == '7':
            list = handle_biggest_sum_by_type(list)
        elif optiune == 'a':
            handle_show_list(list)
        elif optiune == 'x':
            break
        else:
            print('Optiune Invalida!')

