1. Problem Statement
The ATM Transaction Sequence Simulation system simulates basic banking operations, including deposits and withdrawals. It maintains the account balance throughout a sequence of transactions, checks whether withdrawals exceed the available balance or a specified withdrawal limit, and rejects invalid transactions such as negative amounts or zero-value transactions. Finally, the program generates a transaction summary showing successful transactions, rejected transactions, the final account balance, and the total amounts deposited and withdrawn.
2. Algorithm
1. Start the program.
2. Initialize the account balance and maximum withdrawal limit.
3. Initialize the transaction history and transaction counters.
4. Read a sequence of deposit and withdrawal transactions.
5. Check whether the transaction amount is valid and positive.
6. If the transaction is a deposit, add the amount to the account balance.
7. If the transaction is a withdrawal, check whether the amount exceeds the withdrawal limit.
8. Check whether sufficient balance is available.
9. If all withdrawal conditions are satisfied, subtract the amount from the balance; otherwise, reject the transaction.
10. Reject transactions with invalid transaction types or invalid amounts.
11. Record the result of each transaction.
12. Display the transaction history.
13. Display the total deposits, total withdrawals, successful transactions, rejected transactions, and final balance.
14. Stop the program.
15. flowchart
16. ```mermaid
flowchart TD
    A([Start]) --> B[Initialize balance and withdrawal limit]
    B --> C[Read transaction type and amount]
    C --> D{Is amount positive?}
    D -- No --> E[Reject invalid amount]
    D -- Yes --> F{Transaction type?}
    F -- Deposit --> G[Add amount to balance]
    F -- Withdrawal --> H{Within withdrawal limit?}
    F -- Other --> I[Reject invalid transaction type]
    H -- No --> J[Reject withdrawal]
    H -- Yes --> K{Sufficient balance?}
    K -- No --> J
    K -- Yes --> L[Subtract amount from balance]
    E --> M[Record transaction result]
    G --> M
    I --> M
    J --> M
    L --> M
    M --> N{More transactions?}
    N -- Yes --> C
    N -- No --> O[Display transaction summary]
    O --> P([End])
```
code
# ATM Transaction Sequence Simulation

# Initial account details
balance = 5000
withdrawal_limit = 2000

# Transaction sequence: (type, amount)
transactions = [
    ("Deposit", 1500),
    ("Withdrawal", 1000),
    ("Withdrawal", 2500),
    ("Deposit", 2000),
    ("Withdrawal", 6000),
    ("Withdrawal", -500),
    ("Transfer", 500),
    ("Withdrawal", 1500)
]

# Initialize counters
total_deposits = 0
total_withdrawals = 0
successful = 0
rejected = 0

# Store transaction history
history = []

# Process each transaction
for transaction_type, amount in transactions:
    status = ""

    # Validate transaction amount
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        status = "Rejected: Invalid amount"

    elif amount <= 0:
        status = "Rejected: Amount must be positive"

    elif transaction_type == "Deposit":
        balance += amount
        total_deposits += amount
        successful += 1
        status = "Successful"
    elif transaction_type == "Withdrawal":
        if amount > withdrawal_limit:
            status = "Rejected: Exceeds withdrawal limit"
        elif amount > balance:
            status = "Rejected: Insufficient balance"
        else:
            balance -= amount
            total_withdrawals += amount
            successful += 1
            status = "Successful"
    else:
        status = "Rejected: Invalid transaction type"
    # Count rejected transactions
    if status.startswith("Rejected"):
        rejected += 1
    # Record transaction
    history.append(
        (transaction_type, amount, status, balance)
    )
# Display transaction history
print("=" * 75)
print("                 ATM TRANSACTION SUMMARY")
print("=" * 75)
print(f"{'Type':<15}{'Amount':<12}{'Status':<38}{'Balance':>10}")
print("-" * 75)
for transaction in history:
    transaction_type, amount, status, current_balance = transaction

    print(
        f"{transaction_type:<15}"
        f"{amount:<12}"
        f"{status:<38}"
        f"{current_balance:>10.2f}"
    )
print("-" * 75)
print("Total Deposits       : Rs.", total_deposits)
print("Total Withdrawals    : Rs.", total_withdrawals)
print("Successful Transactions:", successful)
print("Rejected Transactions  :", rejected)
print("Final Account Balance : Rs.", balance)
print("=" * 75)
output:
===========================================================================
                 ATM TRANSACTION SUMMARY
===========================================================================
Type           Amount      Status                                   Balance
---------------------------------------------------------------------------
Deposit        1500        Successful                              6500.00
Withdrawal     1000        Successful                              5500.00
Withdrawal     2500        Rejected: Exceeds withdrawal limit      5500.00
Deposit        2000        Successful                              7500.00
Withdrawal     6000        Rejected: Exceeds withdrawal limit      7500.00
Withdrawal     -500        Rejected: Amount must be positive      7500.00
Transfer       500         Rejected: Invalid transaction type     7500.00
Withdrawal     1500        Successful                              6000.00
---------------------------------------------------------------------------
Total Deposits       : Rs. 3500
Total Withdrawals    : Rs. 3500
Successful Transactions: 4
Rejected Transactions  : 4
Final Account Balance : Rs. 6000
===========================================================================
