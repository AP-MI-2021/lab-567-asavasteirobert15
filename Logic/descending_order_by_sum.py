from Domain.expense import get_sum


def descending_order_by_sum(expense_list: list):
    """
    Functia ordoneaza cheltuielile descrescator in fuctie de suma
    :param expense_list: lista cu cheltuieli
    :return: lista cu cheltuieli sortata
    """

    return sorted(expense_list, key=get_sum, reverse = True)
