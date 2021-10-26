
from Domain.expense import getnewexpense, get_type, get_expense_into_string
from Logic.crud import create, read, update, delete

lista = []
lista = create(lista, 7, 1239, '18.08.2013', 'intretinere')
lista = create(lista, 9, 200, '12.20.2012', 'canal')
print(lista)


cheltuiala1 = read(lista,7)
print(cheltuiala1)


cheltuiala_noua = getnewexpense(7, 700, '18.08.2013', 'intretinere + canal')
lista = update(lista, cheltuiala_noua)


cheltuiala1 = read(lista,7)
print(cheltuiala1)

lista = delete(lista, 9)
print(lista)