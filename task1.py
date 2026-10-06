import pandas as pd

df = pd.DataFrame({
    "Employee": ["A", "B", "C", "D", "E"],
    "Department": ["Sales", "Sales", "Marketing", "Sales", "Marketing"],
    "Experience": [1, 2, 3, 4, 5],
    "Monthly_Sales": [25000, 32000, 28000, 40000, 45000]
})

print("Average:", df["Monthly_Sales"].mean())
print("Median:", df["Monthly_Sales"].median())
print("Highest:", df["Monthly_Sales"].max())
print(df.groupby("Department")["Monthly_Sales"].mean())

