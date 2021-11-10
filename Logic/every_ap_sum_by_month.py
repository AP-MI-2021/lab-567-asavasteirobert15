from Domain.expense import get_data, get_nr_apartment, get_sum


def get_month(expense):

    """
    functia returneaza dintr-o data a unei cheltuieli
    :param expense: cheltuiala
    :return: luna dintr-o data
    """

    data = get_data(expense)
    data_split = data.split('.')
    return data_split[1]


def ap_list(expense_list):

    """
    creeaza o lista cu toate nr de apartament
    :param expense_list: lista de apartamente
    :return: lista cu nr de apartament
    """

    ap_list = []
    for cheltuiala in expense_list:
        if get_nr_apartment(cheltuiala) not in ap_list:
            ap_list.append(get_nr_apartment(cheltuiala))

    return ap_list


def list_sum_by_month(expense_list, apartments_list):
    """
    Creeaza o lista de liste care contin sumele lunare pt fiecare apartament
    list_sum_by_month = [[ian1, feb1, ..., dec1], [ian2, feb2, ..., dec2], ... , [ian10, feb10, ..., dec10]
    """
    lst_sume_lunare = []
    for ap in apartments_list:
        lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for cheltuiala in expense_list:
            if get_nr_apartment(cheltuiala) == ap:
                if get_month(cheltuiala) == '01':
                    lst[0] += get_sum(cheltuiala)

                elif get_month(cheltuiala) == '02':
                    lst[1] += get_sum(cheltuiala)

                elif get_month(cheltuiala) == '03':
                    lst[2] += get_sum(cheltuiala)

                elif get_month(cheltuiala) == '04':
                    lst[3] += get_sum(cheltuiala)

                elif get_month(cheltuiala) == '05':
                    lst[4] += get_sum(cheltuiala)

                elif get_month(cheltuiala) == '06':
                    lst[5] += get_sum(cheltuiala)

                elif get_month(cheltuiala) == '07':
                    lst[6] += get_sum(cheltuiala)

                elif get_month(cheltuiala) == '08':
                    lst[7] += get_sum(cheltuiala)

                elif get_month(cheltuiala) == '09':
                    lst[8] += get_sum(cheltuiala)

                elif get_month(cheltuiala) == '10':
                    lst[9] += get_sum(cheltuiala)

                elif get_month(cheltuiala) == '11':
                    lst[10] += get_sum(cheltuiala)

                elif get_month(cheltuiala) == '12':
                    lst[11] += get_sum(cheltuiala)
        lst_sume_lunare.append(lst)

    return lst_sume_lunare
