from Domain.expense import getnewexpense, get_sum
from Logic.add_value_if_date import add_value_if_date


def get_data():

    """
    Functie suport pentru functiile de test
    """

    return \
        [
            getnewexpense(20, 1, 123, '17.08.2018', 'canal'),
            getnewexpense(30, 2, 200, '07.03.2020', 'intretinere'),
            getnewexpense(19, 3, 390, '12.12.2020', 'alte cheltuieli'),
            getnewexpense(8, 6, 332, '05.07.2016', 'canal'),
            getnewexpense(23, 9, 1000, '12.12.2020', 'canal')

        ]



def test_add_value_if_date():
    list = get_data()
    list2 = get_data()
    list2 = add_value_if_date(list2, '12.12.2020', 400)
    assert len(list2) == len(list)
    assert get_sum(list[2]) + 400 == get_sum(list2[2])
