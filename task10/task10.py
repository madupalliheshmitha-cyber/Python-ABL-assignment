# Multi-Branch Sales Matrix Comparison

branches = ["Branch A", "Branch B", "Branch C"]

products = ["Laptop", "Mobile", "Headphones"]

# Sales data: Branch -> Product -> Daily sales
sales = [
    [
        [10, 12, 8],
        [20, 18, 22],
        [15, 12, 10]
    ],
    [
        [14, 10, 11],
        [25, 20, 18],
        [12, 15, 14]
    ],
    [
        [8, 9, 10],
        [18, 22, 20],
        [20, 18, 17]
    ]
]

branch_totals = []
product_totals = [0] * len(products)

print("=" * 65)
print("          MULTI-BRANCH SALES MATRIX COMPARISON")
print("=" * 65)

# Display daily sales and calculate branch totals
for i in range(len(branches)):
    print("\n", branches[i])
    print("-" * 45)

    branch_total = 0

    for j in range(len(products)):
        product_total = sum(sales[i][j])
        branch_total += product_total
        product_totals[j] += product_total

        print(
            products[j],
            "Daily Sales:", sales[i][j],
            "Total:", product_total
        )

    branch_totals.append(branch_total)
    print("Total Branch Sales:", branch_total)

# Display product-wise totals
print("\n" + "=" * 65)
print("PRODUCT-WISE TOTAL SALES")
print("=" * 65)

for i in range(len(products)):
    print(products[i], ":", product_totals[i])

# Identify highest-performing branch
best_branch_index = branch_totals.index(max(branch_totals))

print("\n" + "=" * 65)
print("BRANCH PERFORMANCE COMPARISON")
print("=" * 65)

for i in range(len(branches)):
    print(branches[i], "Total Sales:", branch_totals[i])

print(
    "\nHighest Performing Branch:",
    branches[best_branch_index],
    "with sales of",
    branch_totals[best_branch_index]
)

# Identify best-performing product in each branch
print("\n" + "=" * 65)
print("BEST-PERFORMING PRODUCT IN EACH BRANCH")
print("=" * 65)

for i in range(len(branches)):
    product_branch_totals = []

    for j in range(len(products)):
        product_branch_totals.append(sum(sales[i][j]))

    best_product_index = product_branch_totals.index(
        max(product_branch_totals)
    )

    print(
        branches[i],
        "->",
        products[best_product_index],
        "with sales of",
        product_branch_totals[best_product_index]
    )

print("\nSales analysis completed successfully.")
print("=" * 65)
