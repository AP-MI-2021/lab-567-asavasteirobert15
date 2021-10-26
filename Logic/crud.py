from Domain.expense import getnewexpense, get_nr_apartment


def create(expense_list: list, _nr_apartment: int, _sum: int, _data: str, _type: str):
    expense = getnewexpense(_nr_apartment, _sum, _data, _type)
    return expense_list + [expense]


def read(expense_list: list, _nr_apartment: int = None):
    found_expense = None
    if _nr_apartment is None:
        return expense_list
    for expense in expense_list:
        if get_nr_apartment(expense) == _nr_apartment:
            found_expense = expense

    return found_expense


def update(expense_list: list, new_expense):
    result_expense_list = []
    for expense in expense_list:
        if get_nr_apartment(new_expense) == get_nr_apartment(expense):
            result_expense_list.append(new_expense)
        else:
            result_expense_list.append(expense)

    return result_expense_list


def delete(expense_list: list, _nr_apartment: int):
    result_expense_list = []
    for expense in expense_list:
        if get_nr_apartment(expense) != _nr_apartment:
            result_expense_list.append(expense)

    return result_expense_list
