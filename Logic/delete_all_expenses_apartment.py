from Domain.expense import get_nr_apartment


def delete_all_expenses_apartment(expense_list: list, _nr_apartment: int):

    """
    Functia sterge toate cheltuielile unui apartament dat
    :param expense_list: list : lista cu toate cheltuielile
    :param _nr_apartment: : int : numarul apartamentului a carui cheltuieli trebuiesc sterse
    :return: list : lista noua modificata
    """

    result_list = []
    for expense in expense_list:
        if get_nr_apartment(expense) != _nr_apartment:
            result_list.append(expense)

    return result_list
