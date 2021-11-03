from Domain.expense import getnewexpense, get_nr_apartment
from Logic.delete_all_expenses_apartment import delete_all_expenses_apartment


def get_data():

    """
    Functie suport pentru functiile de test
    """

    return \
        [
            getnewexpense(20, 1, 123, '17.08.2018', 'canal'),
            getnewexpense(30, 2, 200, '07.03.2020', 'intretinere'),
            getnewexpense(19, 3, 390, '15.05.2019', 'alte cheltuieli'),
            getnewexpense(8, 2, 332, '05.07.2016', 'canal'),
            getnewexpense(23, 2, 1000, '12.12.2020', 'canal')

        ]


def test_delete_all_expenses_apartment():
    list = get_data()
    contor = 0
    new_list = delete_all_expenses_apartment(list, 2)
    assert len(new_list) == len(list) - 3
    for expense in new_list:
        if get_nr_apartment(expense) == 2:
            contor = contor + 1
    assert contor == 0
