def getnewexpense(_nr_apartment: int, _sum: int, _data: str, _type: str):

    """
    FUnctia creeaza o noua cheltuiala ca si lista
    :param _nr_apartment: int :numarul apartamentului caruia ii revine cheltuiala
    :param _sum: int :suma cheltuielii
    :param _data: str : data cheltuielii
    :param _type: str : tipul cheltuielii
    :return: noua cheltuiala
    """

    expense_as_list = [_nr_apartment, _sum, _data, _type]

    return expense_as_list

"""
Urmatoarele functii sunt functii tip get 
"""


def get_nr_apartment(expense_as_list):
    return expense_as_list[0]


def get_sum(expense_as_list):
    return expense_as_list[1]


def get_data(expense_as_list):
    return expense_as_list[2]


def get_type(expense_as_list):
    return expense_as_list[3]


def get_expense_into_string(expense_as_list):

    """
    Functia permite citirea unei cheltuieli ca si string
    :param expense: list: cheltuiala ce trebuie citita/afisata
    """

    return f'Cheltuiala de la apartamentul {get_nr_apartment(expense_as_list)} este in valoare de {get_sum(expense_as_list)} din data '\
           f'de {get_data(expense_as_list)}, avand tipul {get_type(expense_as_list)}'
