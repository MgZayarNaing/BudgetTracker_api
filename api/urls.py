from django.urls import path
from api.views.currency_views import (
    currency_list,
    currency_create,
    currency_detail,
    currency_update,
    currency_delete,
)
from api.views.incomecategory_views import (
    income_category_list,
    income_category_create,
    income_category_detail,
    income_category_update,
    income_category_delete,
)

from api.views.expensescategory_views import (
    expenses_category_list,
    expenses_category_create,
    expenses_category_detail,
    expenses_category_update,
    expenses_category_delete,
)

from api.views.income_views import (
    income_list,
    income_create,
    income_detail,
    income_update,
    income_delete,
    total_income,
)

from api.views.expense_views import (
    expense_list,
    expense_create,
    expense_detail,
    expense_update,
    expense_delete,
    total_expense,
)

from api.views.balance_views import get_balance

urlpatterns = [

    path('currencies/', currency_list, name='currency-list'),
    path('currencies/create/', currency_create, name='currency-create'),
    path('currencies/<int:pk>/', currency_detail, name='currency-detail'),
    path('currencies/<int:pk>/update/', currency_update, name='currency-update'),
    path('currencies/<int:pk>/delete/', currency_delete, name='currency-delete'),

    path('incomecategories/', income_category_list, name='income-category-list'),
    path('incomecategories/create/', income_category_create, name='income-category-create'),
    path('incomecategories/<int:pk>/', income_category_detail, name='income-category-detail'),
    path('incomecategories/<int:pk>/update/', income_category_update, name='income-category-update'),
    path('incomecategories/<int:pk>/delete/', income_category_delete, name='income-category-delete'),

    path('expensescategories/', expenses_category_list, name='expenses-category-list'),
    path('expensescategories/create/', expenses_category_create, name='expenses-category-create'),
    path('expensescategories/<int:pk>/', expenses_category_detail, name='expenses-category-detail'),
    path('expensescategories/<int:pk>/update/', expenses_category_update, name='expenses-category-update'),
    path('expensescategories/<int:pk>/delete/', expenses_category_delete, name='expenses-category-delete'),

    path('incomes/', income_list, name='income-list'),
    path('incomes/create/', income_create, name='income-create'),
    path('incomes/<int:pk>/', income_detail, name='income-detail'),
    path('incomes/<int:pk>/update/', income_update, name='income-update'),
    path('incomes/<int:pk>/delete/', income_delete, name='income-delete'),
    path('incomes/total/', total_income, name='total-income'),

    path('expenses/', expense_list, name='expense-list'),
    path('expenses/create/', expense_create, name='expense-create'),
    path('expenses/<int:pk>/', expense_detail, name='expense-detail'),
    path('expenses/<int:pk>/update/', expense_update, name='expense-update'),
    path('expenses/<int:pk>/delete/', expense_delete, name='expense-delete'),
    path('expenses/total/', total_expense, name='total-expense'),

    path('balance/', get_balance, name='get-balance'),

]


