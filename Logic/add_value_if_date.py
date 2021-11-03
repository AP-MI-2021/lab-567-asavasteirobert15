from Domain.expense import get_data


def add_value_if_date(cheltuieli: list, data: str, value: float):
    """
    Functia aduna o valoare la suma tuturor cheltuielilor dintr-o data
    :param cheltuieli: list : lista cu cheltuieli
    :param data: str : data citita
    :param value: float : valoare ce va trebui adunata
    :return:
    """
    new_list = []
    for cheltuiala in cheltuieli:
        if get_data(cheltuiala) == data:
            cheltuiala['sum'] = cheltuiala['sum'] + value
            new_list.append(cheltuiala)
        else:
            new_list.append(cheltuiala)

    return new_list
