from Tests.test_add_value_if_date import test_add_value_if_date
from Tests.test_biggest_sum_by_type import test_biggest_sum_by_type
from Tests.test_delete_all_expenses_apartment import test_delete_all_expenses_apartment
from Tests.tests_for_crud import test_crud
from UI.console import main

test_crud()
test_delete_all_expenses_apartment()
test_add_value_if_date()
test_biggest_sum_by_type()

main()