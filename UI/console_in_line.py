from Domain.expense import get_expense_into_string, getnewexpense
from Logic.add_value_if_date import add_value_if_date
from Logic.biggest_sum_by_type import biggest_sum_by_type
from Logic.crud import create, read, update, delete
from Logic.delete_all_expenses_apartment import delete_all_expenses_apartment


def show_help():
    print('HELP : ')
    print('add,id,nr_ap,sum,data,type -> adauga cheltuiala noua')
    print('read,id -> vizualizarea unei anumite cheltieli dupa id')
    print('showall -> afisarea tuturor cheltuielilor')
    print('update,id,nr_ap,suma,data,type -> modificarea unei cheltuieli cu un id existent')
    print('delete,id -> stergerea unei cheltuieli dupa un id existent')
    print('add_val,by_data,value -> adunarea unei valori la toate cheltuielile dintr-o anumita data')
    print('del_by_nr_ap,nr_ap -> stergerea tuturor cheltuielilor ale unui apartament')
    print('biggest_cost -> gaseste cea mai mare valoare a cheltuielilor in functie de tipul cheltuielii')
    print('exit -> iesire din UI, neaparat la final, nu se pune ; dupa')


def handle_add(cheltuieli, id, nr_ap, sum, data, type):
    try:
        return create(cheltuieli, id, nr_ap, sum, data, type)
    except ValueError as ve:
        print('Eroare: ', ve)

    return cheltuieli


def handle_read(cheltuieli, id):
    try:
        read_expense = read(cheltuieli, id)
        print(f'Cheltuiala cu id {id} este:')
        print(get_expense_into_string(read_expense))
    except ValueError as ve:
        print('Eroare: ', ve)

    return cheltuieli


def handle_showall(cheltuieli):
    try:
        print('Lista de cheltuieli este: ')
        print(cheltuieli)
    except ValueError as ve:
        print('Eroare: ', ve)


def handle_update(cheltuieli, id, nr_ap, sum, data, type):
    try:
        update_expense = getnewexpense(id, nr_ap, sum, data, type)
        cheltuieli = update(cheltuieli, update_expense)
        print(f'Cheltuiala cu id-ul {id} a fost modificata! ')
    except ValueError as ve:
        print('Eroare: ', ve)

    return cheltuieli


def handle_delete(cheltuieli, id):
    try:
        result = read(cheltuieli, id)
        if result is None:
            raise ValueError('Nu exista cheltuiala cu id-ul introdus!')
        cheltuieli = delete(cheltuieli, id)
        print(f'Cheltuiala cu id-ul {id} a fost streasa')
    except ValueError as ve:
        print('Eroare: ', ve)

    return cheltuieli


def handle_add_val(cheltuieli, data, value):
    try:
        cheltuieli = add_value_if_date(cheltuieli, data, value)
        print(f'Sumele cheltuielilor de la data {data} au fost marite cu valoarea de {value} cu succes')
    except ValueError as ve:
        print('Eroare', ve)

    return cheltuieli


def handle_delete_by_nr_ap(cheltuieli, nr_ap):
    try:
        cheltuieli = delete_all_expenses_apartment(cheltuieli, nr_ap)
        print(f'Cheltuielile apartamentului cu nr {nr_ap} au fost sterse cu succes !')
    except ValueError as ve:
        print('Eroare', ve)

    return cheltuieli


def handle_biggest_cost(cheltuieli):
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


def main2():
    lista_cheltuieli = []
    print(' ')
    show_help()
    print(' ')
    comenzi = input('Scrie numele comenzi si parametrii necesari conform ghidului afisat,'
                    'acestea fiind separate prin |,|, dupa care separati comenzile prin |;|:')
    lista_comenzi = comenzi.split(';')
    done = False
    while not done:
        for comanda in lista_comenzi:
            comanda_sep = comanda.split(',')

            if comanda_sep[0] == 'add':
                lista_cheltuieli = handle_add(lista_cheltuieli, int(comanda_sep[1]), int(comanda_sep[2]),
                                              float(comanda_sep[3]), str(comanda_sep[4]), str(comanda_sep[5]))
            elif comanda_sep[0] == 'read':
                lista_cheltuieli = handle_read(lista_cheltuieli, comanda_sep[1])
            elif comanda_sep[0] == 'showall':
                handle_showall(lista_cheltuieli)
            elif comanda_sep[0] == 'update':
                lista_cheltuieli = handle_update(lista_cheltuieli, int(comanda_sep[1]), int(comanda_sep[2]),
                                              float(comanda_sep[3]), str(comanda_sep[4]), str(comanda_sep[5]))
            elif comanda_sep[0] == 'add_val':
                lista_cheltuieli = handle_add_val(lista_cheltuieli, str(comanda_sep[1]), float(comanda_sep[2]))
            elif comanda_sep[0] == 'del_by_nr_ap':
                lista_cheltuieli = handle_delete_by_nr_ap(lista_cheltuieli, int(comanda_sep[1]))
            elif comanda_sep[0] == 'biggest_cost':
                lista_cheltuieli = handle_biggest_cost(lista_cheltuieli)
            elif comanda_sep[0] == 'exit':
                done = True
            else:
                print('Optiune invalida, incercati din nou va rog ! ')
