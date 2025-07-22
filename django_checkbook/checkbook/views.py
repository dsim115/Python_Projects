from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# Home page with account dropdown
def home(request):
    accounts = Account.objects.all()
    return render(request, 'checkbook/index.html', {'accounts': accounts})


# Create new account
def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AccountForm()
    return render(request, 'checkbook/CreateNewAccount.html', {'form': form})


# View account balance and transactions
def view_balance(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    transactions = Transaction.objects.filter(account=account)

    balance = account.starting_balance
    for transaction in transactions:
        if transaction.transaction_type == 'Deposit':
            balance += transaction.amount
        elif transaction.transaction_type == 'Withdrawal':
            balance -= transaction.amount

    return render(request, 'checkbook/BalanceSheet.html', {
        'account': account,
        'transactions': transactions,
        'balance': balance,
    })


# Add new transaction
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransactionForm()
    return render(request, 'checkbook/AddTransaction.html', {'form': form})
