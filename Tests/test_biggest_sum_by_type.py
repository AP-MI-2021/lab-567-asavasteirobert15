from Domain.expense import getnewexpense
from Logic.biggest_sum_by_type import biggest_sum_by_type


def get_data():

    """
    Functie suport pentru functiile de test
    """

    return \
        [
            getnewexpense(20, 1, 123, '17.08.2018', 'canal'),
            getnewexpense(30, 2, 200, '07.03.2020', 'intretinere'),
            getnewexpense(19, 3, 390, '15.05.2019', 'alte cheltuieli'),
            getnewexpense(8, 2, 332, '05.07.2016', 'alte cheltuieli'),
            getnewexpense(23, 2, 1000, '12.12.2020', 'canal')

        ]


def test_biggest_sum_by_type():
    list = get_data()
    max_canal = biggest_sum_by_type(list, 'canal')
    max_intretinere = biggest_sum_by_type(list, 'intretinere')
    max_alte_cheltuieli = biggest_sum_by_type(list, 'alte cheltuieli')
    assert max_canal is not 0 and max_intretinere is not 0 and max_alte_cheltuieli is not 0
    assert max_canal == 1000
    assert max_intretinere == 200
    assert max_alte_cheltuieli == 390
