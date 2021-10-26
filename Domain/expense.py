def getnewexpense(_nr_apartment: int, _sum: int, _data: str, _type: str):
    new_expense = \
        {
            'nr_apartment': _nr_apartment,
            'sum': _sum,
            'data': _data,
            'type': _type
        }
    return new_expense


def get_nr_apartment(expense):
    return expense['nr_apartment']


def get_sum(expense):
    return expense['sum']


def get_data(expense):
    return expense['data']


def get_type(expense):
    return expense['type']


def get_expense_into_string(expense):
    return f'Cheltuiala de la apartamentul {get_nr_apartment(expense)} este in valoare de {get_sum(expense)} din data '\
           f'de {get_data(expense)}, avand tipul {get_type(expense)}'
