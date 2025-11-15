import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("example.csv")

print("Columns available in the dataset:")
print(list(df.columns))

print("\nChoose a visualization type:")
print("1. Line Plot")
print("2. Bar Plot")
print("3. Scatter Plot")

choice = input("Enter your choice (1/2/3): ")

x_col = input("Enter column name for x-axis: ")
y_col = input("Enter column name for y-axis: ")

if choice == '1':
    plt.plot(df[x_col], df[y_col])
    plt.title("Line Plot")
elif choice == '2':
    plt.bar(df[x_col], df[y_col])
    plt.title("Bar Plot")
elif choice == '3':
    plt.scatter(df[x_col], df[y_col])
    plt.title("Scatter Plot")
else:
    print("Invalid choice.")
    exit()
    
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.show()