from django.contrib import admin

from api.models import Currency,IncomeCategory,ExpensesCategory,Income,Expense,Balance

# Register your models here.

admin.site.register(Currency)
admin.site.register(IncomeCategory)
admin.site.register(ExpensesCategory)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Balance)