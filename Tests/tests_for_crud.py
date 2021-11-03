from Domain.expense import getnewexpense, get_id
from Logic.crud import create, read, update, delete


def get_data():

    """
    Functie suport pentru functiile de test
    """

    return \
        [
            getnewexpense(20, 1, 123, '17.08.2018', 'canal'),
            getnewexpense(30, 2, 200, '07.03.2020', 'intretinere'),
            getnewexpense(19, 3, 390, '15.05.2019', 'alte cheltuieli'),
            getnewexpense(8, 6, 332, '05.07.2016', 'canal'),
            getnewexpense(23, 9, 1000, '12.12.2020', 'canal')

        ]


def test_create():

    """
    Functia de test a functii 'create' din crud.py
    """

    list = get_data()
    new_expense = getnewexpense(1, 7, 1000, '12.12.2020', 'canal')
    new_list = create(list, 1, 7, 1000, '12.12.2020', 'canal')
    assert len(list) + 1 == len(new_list)
    assert new_expense in new_list


def test_read():

    """
    Functia de test a funtii 'read' din crud.py
    """

    list = get_data()
    random_expense = list[2]
    assert read(list, get_id(random_expense)) == random_expense
    assert read(list, None) == list


def test_update():

    """
    Functia de test a functii 'update' din crud.py
    """

    list = get_data()
    random_expense = getnewexpense(23, 3, 100, '15.05.2019', 'canal')
    new_list = update(list, random_expense)
    assert len(list) == len(new_list)
    assert random_expense in new_list
    assert new_list != list


def test_delete():

    """
    Functia de test a functiei 'detele' din crud.py
    """

    list = get_data()
    random_expense = getnewexpense(8, 6, 332, '05.07.2016', 'canal')
    new_list = delete(list, get_id(random_expense))
    assert len(list) == len(new_list) + 1
    assert random_expense not in new_list


def test_crud():

    """
    Functia de test generala
    """

    test_create()
    test_read()
    test_update()
    test_delete()
