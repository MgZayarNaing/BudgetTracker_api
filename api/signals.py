from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Income, Expense, Balance

@receiver(post_save, sender=Income)
def update_balance_on_income_create(sender, instance, created, **kwargs):
    if created:
        balance, created = Balance.objects.get_or_create(user=instance.user)
        balance.amount += int(instance.amount)
        balance.save()

@receiver(post_delete, sender=Income)
def update_balance_on_income_delete(sender, instance, **kwargs):
    balance, created = Balance.objects.get_or_create(user=instance.user)
    balance.amount -= int(instance.amount)
    balance.save()

@receiver(post_save, sender=Expense)
def update_balance_on_expense_create(sender, instance, created, **kwargs):
    if created:
        balance, created = Balance.objects.get_or_create(user=instance.user)
        balance.amount -= int(instance.amount)
        balance.save()

@receiver(post_delete, sender=Expense)
def update_balance_on_expense_delete(sender, instance, **kwargs):
    balance, created = Balance.objects.get_or_create(user=instance.user)
    balance.amount += int(instance.amount)
    balance.save()
