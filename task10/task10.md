1. Problem Statement
The Multi-Branch Sales Matrix Comparison system stores product sales data for multiple branches across different days using nested lists. The program calculates the total sales of each product, determines the overall sales of each branch, compares branch performance, and identifies the best-performing product in each branch. Finally, it displays the sales matrix, product-wise totals, branch-wise totals, the highest-performing branch, and the best-selling product for each branch.
2. Algorithm
1. Start the program.
2. Initialize the branch names, product names, and daily sales data using nested lists.
3. Display the sales matrix for all branches and products.
4. Calculate the total sales of each product across all branches and days.
5. Calculate the total sales of each branch.
6. Compare the branch totals to identify the highest-performing branch.
7. For each branch, calculate the total sales of every product across all days.
8. Identify the product with the highest sales in each branch.
9. Display the product-wise sales totals.
10. Display the branch-wise sales totals.
11. Display the best-performing branch and the best-selling product in each branch.
12. Stop the program.
13. flowchart
14. ```mermaid
flowchart TD
    A([Start]) --> B[Initialize branches products and sales matrix]
    B --> C[Display sales matrix]
    C --> D[Calculate total sales for each product]
    D --> E[Calculate total sales for each branch]
    E --> F[Compare branch totals]
    F --> G[Identify highest performing branch]
    G --> H[Calculate product totals for each branch]
    H --> I[Identify best performing product in each branch]
    I --> J[Display product and branch sales reports]
    J --> K([Stop])
```
code:
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
output:
=================================================================
          MULTI-BRANCH SALES MATRIX COMPARISON
=================================================================

 Branch A
---------------------------------------------
Laptop Daily Sales: [10, 12, 8] Total: 30
Mobile Daily Sales: [20, 18, 22] Total: 60
Headphones Daily Sales: [15, 12, 10] Total: 37
Total Branch Sales: 127

 Branch B
---------------------------------------------
Laptop Daily Sales: [14, 10, 11] Total: 35
Mobile Daily Sales: [25, 20, 18] Total: 63
Headphones Daily Sales: [12, 15, 14] Total: 41
Total Branch Sales: 139

 Branch C
---------------------------------------------
Laptop Daily Sales: [8, 9, 10] Total: 27
Mobile Daily Sales: [18, 22, 20] Total: 60
Headphones Daily Sales: [20, 18, 17] Total: 55
Total Branch Sales: 142

=================================================================
PRODUCT-WISE TOTAL SALES
=================================================================
Laptop : 92
Mobile : 183
Headphones : 133

=================================================================
BRANCH PERFORMANCE COMPARISON
=================================================================
Branch A Total Sales: 127
Branch B Total Sales: 139
Branch C Total Sales: 142

Highest Performing Branch: Branch C with sales of 142

=================================================================
BEST-PERFORMING PRODUCT IN EACH BRANCH
=================================================================
Branch A -> Mobile with sales of 60
Branch B -> Mobile with sales of 63
Branch C -> Mobile with sales of 60

Sales analysis completed successfully.
=================================================================
