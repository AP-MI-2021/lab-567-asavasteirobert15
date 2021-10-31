from Domain.expense import get_sum, get_type


def biggest_sum_by_type(cheltuieli: list, _type: str):
    """
    Fucntia returneaza cea mai mare valoare a cheltuielilor de un anumit tip
    :param cheltuieli: list : lista de cheltuieli
    :param _type: str : tip-ul caracteristic
    :return:
    """
    sum_max = 0
    for cheltuiala in cheltuieli:
        if get_sum(cheltuiala) > sum_max and get_type(cheltuiala) == _type:
            sum_max = get_sum(cheltuiala)

    return sum_max
