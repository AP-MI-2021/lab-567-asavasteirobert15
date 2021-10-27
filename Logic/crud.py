from Domain.expense import getnewexpense, get_nr_apartment


def create(expense_list: list, _nr_apartment: int, _sum: int, _data: str, _type: str):

    """
    Functia creeaza o noua cheltuiala
    :param expense_list: list : lista cu cheltuieli
    :param _nr_apartment: int : numarul apartamentului caruia ii revine cheltuiala
    :param _sum: int : suma cheltuielii
    :param _data: str : data cheltuielii
    :param _type: str : tipul cheltuielii
    :return: list : lista cu cheltiala noua adaugata
    """

    expense = getnewexpense(_nr_apartment, _sum, _data, _type)
    return expense_list + [expense]


def read(expense_list: list, _nr_apartment: int = None):

    """
    Fuctia returneaza o cheltuiala anume cautata, sau , in functie de caz , lista totala
    :param expense_list: list : lista cu cheltuieli
    :param _nr_apartment: int : numarul apartamentului a carui cheltuiala se doreste a fi "citita"
    :return: cheltuiala cautata , sau lista cu toate cheltuielile, dupa nevoile utilizatorului
    """

    found_expense = None
    if _nr_apartment is None:
        return expense_list
    for expense in expense_list:
        if get_nr_apartment(expense) == _nr_apartment:
            found_expense = expense

    return found_expense


def update(expense_list: list, new_expense):

    """
    Functia da update la o anumita cheltuiala
    :param expense_list: list : lista totala cu cheltuieli
    :param new_expense: dictionary : cheltuiala care se doreste a fi modificata
    :return: list : noua lista cu cheltuiala ceruta modificata
    """

    result_expense_list = []
    for expense in expense_list:
        if get_nr_apartment(new_expense) == get_nr_apartment(expense):
            result_expense_list.append(new_expense)
        else:
            result_expense_list.append(expense)

    return result_expense_list


def delete(expense_list: list, _nr_apartment: int):

    """
    Functia sterge din lista totala o anumita cheltuiala
    :param expense_list: list : lista totala cu cheltuieli
    :param _nr_apartment: int : numarul apartamentului a carui cheltuiala se doreste a fi stearsa
    :return: list: lista finala dupa stergerea cheltuielii
    """

    result_expense_list = []
    for expense in expense_list:
        if get_nr_apartment(expense) != _nr_apartment:
            result_expense_list.append(expense)

    return result_expense_list
