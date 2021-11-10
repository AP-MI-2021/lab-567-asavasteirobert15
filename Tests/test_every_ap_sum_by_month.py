from Domain.expense import getnewexpense
from Logic.every_ap_sum_by_month import list_sum_by_month


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


def test_every_ap_sum_by_month():
    list = get_data()
    list_ap = [1, 2, 3]
    assert list_sum_by_month(list, list_ap) == [[0, 0, 0, 0, 0, 0, 0, 123, 0, 0, 0, 0],
                                                [0, 0, 200, 0, 0, 0, 332, 0, 0, 0, 0, 1000],
                                                [0, 0, 0, 0, 390, 0, 0, 0, 0, 0, 0, 0]]
