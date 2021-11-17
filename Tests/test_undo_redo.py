from Domain.expense import getnewexpense
from Logic.add_value_if_date import add_value_if_date
from Logic.crud import create
from UI.console import handle_undo, handle_redo, handle_list_versions


def test_undo_redo():
    lista_cheltuiala = []
    list_version = [lista_cheltuiala]
    current_version = 0
    lista_cheltuiala = create(lista_cheltuiala, 1, 20, 200, '12.12.2012', 'canal' )
    list_version, current_version = handle_list_versions(list_version, current_version, lista_cheltuiala)
    lista_cheltuiala = create(lista_cheltuiala, 2, 19, 130, '12.02.2002', 'canal')
    list_version, current_version = handle_list_versions(list_version, current_version, lista_cheltuiala)
    lista_cheltuiala = create(lista_cheltuiala, 3, 8, 1000, '12.10.2019', 'intretinere')
    list_version, current_version = handle_list_versions(list_version, current_version, lista_cheltuiala)
    lista_cheltuiala, current_version = handle_undo(list_version, current_version)
    assert len(lista_cheltuiala) == 2
    lista_cheltuiala, current_version = handle_undo(list_version, current_version)
    assert len(lista_cheltuiala) == 1
    lista_cheltuiala, current_version = handle_undo(list_version, current_version)
    assert len(lista_cheltuiala) == 0
    lista_cheltuiala, current_version = handle_undo(list_version, current_version)
    assert len(lista_cheltuiala) == 0
    lista_cheltuiala = create(lista_cheltuiala, 1, 20, 200, '12.12.2012', 'canal' )
    list_version, current_version = handle_list_versions(list_version, current_version, lista_cheltuiala)
    lista_cheltuiala = create(lista_cheltuiala, 2, 19, 130, '12.02.2002', 'canal')
    list_version, current_version = handle_list_versions(list_version, current_version, lista_cheltuiala)
    lista_cheltuiala = create(lista_cheltuiala, 3, 8, 1000, '12.10.2019', 'intretinere')
    list_version, current_version = handle_list_versions(list_version, current_version, lista_cheltuiala)
    lista_cheltuiala, current_version = handle_redo(list_version, current_version)
    assert len(lista_cheltuiala) == 3
    lista_cheltuiala, current_version = handle_undo(list_version, current_version)
    lista_cheltuiala, current_version = handle_undo(list_version, current_version)
    assert len(lista_cheltuiala) == 1
    lista_cheltuiala, current_version = handle_redo(list_version, current_version)
    assert len(lista_cheltuiala) == 2
    lista_cheltuiala, current_version = handle_redo(list_version, current_version)
    assert len(lista_cheltuiala) == 3



