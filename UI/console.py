from Domain.expense import getnewexpense, get_expense_into_string
from Logic.add_value_if_date import add_value_if_date
from Logic.biggest_sum_by_type import biggest_sum_by_type
from Logic.crud import create, update, delete, read
from Logic.delete_all_expenses_apartment import delete_all_expenses_apartment
from Logic.descending_order_by_sum import descending_order_by_sum


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
    print('8. Ordonarea cheltuielilor descrescător după sumă.')
    print('a. Afisarea listei de cheltuieli.')
    print('z. Undo !')
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


def handle_descending_order_by_sum(cheltuieli):
    try:
        cheltuieli = descending_order_by_sum(cheltuieli)
        print('Cheltuielile au fost ordonate descrescator dupa suma')
    except ValueError as ve:
        print('Eroare', ve)

    return cheltuieli


def handle_list_versions(list_versions, current_version, cheltuieli):
    list_versions.append(cheltuieli)
    current_version += 1
    return list_versions, current_version


def handle_undo(list_versions, current_version):
    if current_version < 1:
        print('Nu mai puteti face undo!')
        return list_versions[current_version], current_version
    current_version = current_version - 1
    return list_versions[current_version], current_version


def main():
    cheltuieli = []
    list_versions = [cheltuieli]
    current_version = 0
    while True:
        show_menu()
        optiune = input("Alege optiunea: ")
        if optiune == '1':
            cheltuieli = handle_crate(cheltuieli)
            list_versions, current_version = handle_list_versions(list_versions, current_version, cheltuieli)
        elif optiune == '2':
            cheltuieli = handle_read(cheltuieli)
        elif optiune == '3':
            cheltuieli = handle_update(cheltuieli)
            list_versions, current_version = handle_list_versions(list_versions, current_version, cheltuieli)
        elif optiune == '4':
            cheltuieli = handle_delete(cheltuieli)
            list_versions, current_version = handle_list_versions(list_versions, current_version, cheltuieli)
        elif optiune == '5':
            cheltuieli = handle_delete_all_expenses_apartment(cheltuieli)
            list_versions, current_version = handle_list_versions(list_versions, current_version, cheltuieli)
        elif optiune == '6':
            cheltuieli = handle_add_value_if_date(cheltuieli)
            list_versions, current_version = handle_list_versions(list_versions, current_version, cheltuieli)
        elif optiune == '7':
            cheltuieli = handle_biggest_sum_by_type(cheltuieli)
        elif optiune == '8':
            cheltuieli = handle_descending_order_by_sum(cheltuieli)
            list_versions, current_version = handle_list_versions(list_versions, current_version, cheltuieli)
        elif optiune == 'a':
            handle_show_list(cheltuieli)
        elif optiune == 'z':
            cheltuieli, current_version = handle_undo(list_versions, current_version)
        elif optiune == 'x':
            break
        else:
            print('Optiune Invalida!')
