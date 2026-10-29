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
