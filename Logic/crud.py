from Domain.expense import getnewexpense, get_id


def create(expense_list: list, _id: int, _nr_apartment: int, _sum: int, _data: str, _type: str):

    """
    Functia creeaza o noua cheltuiala
    :param expense_list: list : lista cu cheltuieli
    :param _id : int : id-ul cheltuielii
    :param _nr_apartment: int : numarul apartamentului caruia ii revine cheltuiala
    :param _sum: int : suma cheltuielii
    :param _data: str : data cheltuielii
    :param _type: str : tipul cheltuielii
    :return: list : lista cu cheltiala noua adaugata
    """

    if _type != 'canal' and _type != 'intretinere' and _type != 'alte cheltuieli':
        raise ValueError('Tipul nu poate fi acceptat!')
    if len(_data) != 10:
        raise ValueError('Data trebuie sa fie in format DD.MM.YYYY !!!')
    for expense in expense_list:
        if _id == get_id(expense):
            raise ValueError('Id-ul trebuie sa fie unic!')
    expense = getnewexpense(_id, _nr_apartment, _sum, _data, _type)
    return expense_list + [expense]


def read(expense_list: list, _id: int = None):

    """
    Fuctia returneaza o cheltuiala anume cautata, sau , in functie de caz , lista totala
    :param expense_list: list : lista cu cheltuieli
    :param _id : int : id-ul cheltuielii
    :return: cheltuiala cautata , sau lista cu toate cheltuielile, dupa nevoile utilizatorului
    """

    found_expense = None
    if _id is None:
        return expense_list
    for expense in expense_list:
        if get_id(expense) == _id:
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
        if get_id(new_expense) == get_id(expense):
            result_expense_list.append(new_expense)
        else:
            result_expense_list.append(expense)

    return result_expense_list


def delete(expense_list: list, _id: int):

    """
    Functia sterge din lista totala o anumita cheltuiala
    :param expense_list: list : lista totala cu cheltuieli
    :param _id : int : id-ul cheltuielii
    :return: list: lista finala dupa stergerea cheltuielii
    """

    result_expense_list = []
    for expense in expense_list:
        if get_id(expense) != _id:
            result_expense_list.append(expense)

    return result_expense_list
