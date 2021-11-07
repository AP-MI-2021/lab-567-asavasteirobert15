from Domain.expense import getnewexpense
from Logic.descending_order_by_sum import descending_order_by_sum


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


def test_descending_order_by_sum():

    """
    Functia de test pt descending_order_by_sum
    """

    list = get_data()
    list2 = get_data()
    list2 = descending_order_by_sum(list2)
    assert len(list) == len(list2)
    assert list[4] == list2[0]
    assert list[1] == list2[3]




