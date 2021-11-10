from Domain.expense import getnewexpense
from Logic.add_value_if_date import add_value_if_date
from UI.console import handle_undo, handle_redo


def get_data():

    """
    Functie suport pentru functiile de test
    """

    return \
        [
            getnewexpense(20, 1, 123, '17.08.2018', 'canal'),
            getnewexpense(30, 2, 200, '12.12.2020', 'intretinere'),
            getnewexpense(19, 3, 390, '15.05.2019', 'alte cheltuieli'),
            getnewexpense(8, 2, 332, '05.07.2016', 'canal'),
            getnewexpense(23, 2, 1000, '12.12.2020', 'canal')

        ]


def test_undo_redo():
    list = get_data()
    list_versions = [[], list]
    current_version = 1
    new_list = add_value_if_date(list, '12.12.2020', 300)
    current_version += 1
    list_versions = list_versions + new_list
    list1, current_version = handle_undo(list_versions, current_version)
    assert list1 == list_versions[current_version]
    list1, current_version = handle_redo(list_versions, current_version)
    assert list1 == list_versions[current_version]



