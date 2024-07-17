import matplotlib.pyplot as plt
years = [year for year in range(2014,2022)]
income = [55,56,62,61,72,72,73,75]
income_ticks = list(range(50,81, 2))
plt.plot(years, income)
plt.title("Income of John (is USD)")
plt.xlabel("Year")
plt.ylabel("Yearly Income in USD")
plt.yticks(income_ticks, [f"{x}k USD" for x in income_ticks])
plt.show()
