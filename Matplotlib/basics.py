import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [10, 20, 30, 40]

# plt.plot(x, y)

# plt.show() # line graph

# labels for easy readability...

# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("Simple Graph")

# plt.show()
# -------------------------------------------------
# line plot:
# x = [1, 2, 3, 4]
# y = [10, 20, 15, 30]

# plt.plot(x, y)

# plt.show()

# bar plot:
# students = ["John", "Alice", "Bob"]
# marks = [80, 90, 70]

# plt.bar(students, marks)

# plt.show()

# scatter plots:
# x = [1, 2, 3, 4]
# y = [10, 20, 15, 30]

# plt.scatter(x, y)

# plt.show()

# creating figure:

# fig = plt.figure()

# print(fig)

# figure and axes:

# fig, ax = plt.subplots()

# ax.plot([1, 2, 3], [10, 20, 30])

# plt.show()
# -------------------------------------------------
# a complete figure with labels, title and legends...

# months = ["Jan", "Feb", "Mar", "Apr"]
# sales_2024 = [10, 20, 25, 30]
# sales_2025 = [15, 25, 35, 45]

# plt.plot(months, sales_2024, label="2024")
# plt.plot(months, sales_2025, label="2025")

# plt.title("Company Sales Comparison")
# plt.xlabel("Months")
# plt.ylabel("Sales in Lakhs")
# plt.legend()

# plt.show()